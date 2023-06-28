"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser


@pytest.fixture(params=[(1980, 1080), (1600, 900)])
def browser_desktop_size(request):
    size = request.param
    browser.open()
    browser.driver.set_window_size(size[0], size[1])

    yield browser

    browser.quit()


@pytest.fixture(params=[(320, 480), (480, 800)])
def browser_mobile_size(request):
    size = request.param
    browser.open()
    browser.driver.set_window_size(size[0], size[1])

    yield browser

    browser.quit()


def test_github_desktop(browser_desktop_size):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_mobile_size):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
