from flask import Flask
app=Flask(__name__)

from cb_idcheck import webhook

wh=webhook.webhook(token='BDxgRCn6VrOTIthSkuF8OB4cOT4FBDwz',
                   log='whlog.txt',
                   id_api='onfido',
                   host='0.0.0.0',
                   port='80',
                   idcheck_token='api_sandbox.xc4F2HsUzVp.WuxI61HM1EmeIoP8ck4eX9t1h9sfiPp_',
                   whitelisted_dir='/app',
                   consider_dir='/app')

wh.run()


#class webhook:
#    def __init__():
#        app.run(host="0.0.0.0", debug=True, port=80)


#    @app.route("/")
#    def hello():
#        return "Hello World from Flask in a uWSGI Nginx Docker container with \
#        Python 3.7 (from the example template) :) :) :) Inside webhook class, app run in class :) hey hey"



#@app.route("/", methods=['POST'])
#def webhook():
#    if not authenticate(request):
#        logging.warning('cb_idcheck.webhook: ' + str(datetime.now()) + ': A request sent to the webhook failed authentication.')
#        abort(401) 
#        if(request.json["payload"]["action"]=="check.completed"):
#            print('completed check received')
#            report_list=self.id_api.list_reports(request.json["payload"]["object"]["id"])
#            if(self.verify_check_content(report_list) == False):
#                infostr='ID Check result: check does not contain all the required report types. The required report types are: ' + str(self.idcheck_config) +  '. The included report types are: '
#                print(infostr)
#                logging.info('%s', infostr)
#                pprint(report_list)
#            else:
#                message, retval = self.id_api.process_webhook_request(request)
#                if retval != None:
#                    print(message)
#                    logging.info('%s', message)
#                    return message, retval
#                else:
#                    print('ID Check result: fail')                        
#        elif(request.json["payload"]["action"]=="test_action"):
#            infostr='Test successful.'
#            print('Test successful.')
#            logging.info('%s', infostr)
#            return infostr, 200
#        logging.info('Unable to process request: %s', request.json)
#        abort(400)

#def authenticate(self, request):
#    key = urllib.parse.quote_plus(self.token).encode()
#    message = request.data
#    auth_code=hmac.new(key, message, hashlib.sha256).hexdigest()
#    return(auth_code == request.headers["X-Sha2-Signature"])
        



#if __name__ == "__main__":
#    # Only for debugging while developing
#    wh=webhook()

@app.route("/")
def hello():
    return wh.hello()
#    return "Hello World from Flask in a uWSGI Nginx Docker container with \n
#    Python 3.7 (from the example template) :) :) :) \n Inside webhook class, app run in class :) hey hey\n in main.py"



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
