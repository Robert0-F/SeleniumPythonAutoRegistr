import random
from random import choice
from string import ascii_letters

print(''.join(choice(ascii_letters) for i in range(12)) + str(random.randint(10, 9999)) + '@hosttomals.com')