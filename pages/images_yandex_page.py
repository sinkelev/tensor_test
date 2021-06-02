from .base_page import BasePage
from selenium.webdriver.common.by import By


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

    def should_be_images_url(self):
        assert "https://yandex.ru/images/" in self.browser.current_url, \
            f"Is not Yandex images url {self.browser.current_url}"

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
        assert text_category == text_in_input, \
            "Сategory name does not match text in search"

    def should_be_block_images_search(self):
        assert self.is_element_present(*self.BLOCK_SEARCH_IMAGES), \
            "Block with images is not presented"

    def open_and_check_first_image(self):
        image = self.browser.find_element(
            *self.FIRST_IMAGES_IN_BLOCK
        )
        image.click()
        assert self.is_element_present(*self.OPEN_IMAGES), \
            "Image does not open"

    def go_on_next_and_prev_images(self):
        fist_image_src = self.browser.find_element(
            *self.OPEN_IMAGES
        ).get_attribute('src')
        self.browser.find_element(*self.NEXT_IMAGE).click()
        next_image_src = self.browser.find_element(
            *self.OPEN_IMAGES
        ).get_attribute('src')
        assert fist_image_src != next_image_src, \
            "Images are the same"

        self.browser.find_element(*self.PREV_IMAGE).click()
        last_image_src = self.browser.find_element(
            *self.OPEN_IMAGES
        ).get_attribute('src')
        assert fist_image_src == last_image_src, \
            "Images are not the same"
