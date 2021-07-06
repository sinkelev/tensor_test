# -*- coding: utf-8 -*-
"""
Модуль для страницы поиска yandex.ru
"""
from atf.assert_that import assert_that, is_in
from atf.ui import *

from selenium.webdriver.common.by import By


class SearchPage(Region):
    """Страница поисковой выдачи yandex"""

    search_cslst    =   CustomList(    By.CSS_SELECTOR,    '.serp-item', 'Поисковая выдача')
    link            =   Link(          By.CSS_SELECTOR,    '.Link.OrganicTitle-Link_wrap', 'Ссылки на сайт')

    def check_search_result_list(self, check_elm=5, **kwargs):
        """В результатах поисковой выдачи присутстует ссылка
        :param check_elm: кол-во проверяемых элементов
        :param kwargs: словарь искомых значений
        """

        self.check_load()

        for i in range(check_elm-1):
            elm = self.get_elm(i+1)
            self.link.add_parent(elm)
            if 'Ссылка' in kwargs.keys():
                link_in_search = self.link.get_attribute('href')
                assert_that(kwargs.get('Ссылка'), is_in(link_in_search),
                            f'Ссылка {kwargs.get("Ссылка")} '
                            f'не совпадает с {link_in_search}')

    def check_load(self):
        """Проверка загрузки страницы"""

        self.search_cslst.should_be(Displayed)

    def get_elm(self, elm_number):
        """Получиние элемента списка"""

        return self.search_cslst.item(elm_number)
