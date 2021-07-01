from atf import *
from atf.ui import *
from pages.main_yandex_page import MainPage
from pages.images_yandex_page import ImagesPage


class TestSearch(TestCaseUI):
    """Открытие yandex.ru, переход на Яндекс картинки,
    проверка функционала
    """

    @classmethod
    def setup_class(cls):
        cls.browser.open('https://yandex.ru/')

    def test_images_search_in_yandex(self):
        MainPage(self.driver).should_be_images_link()
        MainPage(self.driver).click_on_image_link()
        ImagesPage(self.driver).switch_to_last_tab()
        ImagesPage(self.driver).should_be_images_url('https://yandex.ru/images/')
        ImagesPage(self.driver).open_and_test_first_category()
        ImagesPage(self.driver).should_be_block_images_search()
        ImagesPage(self.driver).open_and_check_first_image()
        ImagesPage(self.driver).go_on_next_and_prev_images()


if __name__ == '__main__':
    run_tests()
