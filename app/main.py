from flask import Flask
app=Flask(__name__)

from cb_idcheck import webhook

wh=webhook.webhook(token='',
                   log='whlog.txt',
                   id_api='onfido',
                   host='0.0.0.0',
                   port='80',
                   idcheck_token='',
                   whitelisted_dir='/app',
                   consider_dir='/app')

wh.run()

@app.route("/")
def hello():
    return str("Hello World from Flask in a uWSGI Nginx Docker container with \n \
    Python 3.7 (from the example template) \n") + str(wh.hello()) + str("\n")

@app.route("/", methods=['POST'])
def process_post():
    return wh.process_post(request)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
