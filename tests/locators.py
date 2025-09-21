
from selenium.webdriver.common.by import By
#Регистрация
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input") # Поле "Имя"
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input") # Поле "Email"
PASSWORD_INPUT = (By.XPATH,  "//label[text()='Пароль']/following-sibling::input") # Поле "Пароль"
REGISTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') # Зарегистрироваться
REGISTER_ERROR = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p') # Сообщение об ошибке регистрации
#Логин
LOGIN_EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input') # Поле "Email" на форме входа
LOGIN_PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input') # Поле "Пароль" на форме входа
LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button') # Кнопка "Войти"

ACCOUNT_HEADER = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p') # Личный кабинет
LOGOUT_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button') # Кнопка "Выйти"
CONSTRUCTOR_LINK = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p') # Конструктор
BUNS_TAB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span') # Вкладка "Булки"
SAUCES_TAB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span') # Вкладка "Соусы"
FILLINGS_TAB = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span') # Вкладка "Начинки"
INGREDIENT_CARD = (By.XPATH, "//div[contains(@class,'ingredient-card')]") # Карточка ингредиента (булка, соус, начинка)






