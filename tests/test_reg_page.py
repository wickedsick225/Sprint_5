from data import Person, RandomData
from locators import RegistrationPageLocators, AuthPageLocators
from urls import URLS
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationPage:
    def test_registration_success(self, driver):
    # Проверка успешной регистрации
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomData.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(RandomData.password)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        # Ждем появления страницы авторизации
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(AuthPageLocators.login_account_btn))
        login_btn_displayed = driver.find_element(AuthPageLocators.login_account_btn).is_displayed()
        assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed

    def test_registration_incorrect_password_error(self, driver):
        # Проверка регистрации пользователя c некорректным паролем
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.registration_btn))
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(Person.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(1234)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        # Ждем появления сообщения о некорректном пароле
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegistrationPageLocators.error_message_incorrect_password))
        error = driver.find_element(*RegistrationPageLocators.error_message_incorrect_password).text
        assert (error == 'Некорректный пароль') and (driver.current_url == 'URLS.REG_PAGE_URL')


    def test_double_registration_error(self, driver):
        # Проверка повторной регистрации пользователя
        driver.get(URLS.REG_PAGE_URL)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(RegistrationPageLocators.registration_btn)
        )
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(Person.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(RegistrationPageLocators.error_message_double_reg)
        )  # Ждём появления сообщения о существующем пользователе
        error = driver.find_element(
            *RegistrationPageLocators.error_message_double_reg
        ).text
        assert (error == 'Такой пользователь уже существует') and (driver.current_url == URLS.REG_PAGE_URL)        