from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.actions = ActionChains(driver)

    def open(self):
        self.driver.get(self.url)

    def wait_until_element_displayed(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    
    def move_to_element(self, locator):
        self.actions.reset_actions()
        self.actions.move_to_element(self.find_element(locator)).perform()


    def wait_until_element_is_clickable(self, locator, timeout=30):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_to_frame(self, n):
        self.driver.switch_to.frame(n)


