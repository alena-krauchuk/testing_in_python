from .base_page import BasePage
from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализация проверки на корректный url адрес
        self.MainPage.go_to_login_page()
        assert "login" in self.browser.current_url, "Opened page is not login page"

    def should_be_login_form(self):
        # реализация проверки, что форма логина есть на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is present on the page"

    def should_be_register_form(self):
        # реализация проверки, что форма регистрации есть на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is present on the page"
