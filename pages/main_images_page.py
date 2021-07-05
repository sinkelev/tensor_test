# -*- coding: utf-8 -*-
"""
Модуль для страницы каритнок yandex.ru
"""
from atf.ui import *

from selenium.webdriver.common.by import By


class MainImagesPage(Region):
    """Страница картинок yandex"""

    category_cslst   =   CustomList(   By.CSS_SELECTOR, '.PopularRequestList-Item', 'Категории картинок')

    def should_be_images_url(self, url):
        """Проверка url"""
        self.browser.should_be(UrlContains(url))

    def open_category(self, num=1):
        """Открытие категории картинок
        :param num: порядковый номер категории
        """
        self.category_cslst.item(num).should_be(Displayed)
        category_txt = self.category_cslst.item(num).text
        self.category_cslst.item(num).click()
        return category_txt

    def switch_to_last_tab(self):
        """Открытие последней вкладки"""

        self.browser.switch_to_window(-1)
