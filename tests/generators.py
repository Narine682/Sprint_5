import random
import string
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from locators import *

URL = "https://stellarburgers.nomoreparties.site/"
def generate_email(name="narine"):
    cohort = "31"
    digits = random.randint(100, 999)
    return f"{name}_kazaryan_{cohort}_{digits}@ya.ru"
def generate_password(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))



def login(driver, email, password):
    driver.get(URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER))

def test_registration_and_login(driver):
    email = generate_email("Narine")
    password = generate_password(6)

    driver.get(URL + "register")
    driver.find_element(*NAME_INPUT).send_keys("Narine")
    driver.find_element(*EMAIL_INPUT).send_keys(email)
    driver.find_element(*PASSWORD_INPUT).send_keys(password)
    driver.find_element(*REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LOGIN_BUTTON))
    assert driver.find_element(*LOGIN_BUTTON).is_displayed()

    login(driver, email, password)
    assert driver.find_element(*ACCOUNT_HEADER).is_displayed()





