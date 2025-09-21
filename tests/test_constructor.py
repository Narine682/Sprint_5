from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from locators import *

URL = "https://stellarburgers.nomoreparties.site/"

def login(driver, email, password):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER))

def test_go_to_account(driver):
    driver.get(URL)
    driver.find_element(*ACCOUNT_HEADER).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_BUTTON))
    assert driver.find_element(*LOGIN_BUTTON).is_displayed()

def test_go_to_constructor_from_account(driver):
     driver.get(URL)
     login(driver, "Твоя почта", "Твой пароль")
     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER)).click()
     WebDriverWait(driver, 10).until((EC.visibility_of_element_located(LOGIN_BUTTON)))
     driver.find_element(*CONSTRUCTOR_LINK).click()
     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(INGREDIENT_CARD))
     assert driver.find_element(*INGREDIENT_CARD).is_displayed()

def test_go_to_constructor_from_logo(driver):
     driver.get(URL)
     login(driver, "Твоя почта", "Твой пароль")
     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER)).click()
     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGOUT_BUTTON))
     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGOUT_BUTTON))
     driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
     assert  driver.find_element(*INGREDIENT_CARD).is_displayed()

def test_logout(driver):
     driver.get(URL)
     login(driver, "Твоя почта", "Твой пароль")
     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER)).click()
     WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGOUT_BUTTON)).click()
     WebDriverWait(driver, 10).until((EC.visibility_of_element_located(LOGIN_BUTTON)))
     assert driver.find_element(*LOGIN_BUTTON).is_displayed()

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
       WebDriverWait(driver, 10).until(EC.element_to_be_clickable(FILLINGS_TAB)).click()
       active_tab = driver.find_element(*FILLINGS_TAB).get_attribute("class")
       assert "current" in active_tab

























