from pages.SD_page import SdPage



def test_check_time_of_escalation(driver):
        """
        Имя сценария: "Проверка времени эскалации Обращения типа ЗНО"

        Шаг 1: "Открыть стартовую страницу"
                https://hpsm.emias.mos.ru/sm/index.do
        Шаг 2: "Ввести учетные данные"
                    логин: AutoTestUser
                    пароль: UserAutoTest
        Шаг 3: "В колонке слева выбрать Служба поддержки пользователей"
        Шаг 4: "В выпадающем списке выбрать Создать обращение"
        Шаг 5: "Выбрать категорию Запрос на обслуживание"
        Шаг 6: "Заполнить карточку регистрации Обращения"
                    Инициатор: ПАНТЮХОВ ГЕОРГИЙ (PANTYUKHOV.GS)
                    Контактное лицо: ПАНТЮХОВ ГЕОРГИЙ (PANTYUKHOV.GS)
                    Телефон контактного лица: 0000
                    Сервис: Тестовый ЕМИАС(CI9954462)
                    Краткое описание: Тест
                    Описание: Тест
                    Наименование запроса: Управление запросами ТЕСТ
                    Сотрудник ЦК: ПАНТЮХОВ ГЕОРГИЙ (PANTYUKHOV.GS)

        Шаг 7: "Нажать Сохранить"
        Шаг 8: "Эскалировать обращение"
        Шаг 9: "Создание Нового запроса в шапке страницы"
        Шаг 10: "Сохранить запрос"
        """

        link = 'http://10.2.162.14:8080/smnoldap/index.do'
        login = "AutoTestUser"
        password = "UserAutoTest"
        initiator = 'ПАНТЮХОВ ГЕОРГИЙ (PANTYUKHOV.GS)'
        number = '0000'
        description1 = 'Тест'
        description2 = 'Тестирование'
        request = 'Управление запросами ТЕСТ'
        employee = 'ПАНТЮХОВ ГЕОРГИЙ (PANTYUKHOV.GS)'



        #Шаг 1: Открыть стартовую страницу
        page = SdPage(driver, link)
        page.open()

        #"Шаг 2: Ввести учетные данные"
        page.authorization(login, password)

        #Шаг 3: "В колонке слева выбрать Служба поддержки пользователей"
        page.service_users_button_click()

        #Шаг 4: "В выпадающем списке выбрать Создать обращение"
        page.create_sd_drop_down_click()

        #Шаг 5: "Выбрать категорию Запрос на обслуживание"
        page.choose_needful_category_sd()

        #Шаг 6: "Заполнить карточку регистрации Обращения"
        page.fill_initiator(initiator)
        page.fill_form_SD(number, description1, request, employee)
        page.fill_full_description(description2)

        #Шаг 7: "Нажать Сохранить"
        page.press_save_button()

        #Шаг 8: "Эскалировать обращение"
        page.press_escalation_button()
        page.create_new_ZNO()







