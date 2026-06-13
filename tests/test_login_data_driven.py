import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from playwright.sync_api import expect
from config import Config
from utilis.data_reader_util import read_json_data, read_csv_data, read_excel_data
import time

csv_data = read_csv_data("testdata/logindata.csv")


@pytest.mark.parametrize("testName,email,password,expected", csv_data)
def test_login_data_driven(page, testName, email, password, expected):

    home_page = HomePage(page)
    login_page = LoginPage(page)
    my_account_page = MyAccountPage(page)

    home_page.click_my_account()
    home_page.click_login()

    login_page.login(email, password)
    time.sleep(3)

    if expected == "success":
        expect(my_account_page.get_my_account_page_heading()).to_be_visible(
            timeout=3000
        )

    else:
        expect(login_page.get_login_error()).to_be_visible(timeout=3000)
