import os
import pprint
import logging
from flask import Flask, request
app=Flask(__name__)

from cb_idcheck import webhook

conf={}

conf["token"]=os.environ.get('IDCHECK_WEBHOOK_TOKEN', None)

p="/run/secrets/onfido_webhook_token"
if os.path.exists(p) and conf["token"] == None:
    with open(p) as f:
        conf["token"]=f.readline()
else:
    conf["token"]='tok1'

conf["idcheck_token"]=os.environ.get('IDCHECK_API_TOKEN', None)
    
p="/run/secrets/onfido_token"
if os.path.exists(p) and conf["idcheck_token"] == None:
    with open(p) as f:
        conf["idcheck_token"]=f.readline()
else:
    conf["idcheck_token"]='tok2'


conf["port"]=os.environ.get('IDCHECK_WEBHOOK_PORT', None)
conf["log"]=os.environ.get('IDCHECK_LOG', '/usr/local/var/log/cb_idcheck.log')
conf["host"]=os.environ.get('IDCHECK_HOST', 'localhost')
conf["id_api"]=os.environ.get('ID_API', 'onfido')
conf["whitelisted_dir"]=os.environ.get('WHITELISTED_DIR', None)
conf["consider_dir"]=os.environ.get('CONSIDER_DIR', None)


wh=webhook.webhook(token=conf["token"],
                   log=conf["log"],
                   id_api=conf["id_api"],
                   idcheck_token=conf["idcheck_token"],
                   whitelisted_dir=conf["whitelisted_dir"],
                   consider_dir=conf["consider_dir"])

wh.init()

@app.route("/")
def hello():
    return str("Hello World from Flask in a uWSGI Nginx Docker container with \n \
    Python 3.7 (from the example template) \n") +  str(conf) + "\n" + str(wh.hello()) + str("\n")

@app.route("/", methods=['POST'])
def process_post():
    req=request
    logging.info('main:process_post() - request headers: %s', str(req.headers))
    logging.info('main:process_post() - request data: %s', str(req.data))
    pprint.pprint("main:process_post() - request headers: " +  str(req.headers))
    pprint.pprint("main:process_post() - request data: " +  str(req.data))
    return wh.process_post(req)

if __name__ == "__main__":
    app.run(host=conf["host"], debug=True, port=conf["port"])
