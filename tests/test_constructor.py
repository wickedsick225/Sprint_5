from locators import MainPageLocators
from urls import URLS
from expected_texts import BUN_TEXT, SAUCES_TEXT, TOPPINGS_TEXT

class TestCountructorPage:
    
    def test_transition_to_bun_success(self, driver):
    # Проверка перехода к разделу Булки
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        driver.find_element(*MainPageLocators.bun_btn).click()
        bun_text = driver.find_element(*MainPageLocators.bun).text
        bun_displayed = driver.find_element(*MainPageLocators.bun_ul).is_displayed()
        assert bun_text == BUN_TEXT and bun_displayed
    
    def test_transition_to_sauce_success(self, driver):
    # Проверка перехода к разделу Соусы
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        sauces_text = driver.find_element(*MainPageLocators.sauces).text
        sauces_displayed = driver.find_element(*MainPageLocators.sauces_ul).is_displayed()
        assert sauces_text == SAUCES_TEXT and sauces_displayed
    
    
    def test_transition_to_toppings_success(self, driver):
    # Проверка перехода к разделу Начинки
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_btn).click()
        topping_text = driver.find_element(*MainPageLocators.topping).text
        topping_displayed = driver.find_element(*MainPageLocators.topping_ul).is_displayed()
        assert topping_text == TOPPINGS_TEXT and topping_displayed