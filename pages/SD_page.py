
from locators.locators import locators
from pages.base_page import BasePage
import time


class SdPage(BasePage):

    def authorization(self, login, password):
        self.wait_until_element_displayed(locators.LOGIN_INPUT).send_keys(login)
        self.wait_until_element_displayed(locators.PASSWORD_INPUT).send_keys(password)
        self.wait_until_element_displayed(locators.CHECK_IN_BUTTON).click()

    def click_create_SD_tool_tip(self, hover_element, wait_element):
        element = self.wait_until_element_displayed(hover_element)
        self.move_to_element(element)
        self.wait_until_element_is_clickable(locators.TOOL_TIP_BUTTON).click()


    def service_users_button_click(self):
        self.wait_until_element_is_clickable(locators.SERVICE_USERS_BUTTON).click()

    def create_sd_drop_down_click(self):
        self.wait_until_element_is_clickable(locators.DROP_DOWN_CREATE_SD_BUTTON).click()


    def choose_needful_category_sd(self):
        self.switch_to_frame(1)
        self.wait_until_element_is_clickable(locators.REQUEST_FOR_SERVICE_BUTTON).click()
        # self.driver.switch_to.default_content()

    def fill_form_SD(self, initiator, contact, number, service, description1, description2, request, employee):
        self.wait_until_element_is_clickable(locators.INITIATOR_INPUT).send_keys(initiator)
        self.wait_until_element_is_clickable(locators.CONTACT_NAME_INPUT).send_keys(contact)
        self.wait_until_element_is_clickable(locators.CONTACT_NUMBER_INPUT).send_keys(number)
        self.wait_until_element_is_clickable(locators.NAME_OF_SERVICE_INPUT).send_keys(service)
        time.sleep(2)
        self.wait_until_element_is_clickable(locators.SHORT_DESCRIPTION_INPUT).send_keys(description1)
        self.wait_until_element_is_clickable(locators.NAME_OF_REQUEST).send_keys(request)
        self.wait_until_element_is_clickable(locators.NAME_OF_EMPOYEE_INPUT).send_keys(employee)
        time.sleep(2)

    def fill_full_description(self, description2):
        time.sleep(1)
        self.find_element(locators.FULL_DESCRIPTION_INPUT).click()
        time.sleep(1)
        self.wait_until_element_is_clickable(locators.FULL_DESCRIPTION_INPUT_SECOND).send_keys(description2)
        time.sleep(1)


    def press_save_button(self):
        self.driver.switch_to.default_content()
        self.wait_until_element_displayed(locators.SAVE_BUTTON).click()


    def press_escalation_button(self):
        self.wait_until_element_displayed(locators.ESCALATION_BUTTON).click()


    def create_new_ZNO(self):
        self.wait_until_element_displayed(locators.CREATE_NEW_ZNO_BUTTON).click()
        self.wait_until_element_displayed(locators.SAVE_BUTTON_ZNO).click()