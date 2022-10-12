from seleniumwire import webdriver
import time
import random

from random import choice
from string import ascii_letters

from mimesis.locales import Locale
from mimesis import Person
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from scripts.getProxy import get_proxy
from scripts.getUserAgent import get_user_agent
from scripts.emailApi import check_all_emails, read
from scripts.getEmail import generate_login
import requests
import json
import urllib3
import json
urllib3.disable_warnings()
import warnings
from urllib3.exceptions import InsecureRequestWarning
import contextlib
old_merge_environment_settings = requests.Session.merge_environment_settings

@contextlib.contextmanager
def no_ssl_verification():
    opened_adapters = set()

    def merge_environment_settings(self, url, proxies, stream, verify, cert):
        # Verification happens only once per connection so we need to close
        # all the opened adapters once we're done. Otherwise, the effects of
        # verify=False persist beyond the end of this context manager.
        opened_adapters.add(self.get_adapter(url))

        settings = old_merge_environment_settings(self, url, proxies, stream, verify, cert)
        settings['verify'] = False

        return settings

    requests.Session.merge_environment_settings = merge_environment_settings

    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', InsecureRequestWarning)
            yield
    finally:
        requests.Session.merge_environment_settings = old_merge_environment_settings

        for adapter in opened_adapters:
            try:
                adapter.close()
            except:
                pass




def try_code(upc, front, member_id):
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
        # 'Cookie': 'ASP.NET_SessionId=qk20pvsyfspdd2wdeu1eq4o0; TMA%20-%20Doritos%20XBOX%20IWGDPR=accepted; _ga=GA1.2.389761519.1665424919; _gid=GA1.2.856775663.1665424919; _gat_UA-11401921-227=1',
        'HeaderToken': '',
        'Origin': 'https://www.doritosrockstarenergy.com',
        'Referer': 'https://www.doritosrockstarenergy.com/code-entry',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': f'{get_user_agent()}',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'memberId': f'{member_id}',
        'codes': [
            f'{front}',
            f'{upc}',
        ],
        'date': '',
        'tabCode': '',
        'codeType': 'DORITOS',
        'response': '03AIIukziGzmfk5-jMxHXZS0qTXVkebH0B8DKKzJ2-YWe9tremi8OxVA1WloBoc42MiUvHGv7WS1lO7-MYdFRJnLCrX7KoesyUzP4zQqia1dbP51zQ97SRUN9ff6k6la6wRuNdrOE65IdvI9THDmnYS158rJxy8UpBD8rPxn8peq530tQS78voTceDm4KUvba_Vvw4uJeUeeS-LYhRYWu9BoP1vQbEFBJ6VpKa7lZx9qOc1YPzCEli_60cxt6ZE8LhZpOkMgw7CrWitfr72B0QPiFonnScqyrVFTLCvfQo2MaXvkuO-FdUIwT4Fm7Dd-LH_NwD2EcegluVnzBYzHUosf2IZk4rm5ePpHIJosJSDukt0SCDLRfKbUwGO3YAPSHZVCF0KcW1wUqsXJ6uDfIaUpxaZMwArZT84k14YdfkthXJqO5416vTwNkaIfhyHDPfkB-VZ-SfALFqiAr63yqVZSXytGoyXSMmY44Pv-D8vnzZLXLhMd0zeFFMAOos1UZKapnKxpK_JU7sppPo2A_p6ldlGqK3T20OZCzSjuxG--ZUusBhV3nCltgJzvNNQWzDXuMcD8Be2uiGw_umd7LGJU2S06geU5-uigcnNzf1ka5PD1_w57miqbIFZ_ohHlOmXSGiX3kC0qhSDMyfmu5AvJqBj4JB7EABNC5wUkGBk9fQNqwkK4CQ_FQDha3VWPgiTLV1HimBhspw5o7VUf-WrIBCdJvepaydCOf1SGTTKFOWCBZvkWdlTr5WKG1RCCoGAMNPEX67FQqcVeKcshE48iMbe2--pUBtwEjya3-YkJ4sTLWOiWFU26tKjNicwyFtlXxmMdzfpPNrqBqXPzAJoTxEeOY5X2NGd2yd1bb4AQyQr21984MgHcKypg4iyiuBOrG2LSWYQwi_zbzzHeiGFHiHENO6uPqmkxvNThxKiZmkKIjqaCagvZsTJxYIOLZXC9heShKZfVrxcoKRfw-ruQLr_hPpT_d56ZST3sVgrhTPPLpiOZbVLFXjr5CCYll9m44S5XO9PfbuVA6OGsVTJBZ44mwZZBZ0V7IOEt4h_fMqwOQ-zx_HW3jKgVYhjHrZzG_SXbvh-2Vls_iR34Xk4O0M_SaCtWspdyhtTDVUXn71IdCQhJCWLkCFdiO28mVIcknWARGxvZ3hq6zHApCgK46jzi89Y5GNH3RBNkmpyVGKtYWtZnglFKHh3l2WXS1yZx2YmGucxSGXhwF3TTvdhB3LMawW4v-g1x73LgPfn5MCK9fyIpuH15jpigmgmFULU8ubcvzihMxLHwQc3Agb_31qdt36yg1WoA',
        'currentCulture': 'en',
    }
    with no_ssl_verification():
        response = json.dumps((requests.post('https://www.doritosrockstarenergy.com/WebMethods.aspx/EnterCodes', headers=headers,
                             json=json_data, cookies=cookies).json()))
    print(response)
    if(response.find("Please check if you have verified yourself with reCAPTCHA") >=1):
        print('Капча йобаная')
    elif(response.find("Front of Bag Code is Invalid") >=1):
        print('Код неправильный')
    elif(response.find('There was an error processing the request.') >= 1):
        print('Что то не так')
        ЗАЕБАЛСЯ Я С ЕБАНЫМ "Please check if you have verified yourself with reCAPTCHA"
try_code(34526, 532547431, 297132)