# -*- coding: utf-8 -*-
"""
Модуль для карусели картинок yandex.ru
"""
from atf.assert_that import assert_that, equal_to, not_equal
from atf.ui import *

from selenium.webdriver.common.by import By


class CarouselImagesPage(Region):
    """Страница картинок yandex"""

    img_carousel_elm    =   Element(      By.CSS_SELECTOR, '.MMImage-Preview', 'Картинка в карусели')
    next_btn            =   Button(       By.CSS_SELECTOR, '.CircleButton_type_next', 'Следующая картинка')
    prev_btn            =   Button(       By.CSS_SELECTOR, '.CircleButton_type_prev', 'Предыдущая картинка')

    def go_on_next_and_prev_images(self):
        """Переключение картинок кнопками навигации и проверка"""

        self.img_carousel_elm.should_be(Displayed)
        first_image_src = self.img_carousel_elm.get_attribute('src')
        self.next_btn.click()
        next_image_src = self.img_carousel_elm.get_attribute('src')
        assert_that(first_image_src, not_equal(next_image_src),
                    'Картинки одинаковые')

        self.prev_btn.click()
        last_image_src = self.img_carousel_elm.get_attribute('src')
        assert_that(first_image_src, equal_to(last_image_src),
                    'Картинки не одинаковые')
