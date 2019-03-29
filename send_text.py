from twilio.rest import Client
import config

account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)

def send_text():  
    response = client.messages.create(
        to= "+919344488146", #https://www.twilio.com/console/phone-numbers/verified
        from_= "+19197693667", #+15005550006 will be used for trial account.
        body= "Fine Amount is : 200 rupees" # if you need to attach multimedia to your message, else remove this parameter.
        )
 