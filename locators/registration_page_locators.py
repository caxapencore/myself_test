from selenium.webdriver.common.by import By

class RegistrationPageLocators:

    #way to menu
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[class="header__button ng-star-inserted"]')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[class="auth-modal__register-link button button--link ng-star-inserted"]')

    #registration window
    USER_NAME = (By.CSS_SELECTOR, 'input[id="registerUserName"]')
    USER_SURNAME = (By.CSS_SELECTOR, 'input[id="registerUserSurname"]')
    PHONE_NUMBER = (By.CSS_SELECTOR, 'input[id="registerUserPhone"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="registerUserEmail"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[id="registerUserPassword"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[class="button button--large button--green auth-modal__submit"]')



