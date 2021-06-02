import pytest
from pages.main_yandex_page import MainPage
from pages.search_yandex_page import SearchPage


@pytest.mark.search_tensor_in_ya
def test_search_tensor_in_yandex(browser):
    url = 'https://yandex.ru/'
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_search_field()
    main_page.enter_request("Тензор")
    main_page.should_be_suggest_list()
    main_page.press_enter()
    search_page = SearchPage(browser, browser.current_url)
    search_page.should_be_search_result_list()
    search_page.first_five_links_in_search_result("tensor.ru")
