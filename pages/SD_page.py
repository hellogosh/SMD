import pytest
from selenium.common import TimeoutException

from locators.locators import locators
from pages.base_page import BasePage
import time


class SdPage(BasePage):

    def authorization(self, login, password):
        self.wait_until_element_displayed(locators.LOGIN_INPUT).send_keys(login)
        self.wait_until_element_displayed(locators.PASSWORD_INPUT).send_keys(password)
        self.wait_until_element_displayed(locators.CHECK_IN_BUTTON).click()

    def service_users_button_click(self):
        self.wait_until_element_is_clickable(locators.SERVICE_USERS_BUTTON).click()

    def create_sd_drop_down_click(self):
        self.wait_until_element_is_clickable(locators.DROP_DOWN_CREATE_SD_BUTTON).click()

    def choose_needful_category_sd(self):
        self.switch_to_frame(1)
        self.wait_until_element_is_clickable(locators.REQUEST_FOR_SERVICE_BUTTON).click()

    def fill_form_SD(self, number, description1, request, employee):
        self.wait_until_element_is_clickable(locators.CONTACT_NUMBER_INPUT).send_keys(number)
        self.wait_until_element_is_clickable(locators.SHORT_DESCRIPTION_INPUT).send_keys(description1)
        self.wait_until_element_is_clickable(locators.NAME_OF_REQUEST).send_keys(request)
        self.wait_until_element_is_clickable(locators.NAME_OF_EMPOYEE_INPUT).send_keys(employee)

    def fill_initiator(self, initiator):
        self.wait_until_element_is_clickable(locators.INITIATOR_INPUT).send_keys(initiator)
        self.wait_until_element_is_clickable(locators.INITIATOR_DROP_DOWN).click()
        time.sleep(1) #обновляется форма после загрузки профиля из AD, из-за чего затирается номер, поэтому необходимо дать задержку

    def fill_service(self,service):
        self.wait_until_element_is_clickable(locators.NAME_OF_SERVICE_INPUT).send_keys(service)

    def fill_full_description(self, description2):
        self.find_element(locators.FULL_DESCRIPTION_INPUT).click()
        self.wait_until_element_is_clickable(locators.FULL_DESCRIPTION_INPUT_SECOND).send_keys(description2)

    def press_save_button(self):
        self.driver.switch_to.default_content()
        self.wait_until_element_displayed(locators.SAVE_BUTTON).click()

    def press_escalation_button(self):
        self.wait_until_element_displayed(locators.ESCALATION_BUTTON).click()

    def create_new_ZNO(self):
        self.wait_until_element_displayed(locators.CREATE_NEW_ZNO_BUTTON).click()
        try:
            self.wait_until_element_displayed(locators.SAVE_BUTTON_ZNO, timeout=60).click()
        except TimeoutException:
            pytest.fail('Время эскалации выше критического значения')
