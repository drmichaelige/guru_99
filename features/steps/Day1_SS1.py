from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


USERID = (By.CSS_SELECTOR, 'input[type = text')
PASSWORD = (By.CSS_SELECTOR, 'input[type = password')
LOGIN = (By.CSS_SELECTOR, 'input[value = LOGIN')
LOGIN_SUCCESS = (By.CSS_SELECTOR, "marquee.heading3")


@given('Open Demoguru99 page')
def open_demoguru99_page(context):
     context.driver.get('https://www.demo.guru99.com/V4/')


@when('Input text Userid {text}')
def input_text_userid(context, text):
    context.driver.find_element(*USERID).send_keys(text)


@when('Input text Password {text}')
def input_text_password(context, text):
    context.driver.find_element(*PASSWORD).send_keys(text)


@when('Click Login')
def click_login(context):
    context.driver.find_element(*LOGIN).click()


@then('Verify the output')
def verify_the_output(context):
    context.driver.find_element(*LOGIN_SUCCESS)
    expected_result = "Welcome To Manager's Page of Guru99 Bank"
    actual_result = context.driver.find_element(*LOGIN_SUCCESS).text
    print(expected_result)
    print(actual_result)
    assert expected_result == actual_result, f'Error! Actual text {actual_result} did not match expected {expected_result}'

    print(actual_result)