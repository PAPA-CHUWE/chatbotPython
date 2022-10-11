from email import message
import imp
from urllib import response
from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse 

app=Flask(__name__)

@app.route("/sms",methods=['POST'])

def reply():
    incoming_msg=request.form.get('Body').lower()  # type: ignore
    response=MessagingResponse()
    print(incoming_msg)
    message=response.message()
    responded=False
    words=incoming_msg.split('0')
    if "hello" in incoming_msg:
        reply="hello,how are u"
        

if __name__=="__main__":
    app.run(debug=True)