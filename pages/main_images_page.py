# -*- coding: utf-8 -*-
"""
Модуль для страницы каритнок yandex.ru
"""
from atf.ui import *

from selenium.webdriver.common.by import By


class MainImagesPage(Region):
    """Страница картинок yandex"""

    category_cslst   =   CustomList(   By.CSS_SELECTOR, '.PopularRequestList-Item', 'Категории картинок')

    def check_url(self, url):
        """Проверка url"""
        self.browser.should_be(UrlContains(url))

    def open_category(self, num=1):
        """Открытие категории картинок
        :param num: порядковый номер категории
        """
        self.check_load()
        category_txt = self.category_cslst.item(num).text
        self.category_cslst.item(num).click()
        return category_txt

    def check_load(self):
        """Проверка загрузки страницы"""
        self.category_cslst.should_be(Displayed)
