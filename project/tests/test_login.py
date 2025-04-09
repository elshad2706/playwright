from project.pages.login_page import LoginPage


def test_login_failure(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("incorrect_login","incorrect_password")
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


