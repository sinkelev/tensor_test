from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class ImagesPage(BasePage):
    CATEGORY_PICTURE = (By.XPATH, '//*[@class="PopularRequestList"]/div[1]/a')
    TEXT_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-SearchText')
    INPUT_ON_IMAGES_PAGE = (By.CSS_SELECTOR, '.input__control')
    BLOCK_SEARCH_IMAGES = (By.CSS_SELECTOR, '.serp-controller__content')
    FIRST_IMAGES_IN_BLOCK = (
        By.XPATH,
        '//div[@class="serp-controller__content"]/div/div[1]//a'
    )
    OPEN_IMAGES = (By.CSS_SELECTOR, '.MMImage-Preview')
    NEXT_IMAGE = (By.CSS_SELECTOR, '.CircleButton_type_next')
    PREV_IMAGE = (By.CSS_SELECTOR, '.CircleButton_type_prev')

    @allure.step('Проверка url https://yandex.ru/images/')
    def should_be_images_url(self):
        with allure.step('При преходе на страницу Yandex images'
                         'url:https://yandex.ru/images/'):
            assert 'https://yandex.ru/images/' in self.browser.current_url, \
                f'Is not Yandex images url {self.browser.current_url}'

    @allure.step('Открытие и проверка соответствие текста в input')
    def open_and_test_first_category(self):
        image = self.browser.find_element(
            *self.CATEGORY_PICTURE
        )
        text_category = self.browser.find_element(
            *self.CATEGORY_PICTURE
        ).text
        image.click()
        text_in_input = self.browser.find_element(
            *self.INPUT_ON_IMAGES_PAGE
        ).get_attribute('value')
        with allure.step('При клике на первую категорию в input верный текст'):
            assert text_category == text_in_input, \
                'Сategory name does not match text in search'

    @allure.step('Проверка наличия блока с картинками')
    def should_be_block_images_search(self):
        with allure.step('На странице присутствует поисковая'
                         'выдача с картинками'):
            assert self.is_element_present(*self.BLOCK_SEARCH_IMAGES), \
                'Block with images is not presented'

    @allure.step('Открытие и проверка первой картинки')
    def open_and_check_first_image(self):
        image = self.browser.find_element(
            *self.FIRST_IMAGES_IN_BLOCK
        )
        image.click()
        with allure.step('Открылась первая картинка'):
            assert self.is_element_present(*self.OPEN_IMAGES), \
                'Image does not open'

    @allure.step('Проверка переключения картинок')
    def go_on_next_and_prev_images(self):
        fist_image_src = self.browser.find_element(
            *self.OPEN_IMAGES
        ).get_attribute('src')
        self.browser.find_element(*self.NEXT_IMAGE).click()
        next_image_src = self.browser.find_element(
            *self.OPEN_IMAGES
        ).get_attribute('src')
        with allure.step('Переключение картинки'):
            assert fist_image_src != next_image_src, \
                'Images are the same'

        self.browser.find_element(*self.PREV_IMAGE).click()
        last_image_src = self.browser.find_element(
            *self.OPEN_IMAGES
        ).get_attribute('src')
        with allure.step('Возврат к предыдущей картинке'):
            assert fist_image_src == last_image_src, \
                'Images are not the same'
