import requests
import json
cookies = {
    'ASP.NET_SessionId': 'qk20pvsyfspdd2wdeu1eq4o0',
    'TMA%20-%20Doritos%20XBOX%20IWGDPR': 'accepted',
    '_ga': 'GA1.2.389761519.1665424919',
    '_gid': 'GA1.2.856775663.1665424919',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ASP.NET_SessionId=qk20pvsyfspdd2wdeu1eq4o0; TMA%20-%20Doritos%20XBOX%20IWGDPR=accepted; _ga=GA1.2.389761519.1665424919; _gid=GA1.2.856775663.1665424919',
    'Origin': 'https://www.doritosrockstarenergy.com',
    'Referer': 'https://www.doritosrockstarenergy.com/code-entry',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_data = {
    'memberId': 231968,
    'codes': [
        '123456789',
        '34526',
    ],
    'date': '',
    'tabCode': '',
    'codeType': 'DORITOS',
    'currentCulture': 'en',
}

response = requests.post('https://www.doritosrockstarenergy.com/WebMethods.aspx/EnterCodes',  headers=headers, json=json_data, verify = False)
print(response.json().get('d'))