from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def login(driver, email, password):
    """Войти в аккаунт."""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER))

def logout(driver):
    """Выход из аккаунта."""
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGOUT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGOUT_BUTTON))


