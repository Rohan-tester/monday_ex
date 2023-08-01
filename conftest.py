import pytest
import allure
from selenium import webdriver



@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automation.credence.in")
    return driver


@pytest.fixture(params=[
    ("Credencetest@test.com", "Credence@123"),
    ("Credenctest@test.com", "Credence@123"),
    ("Credencetest@test.com", "Credence@13"),
    ("Credenctest@test.com", "Credence@12")
])
def getdata(request):
    return request.param