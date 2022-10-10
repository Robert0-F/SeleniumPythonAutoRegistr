from seleniumwire import webdriver
import time
import random
from mimesis import Address
from mimesis.locales import Locale
from mimesis import Person
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import names
from selenium.webdriver.common.by import By
from scripts.getProxy import get_proxy
from scripts.getUserAgent import get_user_agent
from scripts.emailApi import check_all_emails, read
from scripts.getEmail import generate_login

person = Person(Locale.DA)
address = Address(Locale.DA)
options = webdriver.ChromeOptions()

# login, password, proxy, port = get_proxy()
#
# proxy_option = {
#     "proxy":{
#         "https": f"https://{login}:{password}@{proxy}:{port}"
#     }
# }


agent = get_user_agent()
print('aye')
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

driver = webdriver.Chrome('chromedriver.exe', options=options)
#driver = webdriver.Chrome('chromedriver.exe', options=options, seleniumwire_options=proxy_option)


phone = f'+45208{random.randint(10000, 99999)}'



if __name__ == '__main__':
    try:

        url = 'https://accounts.nintendo.com/register?post_register_redirect_uri=https%3A%2F%2Faccounts.nintendo.com'
        driver.get(url=url)
        time.sleep(4)
        action = ActionChains(driver)



        #Nickname
        Nik = generate_login()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,  '/html/body/div[1]/main/div/section[2]/form/div[1]/input')))
        pole = driver.find_element(By.XPATH,  '/html/body/div[1]/main/div/section[2]/form/div[1]/input')
        pole.send_keys(Nik)

        #email
        email = Nik + str(random.randint(100, 999)) + '@labelpap.com'
        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section[2]/form/div[2]/input')
        action.move_to_element(pole)
        pole.send_keys(email)

        #password1

        password = 'LeonidPidoras1!'
        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section[2]/form/div[3]/div[1]/input')
        pole.send_keys(password)
        action.move_to_element(pole)
        #password2
        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section[2]/form/div[4]/div[1]/input')
        pole.send_keys(password)



        #year
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/section[2]/form/div[5]/div/div[1]/div[1]/select')))
        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section[2]/form/div[5]/div/div[1]/div[1]/select')
        pole.send_keys(random.randint(1980,2000))
        action.move_to_element(pole).perform()
        #month

        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section[2]/form/div[5]/div/div[1]/div[2]/select')
        pole.send_keys(random.randint(1, 12))

        #day

        pole = driver.find_element(By.XPATH,  '/html/body/div[1]/main/div/section[2]/form/div[5]/div/div[1]/div[3]/select')
        pole.send_keys(random.randint(1, 28))

        #Gender

        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section[2]/form/div[6]/div[1]/select')
        pole.location_once_scrolled_into_view
        action.move_to_element(pole).perform()
        pole.send_keys('Male')


        #click

        driver.execute_script("document.getElementById('form-terms_consented').click();")
        time.sleep(2)



        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/section[2]/form/div[11]/button')
        pole.click()


        time.sleep(3)
        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/form/div[1]/div[2]/label/div')
        pole.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[2]/form/div[3]/button')))
        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/form/div[3]/button')
        pole.click()


        #code
        code = ''
        pole = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/form[1]/div[1]/input')
        pole.send_keys(code)

        time.sleep(322222)



        '''EPIC GAMES'''
        url = 'https://www.epicgames.com/id/register'
        driver.get(url=url)
        time.sleep(4)
        action = ActionChains(driver)



        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-with-epic"]')))
        pole = driver.find_element(By.XPATH, '//*[@id="login-with-epic"]')
        action.move_to_element(pole).click().perform()


        #name
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div[1]/div/input')))
        rand_name = names.get_first_name(gender='male')
        pole = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div[1]/div/input')
        pole.send_keys(rand_name)


        #surname
        rand_surname = names.get_last_name()
        pole = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[2]/div[2]/div/input')
        pole.send_keys(rand_surname)


        #login
        login = generate_login()
        pole = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[3]/div/input')
        pole.send_keys(login)


        #email
        email = login + str(random.randint(100, 999)) + '@labelpap.com'
        pole = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[4]/div/input')
        pole.send_keys(email)


        #pass

        pole = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[5]/div/input')
        password = 'LeonidPidoras12!'
        pole.send_keys(password)
        print(31)

        #radio
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/label[2]/span[1]/span')))
        pole = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/label[2]/span[1]/span')
        action.move_to_element(pole).click().perform()

        print(32)


        #contin
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[7]/button')))
        pole = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/form/div[7]/button')
        action.move_to_element(pole).click().perform()

        time.sleep(10000)













        # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gigya-textbox-39065714942046050"]')))
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-39065714942046050"]')
        # pole.location_once_scrolled_into_view
        # time.sleep(2)
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-52636650089352940"]')
        # pole.send_keys(person.first_name())
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-159831833930945280"]')
        # action.move_to_element(pole).click().perform()
        # pole.send_keys(person.surname())
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-32320507946185452"]')
        # action.move_to_element(pole).click().perform()
        # pole.send_keys(address.street_name())
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-51344355090310960"]')
        # action.move_to_element(pole).click().perform()
        # pole.send_keys(address.street_number())
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-88822848488352300"]')
        # action.move_to_element(pole).click().perform()
        # pole.send_keys(address.city())
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-39065714942046050"]')
        # action.move_to_element(pole).click().perform()
        # pole.send_keys(address.postal_code())
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-55761250888667520"]')
        # action.move_to_element(pole).click().perform()
        # pole.send_keys(phone)
        #
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-multiChoice-0-129645468760921980"]')
        #
        # action.move_to_element(pole).click().perform()
        #
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-checkbox-160298844928918820"]')
        # action.move_to_element(pole).click().perform()
        #
        #
        # login = generate_login()
        # # email1
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-loginID-133415729987448180"]')
        # pole.send_keys(login)
        # # email2
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-19195255866927190"]')
        # pole.send_keys(login)
        #
        # # password 1
        # password = 'DjambulatLubitRamazana123!'
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-password-129521167110879820"]')
        # pole.send_keys(password)
        #
        # # password 2
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-password-2803893837206091"]')
        # pole.send_keys(password)
        #
        #
        # pole = driver.find_element(By.ID, 'gigya-multiChoice-0-129645468760921980')
        # pole.location_once_scrolled_into_view
        # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'gigya-multiChoice-0-129645468760921980')))
        # pole.click()
        #
        # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gigya-checkbox-124950540987203460"]')))
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-checkbox-124950540987203460"]')
        # pole.click()
        #
        # email = 'kitten@labelpap.com'
        # password = 'Kiril123!'
        # check_all_emails(email, password)
        #
        #
        #
        #
        # pole = driver.find_element(By.XPATH, '//*[@id="register-site-login"]/div[14]/input')
        # pole.click()
        #
        #
        # code = False
        # attemps = 0
        # while not code:
        #     print(attemps)
        #     attemps += 1
        #     code = read(email, password)
        #     print(code)
        #     if code:
        #         break
        #     else:
        #         time.sleep(5)
        #     if attemps >= 20:
        #         break
        #
        # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gigya-textbox-code"]')))
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-textbox-code"]')
        # pole.send_keys(code)
        #
        # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="gigya-otp-update-form"]/div[3]/div[1]/input')))
        # pole = driver.find_element(By.XPATH, '//*[@id="gigya-otp-update-form"]/div[3]/div[1]/input')
        # pole.click()
        # time.sleep(10000)
        #
        #
        # '/html/body/div[3]/section/main/div/section/div/div[1]/div/div/form/div[1]/div/div[2]/input'



    except Exception as er:
        print(er)
        time.sleep(100000)
