from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import *
from generators import generate_email, generate_password, generate_name
URL = "https://stellarburgers.nomoreparties.site/"


# Кнопка "Войти в аккаунт" на главной
def test_go_to_account(driver):
    driver.get(URL)
    driver.find_element(*ACCOUNT_HEADER).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_BUTTON))
    assert driver.find_element(*LOGIN_BUTTON).is_displayed()

# Кнопка "Личный кабинет"
def test_personal_account(driver):
    driver.get(URL)
    driver.find_element(*ACCOUNT_HEADER).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_BUTTON))
    driver.find_element(*ACCOUNT_HEADER).click()
    assert driver.find_element(*ACCOUNT_HEADER).is_displayed()



# Кнопка в форме регистрации
def test_registretion_account(driver):
    driver.get(URL)
    driver.find_element(*REGISTER_BUTTON).click()
    driver.find_element(*NAME_INPUT).send_keys(user_data["name"])
    driver.find_element(*EMAIL_INPUT).send_keys(user_date["email"])
    driver.find_element(*PASSWORD_INPUT).send_keys(user_data["password"])
    WebDriverWait(driver, 10).until((EC.visibility_of_element_located(ACCOUNT_HEADER)))
    assert driver.find_element(*ACCOUNT_HEADER).is_displayed()



#Восстановления пароля
def test_login_from_recovery_from(driver, user_data):
    driver.get(URL + "forgot-password")
    driver.find_element(By.XPATH, '//*[text()="Войти"]').click()
    login(driver, user_data["email"], user_data["password"])
    assert driver.find_element(*ACCOUNT_HEADER).is_displayed()

# Переход в личный кабинет
def login(driver, email, password):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER))




#Переход из личного кабинета в конструктор
def test_go_to_constructor_from_logo(driver, user_data):
     driver.get(URL)
     login(driver, user_data["email"], user_data["password"])
     WebDriverWait(driver,10).until(EC.visibility_of_element_located(ACCOUNT_HEADER)).click()
     WebDriverWait(driver,10).until(EC.visibility_of_element_located(LOGOUT_BUTTON))
     WebDriverWait(driver,10).until(EC.visibility_of_element_located(LOGOUT_BUTTON))
     driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
     assert  driver.find_element(*INGREDIENT_CARD).is_displayed()

#Выход из аккаунта
def test_logout(driver, user_data):
     driver.get(URL)
     login(driver, user_data["email"], user_data["password"])
     WebDriverWait(driver, 15).until(EC.visibility_of_element_located(ACCOUNT_HEADER)).click()
     WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LOGOUT_BUTTON)).click()
     WebDriverWait(driver, 15).until((EC.visibility_of_element_located(LOGIN_BUTTON)))
     assert driver.find_element(*LOGIN_BUTTON).is_displayed()
#Раздел Конструктор
def test_go_to_buns(driver):
      driver.get(URL)
      WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUNS_TAB)).click()
      active_tab = driver.find_element(*BUNS_TAB).get_attribute("class")
      assert "current" in active_tab

def test_go_to_sauces(driver):
       driver.get(URL)
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SAUCES_TAB)).click()
       active_tab = driver.find_element(*SAUCES_TAB).get_attribute("class")
       assert "current" in active_tab

def test_go_to_fillings(driver):
       driver.get(URL)
       WebDriverWait(driver,10).until(EC.element_to_be_clickable(FILLINGS_TAB)).click()
       active_tab = driver.find_element(*FILLINGS_TAB).get_attribute("class")
       assert "current" in active_tab






A




























