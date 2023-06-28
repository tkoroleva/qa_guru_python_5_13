"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser


@pytest.fixture(params=[(1980, 1080), (1600, 900), (320, 480), (480, 800)])
def browser_size(request):
    size = request.param
    browser.open()
    browser.driver.set_window_size(size[0], size[1])
    if size[0] > 1000:
        platform = 'desktop'
    else:
        platform = 'mobile'

    yield browser, platform

    browser.quit()


def test_github_desktop(browser_size):
    size = browser_size[1]
    if size == 'mobile':
        pytest.skip('Данное разрешение не подходит для мобильного устройства')
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_size):
    size = browser_size[1]
    if size == 'desktop':
        pytest.skip('Данное разрешение не подходит для десктопного устройства')
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
