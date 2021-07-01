from atf import *
from atf.ui import *
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
        MainPage(self.driver).should_be_search_field()
        MainPage(self.driver).enter_request("Тензор")
        MainPage(self.driver).should_be_suggest_list()
        MainPage(self.driver).press_enter()
        SearchPage(self.driver).should_be_search_result_list()
        SearchPage(self.driver).first_five_links_in_search_result("tensor.ru")


if __name__ == '__main__':
    run_tests()
