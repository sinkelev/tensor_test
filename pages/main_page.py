# -*- coding: utf-8 -*-
"""
Модуль для Главной страницы yandex.ru
"""
from atf.ui import *

from selenium.webdriver.common.by import By


class MainPage(Region):
    """Главная страница yandex"""

    search_inp      = TextField     (By.CSS_SELECTOR, 'input.input__control', 'Поле ввода запроса')
    suggest_elm     = Element       (By.CSS_SELECTOR, '.mini-suggest__popup', 'Подсказками')
    images_lnk      = Link          (By.CSS_SELECTOR, '[data-id="images"]', 'Картинки')
    services_cslst  = CustomList    (By.CSS_SELECTOR, '.services-new__list-item a', 'Сервисы')
    submit_btn      = Button        (By.CSS_SELECTOR, 'button.button.mini-suggest__button', 'Найти')

    def go_to(self, name):
        """Клик по иконке сервиса
        :param name: имя сервиса
        """

        self.check_load()
        self.services_cslst.item(with_text=name).click()
        self.browser.switch_to_window(-1)

    def search(self, request, submit_type=True):
        """Ввести запрос в поисковую строку
        :param request: запрос
        :param submit_type: отправить нажатием на кнопку Найти
        """

        self.check_load()
        self.search_inp.type_in(request)
        self.suggest_elm.should_be(Displayed)
        if not submit_type:
            self.search_inp.send_keys(u'\ue007')
        else:
            self.submit_btn.click()

    def check_load(self):
        """Проверка загрузки страницы"""

        self.search_inp.should_be(Displayed)
