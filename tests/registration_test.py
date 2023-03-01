import time

from pages.registration_page import RegistrationPage

class TestRegistration:
    def test_registration(self, driver):
        registration_page = RegistrationPage(driver, "https://rozetka.com.ua/ua/")
        registration_page.open()
        registration_page.way_to_fills()
        registration_page.fill_all_fields()
        time.sleep(5)
