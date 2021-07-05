# -*- coding: utf-8 -*-
"""
Модуль для страницы картинок yandex.ru
"""
from atf.assert_that import assert_that, equal_to
from atf.ui import *

from selenium.webdriver.common.by import By


class SearchImagesPage(Region):
    """Страница картинок yandex"""

    search_request_inp  =   TextField(    By.CSS_SELECTOR, '.input__control', 'Поисковый запрос')
    block_images_elm    =   Element(      By.CSS_SELECTOR, '.serp-controller__content', 'Блок с картинками')
    images_cslst        =   CustomList(   By.CSS_SELECTOR, '.serp-item__preview', 'Картинки')
    img_carousel_elm    =   Element(      By.CSS_SELECTOR, '.MMImage-Preview', 'Картинка в карусели')

    def check_text_in_input(self, category_name):
        self.search_request_inp.should_be(Displayed)
        input_txt = self.search_request_inp.get_attribute('value')
        assert_that(input_txt, equal_to(category_name),
                    'Имя категории не совпадает с запросом')

    def open_image(self, num=1):
        """Открытие и проверка первой картинки"""

        self.block_images_elm.should_be(Displayed)
        self.images_cslst.item(num).click()
        self.img_carousel_elm.should_be(Displayed)