# -*- coding: utf-8 -*-
"""
Содержит тест поисковой системы Yandex images
"""
from atf import run_tests, log
from atf.ui import TestCaseUI

from pages.main_page import MainPage
from pages.main_images_page import MainImagesPage
from pages.search_images_page import SearchImagesPage
from pages.carousel_page import CarouselImagesPage


class TestSearch(TestCaseUI):
    """Открытие yandex.ru, переход на Яндекс картинки,
    проверка функционала
    """

    url = 'https://yandex.ru/'
    category_num = 1
    image_num = 1

    @classmethod
    def setup_class(cls):
        cls.browser.open(cls.url)

    def test_01_images_in_yandex(self):
        """Открытие и перелистывание картинок"""

        main_pg = MainPage(self.driver)

        log('Переход на сервис картинок. Проверка URL. Открытие категории картинок.')
        main_pg.go_to('Картинки')
        main_images_pg = MainImagesPage(self.driver)
        main_images_pg.switch_to_last_tab()
        main_images_pg.should_be_images_url(self.url + 'images/')
        category_name = main_images_pg.open_category(self.category_num)

        log('Проверка поискового запроса. Открытие картиноки в карусели.')
        search_images_pg = SearchImagesPage(self.driver)
        search_images_pg.check_text_in_input(category_name)
        search_images_pg.open_image(self.image_num)

        log('Проверка навигации карусели.')
        carousel_images = CarouselImagesPage(self.driver)
        carousel_images.go_on_next_and_prev_images()


if __name__ == '__main__':
    run_tests()
