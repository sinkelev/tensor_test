# -*- coding: utf-8 -*-
"""
Содержит тест поисковой системы Yandex images
"""
from atf import run_tests, log
from atf.ui import TestCaseUI

from pages.main_yandex_page import MainPage
from pages.images_yandex_page import ImagesPage


class TestSearch(TestCaseUI):
    """Открытие yandex.ru, переход на Яндекс картинки,
    проверка функционала
    """

    @classmethod
    def setup_class(cls):
        cls.browser.open('https://yandex.ru/')

    def test_01_images_in_yandex(self):
        """Открытие и перелистывание картинок"""

        log('Проверяем наличие ссылки на картинки')
        main = MainPage(self.driver)
        main.should_be_images_link()

        log('Переход на сервис картинок')
        main.click_on_image_link()
        images = ImagesPage(self.driver)
        images.switch_to_last_tab()

        log('Проверка url')
        images.should_be_images_url('https://yandex.ru/images/')

        log('Открытие первой категории картинок и сравнение текста')
        images.open_and_test_first_category()

        log('Проверка укрупненного просмотра картинок')
        images.should_be_block_images_search()
        images.open_and_check_first_image()
        images.go_on_next_and_prev_images()


if __name__ == '__main__':
    run_tests()
