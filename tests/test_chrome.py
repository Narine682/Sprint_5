from selenium import webdriver
from selenium.webdriver.chrome.service import Service

CHROMEDRIVER_PATH = "C:\\Users\\Artar\\PycharmProjects\\Sprint_5\\WebDriver\\bin\\chromedriver.exe"
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service)

print("Chrome подключен, заголовок страницы:", driver.title)
driver.quit()
driver.get("https://www.google.com")
