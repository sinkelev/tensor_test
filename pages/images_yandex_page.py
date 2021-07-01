# -*- coding: utf-8 -*-
"""
Модуль для страницы каритнок yandex.ru
"""
from atf.assert_that import assert_that, equal_to, not_equal
from atf.ui import *

from selenium.webdriver.common.by import By


class ImagesPage(Region):
    """Страница картинок yandex"""

    category_elm        =   Element(      By.XPATH,        '//*[@class="PopularRequestList"]/div[1]/a/div[2]', 'Первая категория картинок')
    search_request_inp  =   TextField(    By.CSS_SELECTOR, '.input__control', 'Поисковый запрос')
    block_images_elm    =   Element(      By.CSS_SELECTOR, '.serp-controller__content', 'Блок с картинками')
    first_image_elm     =   Element(      By.XPATH,        '//div[@class="serp-controller__content"]/div/div[1]//a', 'Первая картинка')
    img_carousel_elm    =   Element(      By.CSS_SELECTOR, '.MMImage-Preview', 'Картинка в карусели')
    next_btn            =   Button(       By.CSS_SELECTOR, '.CircleButton_type_next', 'Следующая картинка')
    prev_btn            =   Button(       By.CSS_SELECTOR, '.CircleButton_type_prev', 'Предыдущая картинка')

    def should_be_images_url(self, url):
        """Проверка url"""

        self.browser.should_be(UrlContains(url))

    def open_and_test_first_category(self):
        """Открытие первой катеогрии картинок и проверка
        сответствия текста и поискового запроса
        """

        category_txt = self.category_elm.text
        self.category_elm.click()
        input_txt = self.search_request_inp.get_attribute('value')
        assert_that(category_txt, equal_to(input_txt),
                    'Имя категории не совпадает с запросом')

    def should_be_block_images_search(self):
        """Проверка блока с картинками"""

        self.block_images_elm.should_be(Displayed)

    def open_and_check_first_image(self):
        """Открытие и проверка первой картинки"""

        self.first_image_elm.click()
        self.img_carousel_elm.should_be(Displayed)

    def go_on_next_and_prev_images(self):
        """Переключение картинок кнопками навигации и проверка"""

        first_image_src = self.img_carousel_elm.get_attribute('src')
        self.next_btn.click()
        next_image_src = self.img_carousel_elm.get_attribute('src')
        assert_that(first_image_src, not_equal(next_image_src),
                    'Картинки одинаковые')

        self.prev_btn.click()
        last_image_src = self.img_carousel_elm.get_attribute('src')
        assert_that(first_image_src, equal_to(last_image_src),
                    'Картинки не одинаковые')

    def switch_to_last_tab(self):
        """Открытие последней вкладки"""

        self.browser.switch_to_window(-1)
