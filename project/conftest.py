import pytest
from project.pages.login_page import LoginPage
from project.pages.dashboard_page import DashboardPage


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)
