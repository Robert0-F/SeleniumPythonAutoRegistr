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


options = webdriver.ChromeOptions()

# login, password, proxy, port = get_proxy()
#
# proxy_option = {
#     "proxy":{
#         "https": f"https://{login}:{password}@{proxy}:{port}"
#     }
# }
clintKeyAntiCaptcha = '51eae633b6157688e92d4d2e2ea23468'

agent = get_user_agent()
options.add_argument('--disable-notifications')
options.add_argument('disable-infobars')
options.add_argument("--lang=en-US")
options.add_argument('--disable-default-apps')
options.add_argument(f'user-agent={agent}')
options.add_argument("--start-maximized")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome('chromedriver.exe', options=options)
headers = {'Referer': 'https://www.doritosrockstarenergy.com/registration',
           'Origin': 'https://www.doritosrockstarenergy.com',
           'Host': 'www.doritosrockstarenergy.com',
           'User-Agent': f'{get_user_agent()}',
           'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"'
}

def generateEmail():
    return ''.join(choice(ascii_letters) for i in range(12)) + str(random.randint(10, 9999)) + '@hosttomals.com'


def getName():
    person = Person(Locale.EN)
    return person.first_name(), person.surname()


def zipCod():
    return random.randint(12345, 99999)

def get_codes(upc, front):
    link = 'https://www.doritosrockstarenergy.com/WebMethods.aspx/EnterCodes'
    for i in range(upc, 99999):
        for j in range(front, 999999999):
            pass

def registration():

    session = requests.Session()
    lnk = 'https://www.doritosrockstarenergy.com/WebMethods.aspx/Register'
    print(session.post(lnk))


def captha_solve():
    session = requests.Session()
    i = 0
    while i < 1:
        raw = {
            "clientKey": "51eae633b6157688e92d4d2e2ea23468",
            "task":
                {
                    "type": "NoCaptchaTaskProxyless",
                    "websiteURL": "https://www.doritosrockstarenergy.com",
                    "websiteKey": "6LcfduIUAAAAAMF1tuZ9r3qWvNfFF5YZrA9Edp0o"
                },
           "softId": "909"
        }

        t = session.post('https://api.anti-captcha.com/createTask', data=json.dumps(raw))
        taskId = json.loads(t.content)
        taskId = taskId['taskId']
        raw_captha = {
            "clientKey": "c52ad7803c2b236945e99d31fe941f6d",
            "taskId": taskId
        }
        attemps = 0

        while True:
            attemps += 1
            s = session.post('https://api.anti-captcha.com/getTaskResult', data=json.dumps(raw_captha))
            status = json.loads(s.content)
            status_check = status['status']
            if status_check == 'ready':
                respone_captha = status['solution']['gRecaptchaResponse']
                i += 1
                return respone_captha
            if attemps > 14:
                break



















# if __name__ == '__main__':
#     try:
#         driver.get(url=url)
#         time.sleep(4)
#         action = ActionChains(driver)
#
#         WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/section/main/div/section/div/div/div[2]/div[2]/div/form/div[2]/div[3]/div[6]/a/span')))
#         pole = driver.find_element(By.XPATH, '/html/body/div[3]/section/main/div/section/div/div/div[2]/div[2]/div/form/div[2]/div[3]/div[6]/a/span')
#         pole.location_once_scrolled_into_view
#         print(12)
#         time.sleep(3)
#         action.move_to_element(pole).click().perform()
#         print(1)
#         WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gigya-textbox-39065714942046050"]')))
#         pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-39065714942046050"]')
#         pole.location_once_scrolled_into_view
#         time.sleep(2)
#         pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-52636650089352940"]')
#         pole.send_keys(person.first_name())
#
#
#         # password 1
#         password = 'DjambulatLubitRamazana123!'
#         pole = driver.find_element(By.XPATH, '//*[@id="gigya-password-129521167110879820"]')
#         pole.send_keys(password)
#
#         # password 2
#         pole = driver.find_element(By.XPATH, '//*[@id="gigya-password-2803893837206091"]')
#         pole.send_keys(password)
#
#
#         pole = driver.find_element(By.ID, 'gigya-multiChoice-0-129645468760921980')
#         pole.location_once_scrolled_into_view
#         WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'gigya-multiChoice-0-129645468760921980')))
#         pole.click()
#
#         WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gigya-checkbox-124950540987203460"]')))
#         pole = driver.find_element(By.XPATH, '//*[@id="gigya-checkbox-124950540987203460"]')
#         pole.click()
#
#         email = 'kitten@labelpap.com'
#         password = 'Kiril123!'
#         check_all_emails(email, password)
#
#
#
#
#         pole = driver.find_element(By.XPATH, '//*[@id="register-site-login"]/div[14]/input')
#         pole.click()
#
#
#         code = False
#         attemps = 0
#         while not code:
#             print(attemps)
#             attemps += 1
#             code = read(email, password)
#             print(code)
#             if code:
#                 break
#             else:
#                 time.sleep(5)
#             if attemps >= 20:
#                 break
#
#
#         time.sleep(10000)
#
#
#
#
#     except Exception as er:
#         print(er)
#         time.sleep(100000)