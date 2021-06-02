from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class MainPage(BasePage):
    SEARCH_FIELD = (By.CSS_SELECTOR, '.input__control')
    SUGGEST_LIST = (By.CSS_SELECTOR, '.mini-suggest__popup')
    IMAGES_LINK = (By.CSS_SELECTOR, '[data-id="images"]')

    @allure.step('Проверка наличия поля ввода')
    def should_be_search_field(self):
        with allure.step('При открытии страницы есть поле ввода'):
            assert self.is_element_present(*self.SEARCH_FIELD), \
                'Search field is not presented'

    @allure.step('Проверка наличия таблицы с подсказками (suggest)')
    def should_be_suggest_list(self):
        with allure.step('При вводе запроса в input появляется suggest'):
            assert self.is_element_present(*self.SUGGEST_LIST), \
                'Suggest list is not presented'

    @allure.step('Проверка наличия ссылки(иконки) на Yandex images')
    def should_be_images_link(self):
        with allure.step('На главной странице присутствует ссылка на images'):
            assert self.is_element_present(*self.IMAGES_LINK), \
                'Images link is not presented'

    def click_on_image_link(self):
        images = self.browser.find_element(
            *self.IMAGES_LINK
        )
        images.click()

    def enter_request(self, request):
        enter_request = self.browser.find_element(
            *self.SEARCH_FIELD
        )
        enter_request.send_keys(request)

    def press_enter(self):
        self.browser.find_element(
            *self.SEARCH_FIELD
        ).send_keys(u'\ue007')
