from atf.assert_that import *
from atf.ui import *
from selenium.webdriver.common.by import By


class SearchPage(Region):
    """Страница поисковой выдачи yandex"""
    search_result_list  =   Element(        By.CSS_SELECTOR, '#search-result', 'Поисковая выдача')
    link_in_search_list =   CustomList(     By.XPATH,        '//*[@class="serp-item"]//h2//a', 'Ссылка на сайт')

    def should_be_search_result_list(self):
        """Проверка таблицы с результатами"""
        self.search_result_list.should_be(Displayed)

    def first_five_links_in_search_result(self, search_link):
        """В первых 5ти результатах присутстует ссылка """
        for link in self.link_in_search_list:
            link = link.get_attribute('href')
            assert_that(search_link, is_in(link), f'Search link is not in {link}')
