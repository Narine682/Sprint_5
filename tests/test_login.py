import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

EMAIL =" Narine_kazaryan_31_@yandex.ru"
PASSWORD = "7121980"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)).send_keys(EMAIL)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER))

def test_login_from_main_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*LOGIN_BUTTON).click()
    login(driver)
    assert 'Личный кабинет' in driver.find_element(*ACCOUNT_HEADER).text

def test_login_from_profile_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*ACCOUNT_HEADER).click()
    login(driver)
    assert 'Личный кабинет' in driver.find_element(ACCOUNT_HEADER).text

def test_login_from_registration_from(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*LOGIN_BUTTON).click()
    login(driver)
    assert 'Личный кабинет' in driver.find_element(*ACCOUNT_HEADER).text

def test_login_from_recovery_from(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*LOGIN_BUTTON).click()
    login(driver)
    assert 'Личный кабинет' in driver.find_element(*ACCOUNT_HEADER).text

