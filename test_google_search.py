import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture
def full_screen_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('https://google.com')
    yield
    print("\nТут могла быть Ваша реклама")
    browser.quit()


def test_search_in_google(full_screen_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_unhappy_search_in_google(full_screen_browser):
    search_request = "nothingfoundinthissearchandiwillbehappy"
    browser.element('[name="q"]').should(be.blank).type(search_request).press_enter()
    browser.element('[id="botstuff"]').should(
        have.text('По запросу ' + search_request + ' ничего не найдено.'))
