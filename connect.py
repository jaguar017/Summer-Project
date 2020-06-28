from firebase import firebase
from twilio.rest import Client
firebase=firebase.FirebaseApplication("https://smart-parking-3d84f.firebaseio.com/",None)
result=firebase.get("Parking","Servo")
if(result=="open"):
    account_sid = 'AC75bcedbef35a8173c7d0e609502430ff'
    auth_token = '240451c4c9e950708c5bf8989b65f22a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body='''Parking lot is being accessed.''',
                            from_='+12058517496',
                              to='+917972746951'
                          )

    print(message.sid)


