import requests

#remove https warning
requests.packages.urllib3.disable_warnings()

def post(target):
   payload_list={}
   payload_list['data']="Testing!"
   headers = {
            'content-type': "application/json",
            'Accept': "*/*",
        }
   response = requests.post(target, data=payload_list, headers=headers, verify=False)
   print (response)

#Input target
target = input("Target:")

post(target)
