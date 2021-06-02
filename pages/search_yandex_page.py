from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure


class SearchPage(BasePage):
    SEARCH_RESULT_LIST = (By.CSS_SELECTOR, '#search-result')
    LINK_IN_SEARCH_LIST = (By.XPATH, '//*[@class="serp-item"]//h2//a')

    @allure.step('Проверка наличия поисковой выдачи')
    def should_be_search_result_list(self):
        with allure.step('При преходе на страницу'
                         'поика есть результаты выдачи'):
            assert self.is_element_present(*self.SEARCH_RESULT_LIST), \
                'Search result list is not presented'

    @allure.step('Проверка наличия в первых 5 результатах ссылкы на tensor.ru')
    def first_five_links_in_search_result(self, search_link):
        first_five = self.browser.find_elements(
            *self.LINK_IN_SEARCH_LIST
        )[:5]
        for link in first_five:
            link = link.get_attribute('href')
            with allure.step('Есть ссылка на tensor.ru'):
                assert search_link in link, \
                    f'Search link is not in {link}'
