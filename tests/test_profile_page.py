from locators import MainPageLocators, PersonalAreaLocators, AuthPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestProfileArea:
    
    def test_transition_to_personal_area_from_main_page_success(self, driver, get_login_drive):
    # Проверка перехода в личный кабинет с главной страницы по кнопке "Личный кабинет"
        driver = get_login_drive
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn)) #Ждем появления кнопки "Личный кабинет"
        driver.find_element(*MainPageLocators.personal_account_btn).click() #кликаем по кнопке "Личный кабинет"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn)) # Проверяем что кнопка Выхода появилась
        exit_btn_displayed = driver.find_element(*PersonalAreaLocators.exit_btn).is_displayed() #Проверяем что кнопка Выхода активна
        assert exit_btn_displayed and driver.current_url == URLS.AUTH_PAGE_URL
    
   
    def test_transition_to_counstructor_from_personal_area_page_by_click_constructor_btn_success(self, driver, get_login_drive):
        # Проверка перехода в конструктор из личного кабинета по кнопке "Конструктор"
        driver = get_login_drive
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn)) #Ждем появления кнопки "Личный кабинет"
        driver.find_element(*MainPageLocators.personal_account_btn).click() #кликаем по кнопке "Личный кабинет"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn)) # Проверяем что кнопка Выхода появилась
        driver.find_element(*PersonalAreaLocators.constructor_btn).click()# Переходим в конструктор
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(MainPageLocators.bun))
        bun_displayed = driver.find_element(*MainPageLocators.bun_btn).is_displayed()
        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed

   
    def test_transition_to_counstructor_from_personal_area_page_by_click_logo_success(self, driver, get_login_drive):
        # Проверка перехода в конструктор из личного кабинета по клику на лого
        driver = get_login_drive
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn)) #Ждем появления кнопки "Личный кабинет"
        driver.find_element(*MainPageLocators.personal_account_btn).click() #кликаем по кнопке "Личный кабинет"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        driver.find_element(*MainPageLocators.logo_btn).click # Проверка перехода в конструктор по клику на лого
        WebDriverWait(driver,10).until(EC.visibility_of_element_located(MainPageLocators.bun))
        bun_displayed = driver.find_element(*MainPageLocators.bun_btn).is_displayed()
        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed
        
        
    def test_logout_from_personal_area_success(self, driver, get_login_driver):
        # Проверка выхода из личного кабинета
        driver = get_login_driver
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(MainPageLocators.personal_account_btn))
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PersonalAreaLocators.exit_btn))
        driver.find_element(*PersonalAreaLocators.exit_btn).click()  # Жмём "Выход"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(AuthPageLocators.login_account_btn))
        login_btn_displayed = driver.find_element(*AuthPageLocators.login_account_btn).is_displayed()  # Проверяем, что кнопка входа видна
        assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed

