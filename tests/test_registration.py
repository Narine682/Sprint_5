from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from config import BASE_URL


def test_registration_success(driver, user_data):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)

    wait.until(EC.visibility_of_element_located(NAME_INPUT)).send_keys(user_data["name"])
    driver.find_element(*NAME_INPUT).send_keys(user_data["email"])
    driver.find_element(*PASSWORD_INPUT).send_keys(user_data["password"])
    driver.find_element(*REGISTER_BUTTON).click()

    account_element = wait.until(EC.visibility_of_element_located(ACCOUNT_HEADER))
    assert 'Личный Кабинет' in account_element.text


def test_registration_short_password(driver, user_data):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver,10)
    driver.get(BASE_URL)

    wait.until(EC.visibility_of_element_located(NAME_INPUT)).send_keys(user_data["name"])
    driver.find_element(*NAME_INPUT).send_keys(user_data["email"])
    driver.find_element(*PASSWORD_INPUT).send_keys("123")
    driver.find_element(*REGISTER_BUTTON).click()

    error_text = wait.until(EC.visibility_of_element_located(REGISTER_ERROR)).text
    assert "пароль" in error_text.lower()


