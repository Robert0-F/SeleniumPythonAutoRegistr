import requests
import urllib3
import json
urllib3.disable_warnings()
cookies = {
    'ASP.NET_SessionId': 'qk20pvsyfspdd2wdeu1eq4o0',
    'TMA%20-%20Doritos%20XBOX%20IWGDPR': 'accepted',
    '_ga': 'GA1.2.389761519.1665424919',
    '_gid': 'GA1.2.856775663.1665424919',
    '_gat_UA-11401921-227': '1',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'ASP.NET_SessionId=qk20pvsyfspdd2wdeu1eq4o0; TMA%20-%20Doritos%20XBOX%20IWGDPR=accepted; _ga=GA1.2.389761519.1665424919; _gid=GA1.2.856775663.1665424919; _gat_UA-11401921-227=1',
    'Origin': 'https://www.doritosrockstarenergy.com',
    'Referer': 'https://www.doritosrockstarenergy.com/registration',
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
    'member': {
        'BirthDate': '07/05/2001',
        'Country': None,
        'Email': 'dfisdfklj@gmail.com',
        'FirstName': 'Robert',
        'Gender': None,
        'LastName': 'Xyulo',
        'Misc5': None,
        'Misc7': None,
        'Misc8': None,
        'Misc9': None,
        'Misc10': None,
        'Misc11': None,
        'Misc12': None,
        'Misc13': None,
        'Misc14': None,
        'Misc15': None,
        'Num1': None,
        'Num2': None,
        'Num3': None,
        'Num4': None,
        'Num5': None,
        'Optin1': False,
        'Optin2': True,
        'Optin3': True,
        'Optin4': None,
        'Optin5': None,
        'Optin6': None,
        'Optin7': None,
        'Optin8': None,
        'Optin9': None,
        'Optin10': None,
        'PostalCode': '77123',
        'SiteCode': 'Microsite',
        'Username': None,
        'country': 'USA',
    },
    'code': '',
    'fbUserID': '',
    'signedRequest': '',
    'twitterId': '',
    'googleId': '',
    'emailConfirm': 'dfisdfklj@gmail.com',
    'shareClickGuid': None,
    'date': '',
    'response': '03AIIukzjEtoRSJLBELOfxqAQMr3RlL1O3qz244EuQvMCKfPA-_PI-cimTtb-jl8W83CM3Ex14FF6vfiUqMHNRaAziH4vrD2Nhcwju0RmgCA5YilwHmTVgm7USy8NUTRelW3UUIaCxat0Ofj87cZKG7mOZVZhKFUG39ZZ_n1G2uclMOKte97rJ3990ip4tNEvCD_5OxCiJWh68HQ_dCQVsT8zChh30icGUL99tP_s8jQ-eSH6VmVHl6cpcjT9gHe0vAdvg-VzNaJTcmLz-UMErwjrBUf8To0rPF2nF0Ul0wx8C8LzwCBCC2123gZVY-9uTKjRanuO8NOmUtyDJYg7CTRAU4QfhZ6Bl4Gd2hWBTYhiOCsDIDj9uAFr2mWvMA7x_WDmDW-BA3QJtOv7nuBoHbKVB0JNqqRBvW_qN87rH0-UgW0Xvm8ZtF3N5nLu2OEtftDifkqLm15e2LCM0N4Mxvh7nUsyjOLRV4MzlhPo_F50p3h4oerEKyY5B5jwzGEsHmFV0HZOer6U6akX9muqgO9WM0N7BdKaPFqBqAPjstL3f60R4-cx1AmSn3GiRPneLptOpDGnvHORXunKkDxBwzs-wsXgro1qldRLM08DlEwLXrIwjKWwfAaDRx-j3mGV0Ip92sibux5as6An-2gB_k3g2EmVJGmdrEgmccwpQQCB638oJv5Bu2gJj9Lu4e28-E2xd-hOSPqppU7amD7FmcbcpsAlxXYGYWnphx8_ptgESiHTUb8_03JX48_3xawyLoDuqPXd6Qda_Fzw0xEyJzBwIW_vmnR7BC9ci0hz_EY3BlIE57CkrCL-79SzS9StEeT07WBgB2J1OG_eCDo89l2FVeBA0JCVh3zt9tNgQL4l3gRi0fzkXQJaWFxZlBWjN9sp2CGSVCQrj9gOyY817l57fU2QuIUydmJokmc9oWLvjEg7r7t9NXr5WH-WeD2dhV3WrwEaYOvrVnyuf9x198ZwIlGPCw_CR2o-7KVl1fIsB7N5DVh31zHAYDRcFTNdaFNInNJjKte-FppZgHSTGrChZyo3A7W9seL9zi8C2H1C-9g3M8Cw-7S4ovBNPqKCKIiV2Z0rkukG4ofvC35SV0MiE2T803xa_IzqpHAmtddQhMIr_D9ouStpAItupeUHoaE7F0Tuv--jtgNMpUlXrl153ohoEvDWPQsN2Zi2efoxTUXwphfR4F20MCBoDNdQxfnR0Wu0r--eMszvxnmRrNPfnpT87C0gSeIT68ciYj_wfAW5vBBwPsK7FD0kQTKsiDIvFhSMnYOoVcsP45qeqVAE-9ELrsTte7w',
    'currentCulture': 'en',
}

response = requests.post('https://www.doritosrockstarenergy.com/WebMethods.aspx/Register', headers=headers, json=json_data, verify=False)
print((json.loads(response.json().get('d'))).get('errors'))