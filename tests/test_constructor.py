import pytest
from locators import MainPageLocators
from urls import URLS
from expected_texts import BUN_TEXT, SAUCES_TEXT, TOPPINGS_TEXT

@pytest.mark.parametrize(
    "preclick, btn_locator, section_locator, ul_locator, expected_text",
    [
        # Для Булок — сначала кликаем "Соусы", затем "Булки"
        (MainPageLocators.sauces_btn, MainPageLocators.bun_btn, MainPageLocators.bun, MainPageLocators.bun_ul, BUN_TEXT),

        # Для Соусов — просто кликаем "Соусы"
        (None, MainPageLocators.sauces_btn, MainPageLocators.sauces, MainPageLocators.sauces_ul, SAUCES_TEXT),

        # Для Начинок — просто кликаем "Начинки"
        (None, MainPageLocators.toppings_btn, MainPageLocators.topping, MainPageLocators.topping_ul, TOPPINGS_TEXT),
    ],
    ids=["Булки (через Соусы)", "Соусы", "Начинки"]
)
def test_transition_sections(driver, preclick, btn_locator, section_locator, ul_locator, expected_text):
    driver.get(URLS.MAIN_PAGE_URL)

    # если нужно — сначала уходим в другой раздел
    if preclick:
        driver.find_element(*preclick).click()

    driver.find_element(*btn_locator).click()

    # проверяем текст и наличие блока
    section_text = driver.find_element(*section_locator).text
    section_displayed = driver.find_element(*ul_locator).is_displayed()
    assert section_text == expected_text and section_displayed