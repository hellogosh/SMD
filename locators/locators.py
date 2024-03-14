from selenium.webdriver.common.by import By


class locators():
    URL = 'https://hpsm.emias.mos.ru/sm/index.do'
    LOGIN_INPUT = (By.ID, 'LoginUsername')
    PASSWORD_INPUT = (By.ID, 'LoginPassword')
    CHECK_IN_BUTTON = (By.ID, 'loginBtn')
    SERVICE_USERS_BUTTON = (By.XPATH, '//span[contains(text(), "Управление Обращениями")]')
    DROP_DOWN_CREATE_SD_BUTTON = (By.XPATH, '//span[contains(text(), "Создать обращение")]')
    TOOL_TIP_BUTTON = (By.XPATH, '//*[@id="ext-gen-top428"]/span')
    REQUEST_FOR_SERVICE_BUTTON = (By.XPATH, '//a[contains(text(), "Запрос на обслуживание")]')

    INITIATOR_INPUT = (By.ID, 'X6')
    INITIATOR_DROP_DOWN = (By.XPATH, '//*[@id="X6Popup_0_0"]')
    CONTACT_NUMBER_INPUT = (By.ID, 'X21')
    NAME_OF_SERVICE_INPUT = (By.ID, 'X47')
    SHORT_DESCRIPTION_INPUT = (By.ID, 'X63')
    FULL_DESCRIPTION_INPUT = (By.CSS_SELECTOR, 'div#X67Edit')
    FULL_DESCRIPTION_INPUT_SECOND = (By.CSS_SELECTOR, 'div#X67Edit textarea')
    NAME_OF_REQUEST = (By.ID, 'X29')
    NAME_OF_EMPOYEE_INPUT = (By.ID, 'X45')
    SAVE_BUTTON = (By.XPATH, '//button[contains(text(),"Сохранить")]')
    ESCALATION_BUTTON = (By.XPATH, '//button[contains(text(), "Выполнить эскалацию")]')
    CREATE_NEW_ZNO_BUTTON = (By.XPATH, '//button[contains(text(), "Создание нового запроса")]')
    SAVE_BUTTON_ZNO = (By.XPATH, '//button[contains(text(), "Сохранить и выйти")]')



