# -*- coding: utf-8 -*-
"""
Модуль для страницы поиска yandex.ru
"""
from atf.assert_that import assert_that, is_in
from atf.ui import *

from selenium.webdriver.common.by import By


class SearchPage(Region):
    """Страница поисковой выдачи yandex"""

    search_tbl       =   Table(          By.CSS_SELECTOR,    '#search-result', 'Поисковая выдача')
    site_link_cslst  =   CustomList(     By.XPATH,           '//*[@class="serp-item"]//h2//a', 'Ссылки на сайт')

    def should_be_search_result_list(self):
        """Проверка таблицы с результатами"""

        self.search_tbl.should_be(Displayed)

    def match_links(self, search_link, count_link=1):
        """В результатах поисковой выдачи присутстует ссылка """

        for i in range(count_link-1):
            link = self.site_link_cslst.item(i+1).get_attribute('href')
            assert_that(search_link, is_in(link),
                        f'Ссылка {link} не совпадает с {search_link}')
