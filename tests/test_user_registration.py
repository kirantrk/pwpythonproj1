from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilis.random_data_util import RandomDataUtil
from playwright.sync_api import expect
import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_user_registration(page):
    home_page = HomePage(page)
    registration_page = RegistrationPage(page)
    random_data = RandomDataUtil()

    home_page.click_my_account()
    home_page.click_register()

    password = random_data.get_password()

    registration_page.set_first_name(random_data.get_first_name())
    registration_page.set_last_name(random_data.get_last_name())
    registration_page.set_email(random_data.get_email())
    registration_page.set_telephone(random_data.get_phone_number())
    registration_page.set_password(password)
    registration_page.set_confirm_password(password)
    registration_page.set_privacy_policy()
    registration_page.click_continue()

    confirmation_msg = registration_page.get_confirmation_msg()
    expect(confirmation_msg).to_have_text("Your Account Has Been Created!")

    

