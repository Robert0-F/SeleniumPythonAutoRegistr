import random


def generate_login():
    set_of_letters = 'abcdefghijklmnopqrstuvwxyz123456789'
    setik = []
    for i in range(0, random.randint(7, 10)):
        setik.append(random.choice(set_of_letters))
    login = ''.join(setik)
    login += '@labelpap.com'
    return login

