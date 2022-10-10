import imaplib, json, requests, re, time
import quopri
from bs4 import BeautifulSoup




def check_all_emails(address, password):
    SMTP_SERVER = "imap.yandex.ru"
    SMTP_PORT = 993

    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(address, password)
    mail.select()
    try:
        print('start')
        print(address)
        print(password)
        time.sleep(2.5)
        data, ids = mail.search(None, '(UNSEEN)')
        print(ids[0].split())

        for id in ids[0].split():
            subject = (mail.fetch(id, '(RFC822)')[1][0][1].strip())
            b = quopri.decodestring(subject)
            b = b.decode('windows-1251')
            soup = BeautifulSoup(b, 'html.parser')
    except:
        return None

    try:
        print('start spam')
        print(address)
        print(password)
        time.sleep(2.5)
        mail.select('Spam')
        data, ids = mail.search(None, '(UNSEEN)')
        for id in ids[0].split():
            subject = (mail.fetch(id, '(RFC822)')[1][0][1].strip())
            b = quopri.decodestring(subject)
            b = b.decode('windows-1251')
            soup = BeautifulSoup(b, 'html.parser')
    except:
        return False




def read(address, password):
    SMTP_SERVER = "imap.yandex.ru"
    SMTP_PORT = 993
    massiv_strok = []
    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(address, password)
    mail.select()
    try:
        print('start')
        print(address)
        print(password)
        time.sleep(2.5)
        data, ids = mail.search(None, '(UNSEEN)')
        for id in ids[0].split():

            subject = (mail.fetch(id, '(RFC822)')[1][0][1].strip())
            soup = BeautifulSoup(subject, 'html.parser')
            soup = soup.decode('utf-8')

            massiv_strok.append(soup.split('\n'))

        real_massiv = str(massiv_strok[0]).split(',')

        code = real_massiv[99]
        code.replace(' ', '')
        print(code)
        newCode = ''
        for i in code:
            if i.isdigit():
                newCode += str(i)
        print(newCode)
        return newCode

    except:
        return False





        # except:
        # return False
    #
    # def check_block(address, password):
    #     SMTP_SERVER = "outlook.office365.com"
    #     SMTP_PORT = 993
    #
    #     mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    #     try:
    #         mail.login(address, password)
    #         mail.select()
    #         try:
    #             data, ids = mail.search(None, '(UNSEEN)')
    #             for _ in ids:
    #                 for id in ids[0].split():
    #                     (mail.fetch(id, '(RFC822)')[1][0][1].strip())
    #         except:
    #             pass
    #     except Exception as ex:
    #         message = str(ex).split('.')
    #         message = message[0].replace('b', '')
    #         message = message.replace("'", '')
    #         if message.lower() == "authentication failed":
    #             return 'blocked'
    #     else:
    #         return 'active'
    #
    #
    #
def read_auth(address, password):
    SMTP_SERVER = "outlook.office365.com"
    SMTP_PORT = 993

    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(address, password)
    mail.select()
    try:
        print('start')
        print(address)
        print(password)
        time.sleep(2.5)
        data, ids = mail.search(None, '(UNSEEN)')
        for id in ids[0].split():
            subject = (mail.fetch(id, '(RFC822)')[1][0][1].strip())
            soup = BeautifulSoup(subject, 'html.parser')
            soup = soup.decode('utf-8')
            massiv_strok = soup.split('\n')
            for i in range(0, len(massiv_strok)):
                if 'Please use the following code to access your account.' in massiv_strok[i]:
                    code = massiv_strok[i + 2]
                    return code
    except:
        return False