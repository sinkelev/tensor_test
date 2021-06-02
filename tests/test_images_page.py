import pytest
from pages.main_yandex_page import MainPage
from pages.images_yandex_page import ImagesPage


@pytest.mark.test_image_service_ya
def test_search_tensor_in_yandex(browser):
    url = 'https://yandex.ru/'
    main_page = MainPage(browser, url)
    main_page.open()
    main_page.should_be_images_link()
    main_page.click_on_image_link()
    images_page = ImagesPage(browser, browser.current_url)
    images_page.switch_to_last_tab()
    images_page.should_be_images_url()
    images_page.open_and_test_first_category()
    images_page.should_be_block_images_search()
    images_page.open_and_check_first_image()
    images_page.go_on_next_and_prev_images()
