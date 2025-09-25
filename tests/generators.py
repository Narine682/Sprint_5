import random
import string


URL = "https://stellarburgers.nomoreparties.site/"
def generate_email():
    return f"Narine_kazaryan_31_{random.randint(100,999)}@yandex.ru"

def generate_password(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_name():
    return "Test User"
print(generate_email())
print(generate_password())
print(generate_name())






