from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from config import BASE_URL
import pytest
from helpers import login

class TestConstructor:


    def test_go_to_account(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*ACCOUNT_HEADER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_BUTTON))
        assert driver.find_element(*LOGIN_BUTTON).is_displayed()

    def test_personal_account(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*ACCOUNT_HEADER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_BUTTON))
        assert driver.find_element(*ACCOUNT_HEADER).is_displayed()


    def test_registretion_account(self, driver,user_data):
        driver.get(BASE_URL)
        driver.find_element(*REGISTER_BUTTON).click()
        driver.find_element(*NAME_INPUT).send_keys(user_data["name"])
        driver.find_element(*EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(user_data["password"])
        WebDriverWait(driver, 10).until((EC.visibility_of_element_located(ACCOUNT_HEADER)))
        assert driver.find_element(*ACCOUNT_HEADER).is_displayed()


    def test_login_from_recovery_from(self, driver, user_data):
        driver.get(BASE_URL + "forgot-password")
        driver.find_element(By.XPATH, '//*[text()="Войти"]').click()
        login(driver, user_data["email"], user_data["password"])
        assert driver.find_element(*ACCOUNT_HEADER).is_displayed()


    def test_login(self, driver, email, password):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ACCOUNT_HEADER))



    def test_go_to_constructor_from_logo(self, driver, user_data):
        driver.get(BASE_URL)
        login(driver, user_data["email"], user_data["password"])
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(ACCOUNT_HEADER)).click()
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(LOGOUT_BUTTON))
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()
        assert  driver.find_element(*INGREDIENT_CARD).is_displayed()


    def test_logout(self, driver, user_data):
        driver.get(BASE_URL)
        login(driver, user_data["email"], user_data["password"])
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(ACCOUNT_HEADER)).click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LOGOUT_BUTTON)).click()
        WebDriverWait(driver, 15).until((EC.visibility_of_element_located(LOGIN_BUTTON)))
        assert driver.find_element(*LOGIN_BUTTON).is_displayed()

    def test_go_to_buns(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(BUNS_TAB)).click()
        active_tab = driver.find_element(*BUNS_TAB).get_attribute("class")
        assert "current" in active_tab

    def test_go_to_sauces(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SAUCES_TAB)).click()
        active_tab = driver.find_element(*SAUCES_TAB).get_attribute("class")
        assert "current" in active_tab

    def test_go_to_fillings(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(FILLINGS_TAB)).click()
        active_tab = driver.find_element(*FILLINGS_TAB).get_attribute("class")
        assert "current" in active_tab

































