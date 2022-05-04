from seleniumwire import webdriver
import time
import random
from mimesis import Address
from mimesis.locales import Locale
from mimesis import Person
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
from scripts.getProxy import get_proxy
from scripts.getUserAgent import get_user_agent

from scripts.getEmail import generate_login

person = Person(Locale.DA)
address = Address(Locale.DA)
options = webdriver.ChromeOptions()
login, password, proxy, port = get_proxy()
proxy_option = {
    "proxy":{
        "https": f"https://{login}:{password}@{proxy}:{port}"
    }
}


agent = get_user_agent()

options.add_extension('anticaptcha-plugin_v0_52.xpi')
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

driver = webdriver.Chrome('chromedriver.exe', options=options, seleniumwire_options=proxy_option)

url = 'https://gaming.pringles.com/da_DK/Register'
phone = f'+45208{random.randint(10000, 99999)}'



if __name__ == '__main__':
    try:
        driver.get(url=url)
        time.sleep(4)
        action = ActionChains(driver)

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/section/main/div/section/div/div/div[2]/div[2]/div/form/div[2]/div[3]/div[6]/a/span')))
        pole = driver.find_element(By.XPATH, '/html/body/div[3]/section/main/div/section/div/div/div[2]/div[2]/div/form/div[2]/div[3]/div[6]/a/span')
        pole.location_once_scrolled_into_view
        print(12)
        time.sleep(3)
        action.move_to_element(pole).click().perform()
        print(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gigya-textbox-39065714942046050"]')))
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-39065714942046050"]')
        pole.location_once_scrolled_into_view
        time.sleep(2)
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-52636650089352940"]')
        pole.send_keys(person.first_name())
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-159831833930945280"]')
        action.move_to_element(pole).click().perform()
        pole.send_keys(person.surname())
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-32320507946185452"]')
        action.move_to_element(pole).click().perform()
        pole.send_keys(address.street_name())
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-51344355090310960"]')
        action.move_to_element(pole).click().perform()
        pole.send_keys(address.street_number())
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-88822848488352300"]')
        action.move_to_element(pole).click().perform()
        pole.send_keys(address.city())
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-39065714942046050"]')
        action.move_to_element(pole).click().perform()
        pole.send_keys(address.postal_code())
        #pole = driver.find_element(by=By.ID, value='Email')
        #pole.click()
        # pole.send_keys(EMAIL)
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-55761250888667520"]')
        action.move_to_element(pole).click().perform()
        pole.send_keys(phone)

        pole = driver.find_element(By.XPATH, '//*[@id="gigya-multiChoice-0-129645468760921980"]')

        action.move_to_element(pole).click().perform()
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-checkbox-124950540987203460"]')

        action.move_to_element(pole).click().perform()
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-checkbox-160298844928918820"]')
        action.move_to_element(pole).click().perform()


        login = generate_login()
        # email1
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-loginID-133415729987448180"]')
        pole.send_keys(login)
        # email2
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-19195255866927190"]')
        pole.send_keys(login)

        # password 1
        password = 'DjambulatLubitRamazana123!'
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-password-129521167110879820"]')
        pole.send_keys(password)

        # password 2
        password = 'DjambulatLubitRamazana123!'
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-password-2803893837206091"]')
        pole.send_keys(password)


        pole = driver.find_element(By.ID, 'gigya-multiChoice-0-129645468760921980')
        pole.location_once_scrolled_into_view
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'gigya-multiChoice-0-129645468760921980')))
        pole.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gigya-checkbox-124950540987203460"]')))
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-checkbox-124950540987203460"]')
        pole.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gigya-checkbox-160298844928918820"]')))
        pole = driver.find_element(By.XPATH, '//*[@id="gigya-checkbox-160298844928918820"]')
        pole.click()


        pole = driver.find_element(By.XPATH, '//*[@id="register-site-login"]/div[14]/input')
        pole.click()

        time.sleep(600)


    except Exception as er:
        print(er)
        time.sleep(100000)