from atf import run_tests, log
from atf.ui import TestCaseUI

from pages.main_yandex_page import MainPage
from pages.search_yandex_page import SearchPage


class TestSearch(TestCaseUI):
    """Открытие yandex.ru, ввод и проверка suggest,
    проверка первых 5ти результатов выдачи
    """

    @classmethod
    def setup_class(cls):
        cls.browser.open('https://yandex.ru/')

    def test_search_tensor_in_yandex(self):
        """Поиск 'Тензор' в yandex"""

        log('Проверяем наличие поля ввода и подсказки')
        main = MainPage(self.driver)
        main.should_be_search_field()
        main.enter_request('Тензор')
        main.should_be_suggest_list()

        log('Переход к поисковой выдачи и проверка ссылок')
        MainPage(self.driver).press_enter()
        search = SearchPage(self.driver)
        search.should_be_search_result_list()
        search.first_five_links_in_search_result('tensor.ru')


if __name__ == '__main__':
    run_tests()
