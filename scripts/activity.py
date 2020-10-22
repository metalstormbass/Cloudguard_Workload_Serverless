import requests

#remove https warning
requests.packages.urllib3.disable_warnings()

def post(target):

   headers = {
            'content-type': "application/json",
            'Accept': "*/*",
        }
   response = requests.post(target, data={'data' : user_input, 'command' : user_command },verify=False)
   print (response)

#Input target
target = input("Target: ")
user_input = input("Enter your message here: ")
user_command = input("Enter your test command here: ")
post(target)
