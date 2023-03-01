import time

from generator.generator import generated_person
from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    locators = RegistrationPageLocators

    def way_to_fills(self):
        self.element_is_visible(self.locators.ACCOUNT_BUTTON).click()
        self.element_is_clickable(self.locators.REGISTRATION_BUTTON).click()

    def fill_all_fields(self):
        person_info = next(generated_person())
        user_name = person_info.user_name
        user_surname = person_info.user_surname
        phone_number = person_info.phone_number
        email = person_info.email
        password = person_info.password

        self.element_is_visible(self.locators.USER_NAME).send_keys(user_name)
        self.element_is_visible(self.locators.USER_SURNAME).send_keys(user_surname)
        self.element_is_visible(self.locators.PHONE_NUMBER).send_keys(phone_number)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()