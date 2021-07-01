from atf.assert_that import *
from atf.ui import *
from selenium.webdriver.common.by import By


class ImagesPage(Region):
    """Страница картинок yandex"""
    category_picture        =   Element(By.XPATH,        '//*[@class="PopularRequestList"]/div[1]/a/div[2]', 'Первая категория картинок')
    input_on_images_page    =   Element(By.CSS_SELECTOR, '.input__control', 'Поле ввода запроса')
    block_search_images     =   Element(By.CSS_SELECTOR, '.serp-controller__content', 'Блок с картинками')
    first_images_in_block   =   Element(By.XPATH,        '//div[@class="serp-controller__content"]/div/div[1]//a','Первая картинка')
    open_images             =   Element(By.CSS_SELECTOR, '.MMImage-Preview', 'Картинка в карусели')
    next_image              =   Element(By.CSS_SELECTOR, '.CircleButton_type_next', 'Кнопка следующая картинка')
    prev_image              =   Element(By.CSS_SELECTOR, '.CircleButton_type_prev', 'Кнопка предыдущая картинка')

    def should_be_images_url(self, url):
        """Проверка url"""
        self.browser.should_be(UrlContains(url))

    def open_and_test_first_category(self):
        """Открытие первой катеогрии картинок и проверка
        сответствия текста и поискового запроса
        """
        text_category = self.category_picture.text
        self.category_picture.click()
        text_in_input = self.input_on_images_page.get_attribute('value')
        assert_that(text_category, equal_to(text_in_input), 'Имя категории не совпадает с запросом')

    def should_be_block_images_search(self):
        """Проверка блока с картинками"""
        self.block_search_images.should_be(Displayed)

    def open_and_check_first_image(self):
        """Открытие и проверка первой картинки"""
        self.first_images_in_block.click()
        self.open_images.should_be(Displayed)

    def go_on_next_and_prev_images(self):
        """Переключение картинок кнопками навигации и проверка"""
        fist_image_src = self.open_images.get_attribute('src')
        self.next_image.click()
        next_image_src = self.open_images.get_attribute('src')
        assert_that(fist_image_src, not_equal(next_image_src), 'Картинки одинаковые')
        self.prev_image.click()
        last_image_src = self.open_images.get_attribute('src')
        assert_that(fist_image_src, equal_to(last_image_src), 'Картинки не одинаковые')

    def switch_to_last_tab(self):
        """Открытие последней вкладки"""
        self.browser.switch_to_window(-1)
