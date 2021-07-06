# -*- coding: utf-8 -*-
"""
Модуль для страницы поиска yandex.ru
"""
from atf.assert_that import assert_that, is_in
from atf.ui import *

from selenium.webdriver.common.by import By


class SearchPage(Region):
    """Страница поисковой выдачи yandex"""

    search_cslst    = CustomList(  By.CSS_SELECTOR, '.serp-item', 'Поисковая выдача')
    links_in_rows    = Link(        By.CSS_SELECTOR, '.Link.OrganicTitle-Link_wrap', 'Ссылки на сайт')

    def check_search_result_list(self, num_lines=5, **kwargs):
        """Проверка поисковой выдачи
        :param num_lines:(int) кол-во проверяемых элементов
        :param kwargs: (dict) словарь искомых значений:
            Ссылка:(string) url сайта
        """

        self.check_load()

        for i in range(num_lines - 1):
            elm = self.get_row(i + 1)
            if 'Ссылка' in kwargs.keys():
                self.links_in_rows.add_parent(elm)
                link_in_row = self.links_in_rows.get_attribute('href')
                assert_that(kwargs.get('Ссылка'), is_in(link_in_row),
                            f'Ссылка {kwargs.get("Ссылка")} '
                            f'не совпадает с {link_in_row}')

    def check_load(self):
        """Проверка загрузки страницы"""

        self.search_cslst.should_be(Displayed)

    def get_row(self, elm_number):
        """Получиние элемента списка
        :param elm_number: (int) порядковый номер элемента
        """

        return self.search_cslst.item(elm_number)
