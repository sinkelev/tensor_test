from atf.ui import *

from selenium.webdriver.common.by import By


class MainPage(Region):
    """Главная страница yandex"""

    search_inp      =   TextField(  By.CSS_SELECTOR,    'input.input__control', 'Поле ввода запроса')
    suggest_tbl     =   Table(      By.CSS_SELECTOR,    '.mini-suggest__popup', 'Подсказками')
    images_elm      =   Element(    By.CSS_SELECTOR,    '[data-id="images"]', 'Картинки')

    def should_be_search_field(self):
        """Проверка поисковой строки"""

        self.search_inp.should_be(Displayed)

    def should_be_suggest_list(self):
        """Проверка таблицы с подсказками (suggest)"""

        self.suggest_tbl.should_be(Displayed)

    def should_be_images_link(self):
        """Проверка иконки сервиса картинок"""

        self.images_elm.should_be(Displayed)

    def click_on_image_link(self):
        """Клик по иконке сервиса картинок"""

        self.images_elm.click()

    def enter_request(self, request):
        """Ввести запрос в поисковую строку"""

        self.search_inp.type_in(request)

    def press_enter(self):
        """Нажать Enter"""

        self.search_inp.send_keys(u'\ue007')
