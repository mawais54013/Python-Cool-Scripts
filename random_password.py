import string
from random import *

def getRandomPassword():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(randint(8,16)))

    return password

print(getRandomPassword())
