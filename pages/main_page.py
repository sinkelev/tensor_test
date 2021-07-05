# -*- coding: utf-8 -*-
"""
Модуль для Главной страницы yandex.ru
"""
from atf.ui import *

from selenium.webdriver.common.by import By


class MainPage(Region):
    """Главная страница yandex"""

    search_inp = TextField(By.CSS_SELECTOR, 'input.input__control', 'Поле ввода запроса')
    suggest_tbl = Table(By.CSS_SELECTOR, '.mini-suggest__popup', 'Подсказками')
    images_lnk = Link(By.CSS_SELECTOR, '[data-id="images"]', 'Картинки')
    services_cslst = CustomList(By.CSS_SELECTOR, '.services-new__list-item a', 'Сервисы')

    def should_be_suggest_list(self):
        """Проверка таблицы с подсказками (suggest)"""

        self.suggest_tbl.should_be(Displayed)

    def go_to(self, name):
        """Клик по иконке сервиса"""

        self.services_cslst.item(with_text=name).should_be(Displayed)
        self.services_cslst.item(with_text=name).click()

    def enter_request(self, request):
        """Ввести запрос в поисковую строку"""

        self.search_inp.should_be(Displayed)
        self.search_inp.type_in(request)

    def press_enter(self):
        """Нажать Enter"""

        self.search_inp.send_keys(u'\ue007')
