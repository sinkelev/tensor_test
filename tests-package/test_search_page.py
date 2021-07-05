# -*- coding: utf-8 -*-
"""
Содержит тест поисковой системы Yandex.ru
"""
from atf import run_tests, log
from atf.ui import TestCaseUI

from pages.main_page import MainPage
from pages.search_page import SearchPage


class TestSearch(TestCaseUI):
    """Открытие yandex.ru, ввод и проверка suggest,
    проверка первых 5ти результатов выдачи
    """

    @classmethod
    def setup_class(cls):
        cls.browser.open('https://yandex.ru/')

    def test_01_search_tensor(self):
        """Поиск 'Тензор' в yandex"""

        log('Проверяем наличие поля ввода и подсказки')
        main_pg = MainPage(self.driver)
        main_pg.enter_request('Тензор')
        main_pg.should_be_suggest_list()

        log('Переход к поисковой выдачи и проверка ссылок')
        main_pg.press_enter()
        search_pg = SearchPage(self.driver)
        search_pg.should_be_search_result_list()
        search_pg.match_links('tensor.ru', 5)


if __name__ == '__main__':
    run_tests()
