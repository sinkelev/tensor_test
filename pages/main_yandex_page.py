from atf.ui import *
from selenium.webdriver.common.by import By


class MainPage(Region):
    """Главная страница yandex"""
    search_field    =   Element(By.CSS_SELECTOR, 'input.input__control', 'Поле ввода запроса')
    suggest_list    =   Element(By.CSS_SELECTOR, '.mini-suggest__popup', 'Таблица с подсказками')
    images_link     =   Element(By.CSS_SELECTOR, '[data-id="images"]', 'Иконка перехода на картинки')

    def should_be_search_field(self):
        """Проверка поисковой строки"""
        self.search_field.should_be(Displayed)

    def should_be_suggest_list(self):
        """Проверка таблицы с подсказками (suggest)"""
        self.suggest_list.should_be(Displayed)

    def should_be_images_link(self):
        """Проверка иконки сервиса картинок"""
        self.images_link.should_be(Displayed)

    def click_on_image_link(self):
        """Клик по иконке сервиса картинок"""
        self.images_link.click()

    def enter_request(self, request):
        """Ввести запрос в поисковую строку"""
        self.search_field.type_in(request)

    def press_enter(self):
        """Нажать Enter"""
        self.search_field.send_keys(u'\ue007')
