import json, requests
headers = {'Referer': 'https://www.doritosrockstarenergy.com/registration',
           'Origin': 'https://www.doritosrockstarenergy.com',
           'Host': 'www.doritosrockstarenergy.com',
           'User-Agent': f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
           'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"'
}
def registration():
    data = {'BirthDate': "07/05/2001",
            'Email': f"killstreaker17gmail.com",
            'FirstName': f'Robert',
            'LastName': f'Xuilo',
            'PostalCode':f"77123",
            'SiteCode': "Microsite"}
    data = json.dumps(data)
    session = requests.Session()
    lnk = 'https://www.doritosrockstarenergy.com/WebMethods.aspx/Register'
    print(requests.post(lnk, verify = False))
registration()