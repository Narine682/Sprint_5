
from selenium.webdriver.common.by import By
#Регистрация
NAME_INPUT = (By.NAME, "name") # Поле "Имя"
EMAIL_INPUT = (By.XPATH,  '//input[@name="name"]') # Поле "Email"
PASSWORD_INPUT = (By.NAME, "Пароль" ) # Поле "Пароль"
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Зарегистрироваться
REGISTER_ERROR = (By.XPATH, "//p[contains(@class,'input__error')]") # Сообщение об ошибке регистрации
#Логин
LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name'])[2]") # Поле "Email"
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']") # Поле "Пароль"
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти"

ACCOUNT_HEADER = (By.XPATH, "//p[text()='Личный кабинет']") # Личный кабинет
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выйти"
CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']") # Конструктор

BUNS_TAB = (By.XPATH, "//span[text()='Булки']") # Вкладка "Булки"
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']") # Вкладка "Соусы"
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']") # Вкладка "Начинки"
INGREDIENT_CARD = (By.XPATH, "//div[contains(@class,'BurgerIngredient_ingredient__')]") # Карточка ингредиента (булка, соус, начинка)





