from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
import pytest

def open_link(link:str) -> None:
    
    browser = webdriver.Chrome()
    browser.get(link) 



# Задание: параметризация тестов
# Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать
#  несколько url-адресов задач, где появляются кусочки сообщений.
#  Ваша задача — реализовать автотест со следующим сценарием действий: 


def resolve(link:str) -> None:
    
# открыть страницу 
    browser = webdriver.Chrome()
    browser.get(link) 
    
def logOut(browser):
    try:
        loginButton=browser.find_element(By.XPATH, '//*[@id="ember872"]/li[6]/button')
        loginButton.click()
    except:
        print('Logout button was not located')
        

def execute_test(link:str):
    link="https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link) 
    time.sleep(6)
    logOut(browser)
    time.sleep(6)

    # авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
        #найти форму ввода логина и пароля
    exButton=browser.find_element(By.ID,"ember33")
    exButton.click()
    time.sleep(2)

        #ввести логин и паоль
    loginField=browser.find_element(By.ID,"id_login_email")
    loginField.send_keys("derbilla@mail.ru")

    passwordField=browser.find_element(By.ID,"id_login_password")
    passwordField.send_keys("8026921aA")

    #найти кнопку входа 
    loginButton=browser.find_element(By.CLASS_NAME, "sign-form__btn")
    #нажать кнопку входи
    loginButton.click()
    time.sleep(12)


    #browser.quit()

    # найти поле ввода
    # очистить поле ввода
    # ввести правильный ответ (поле перед вводом должно быть пустым)

    #string-quiz__textarea
    try:
        answer = math.log(int(time.time()))
        answerField=browser.find_element(By.CLASS_NAME,"string-quiz__textarea")
        answerField.send_keys(answer)

        answerButton=browser.find_element(By.CLASS_NAME,"submit-submission")

        browser.execute_script('arguments[0].removeAttribute("disabled");', answerButton)
        answerButton.click()
    except:
        print("Answer located")

    time.sleep(4)
    
    # найти поле COrrect   
    resultValueLabel=browser.find_element(By.CLASS_NAME,"smart-hints__hint")
    #Считать его текстовое значение
    resultValue = resultValueLabel.text
    if(resultValue == "Correct!"):
        return True
    else:
        return False    
   

lesson_ids = ('236895', '236896', '236897', '236898', '236899',
                        '236903', '236904', '236905')

@pytest.mark.parametrize('lesson_ids', lesson_ids)
def test_selenium_3_6_3(lesson_ids):
    link = (f'https://stepik.org/lesson/{lesson_ids}/step/1')
    result = execute_test(link)
    assert result


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number_list', ["lesson_ids"])#Создаем фикстуру параметриз('переменная', ["урлы"]
class Test_login():# Создаем класс, название с Test..

    lesson_ids = ('236895', '236896', '236897', 
                  '236898', '236899',
                  '236903', '236904', '236905')
    
    def test_guest_should_see_login_link(self,browser, number_list):
        answer = math.log(int(time.time()))# Создаем переменную
        browser.get(f"http://selenium1py.pythonanywhere.com/{number_list}/step/1")
        browser.implicity_wait(10)# Добавляем явное ожидание

        #send_keys(), он принимает только строки, а не числа)
        #переводим время в строку)
        browser.find_element(By.CSS_SELECTOR, '.textarea').send_keys(str(answer))
        # находим класс кнопку answerButton и нажимаем
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        #Через WebDriverWait EC.visibility_of_element_located().text 
        #находим класс сообщения и текст его присваиваем переменной
        result = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        #Проверяем не равен ли он !="Correct!"
        assert result == 'Correct!', result
        # этот тест запустится 8 раза
         # assert 'Correct!' == text, f'Ожидаемое значение <Correct!>, фактическое значение <<{text}>>'
        assert result == 'Correct!', result
    # assert 'Correct!' == result, f'Ожидаемое значение <Correct!>, фактическое значение <<{text}>>'


    if __name__ == "__main__":
        pytest.main()


    