from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import math
import time



lesson_ids = ('236895', '236896', '236897', '236898', '236899',
                        '236903', '236904', '236905')


@pytest.fixture(scope='session')
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson_ids', lesson_ids)
def test_selenium_3_6_3(browser, lesson_ids):
    answer = math.log(int(time.time()))
    browser.get(f'https://stepik.org/lesson/{lesson_ids}/step/1')
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, '.textarea').send_keys(str(answer))
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    result = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text

    assert result == 'Correct!', result
    # assert 'Correct!' == result, f'Ожидаемое значение <Correct!>, фактическое значение <<{text}>>'

    try:
        assert 'Correct!' == result, f'Ожидаемое значение <Correct!>, фактическое значение <<{text}>>'
    except AssertionError:
        final += result  # собираю ответ каждой ошибки

def test_final_text():
    print(f'\n\nПредложение: {final}')


