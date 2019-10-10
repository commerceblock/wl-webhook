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
        conf["token"]=f.readline().rstrip()
else:
    conf["token"]='tok1'

conf["idcheck_token"]=os.environ.get('IDCHECK_API_TOKEN', None)
    
p="/run/secrets/onfido_token"
if os.path.exists(p) and conf["idcheck_token"] == None:
    with open(p) as f:
        conf["idcheck_token"]=f.readline().rstrip()
else:
    conf["idcheck_token"]='tok2'


p=os.environ.get('SMTP_USERNAME_FILE', None)
if os.path.exists(p):
    with open(p) as f:
        smtp_conf["username"]=f.readline().rstrip()
else:
    smtp_conf["username"]=None

p=os.environ.get('SMTP_PASSWORD_FILE', None)
if os.path.exists(p):
    with open(p) as f:
        smtp_conf["password"]=f.readline().rstrip()
else:
    smtp_conf["password"]=None

p=os.environ.get('EMAIL_TEMPLATE_FILE', None)
if os.path.exists(p):
    with open(p) as f:
        smtp_conf["complete_template"]=Template(f.read())
else:
    smtp_conf["compete_template"]=None

p=os.environ.get('EMAIL_FAIL_TEMPLATE_FILE', None)
if os.path.exists(p):
    with open(p) as f:
        smtp_conf["fail_template"]=Template(f.read())
else:
    smtp_conf["fail_template"]=None

smtp_conf["server"]=os.environ.get('SMTP_SERVER',None)
smtp_conf["port"]=os.environ.get('SMTP_PORT',None)
smtp_conf["email_from"]=os.environ.get('SMTP_EMAIL_FROM',None)
smtp_conf["email_subject"]=os.environ.get('SMTP_EMAIL_SUBJECT',None)

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
                   consider_dir=conf["consider_dir"],
                   smtp_conf)
wh.init()

@app.route("/")
def hello():
    return str("Hello World from Flask in a uWSGI Nginx Docker container with \n \
    Python 3.7 (from the example template) \n") +  str(conf) + "\n" + str(wh.hello()) + str("\n")

@app.route("/", methods=['POST'])
def process_post():
    return wh.process_post(request)

if __name__ == "__main__":
    app.run(host=conf["host"], debug=True, port=conf["port"])
