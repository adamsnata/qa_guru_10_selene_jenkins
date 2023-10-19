import os

import allure
from selene import browser, be, have

import tests


class RegistrationPage:
    @allure.step("Open  main page")
    def open(self):
        browser.open('/automation-practice-form')
        browser.execute_script('document.querySelector("#fixedban").remove()')
        browser.element('footer').execute_script('element.remove()')

    @allure.step("Fill first name")
    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    @allure.step("Fill last name")
    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    @allure.step("Fill  email")
    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    @allure.step("Select gender")
    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    @allure.step("Fill user number")
    def fill_user_number(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    @allure.step("Fill  date of birth")
    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        with allure.step('fill month'):
            browser.element('.react-datepicker__month-select').send_keys(month)
        with allure.step('fill year'):
            browser.element('.react-datepicker__year-select').send_keys(year)
        with allure.step('fill day'):
            browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    @allure.step("Select subject")
    def select_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()

    @allure.step("Select hobbies")
    def select_hobbies(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    @allure.step("Upload picture")
    def upload_picture(self, value):
        browser.element("#uploadPicture").set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f'resources/{value}')
            )
        )

    @allure.step("Insert address")
    def insert_address(self, value):
        browser.element('#currentAddress').type(value)

    @allure.step("Select state")
    def select_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    @allure.step("Select city")
    def select_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    @allure.step("Submit")
    def submit(self):
        browser.element('#submit').press_enter()

    @allure.step("Check submitting the form")
    def check_submitting_the_form(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    @allure.step("Check input data")
    def check_input_data(self, first_name, last_name, email, gender,
                                                   number, date, subject, hobby,
                                                   picture, address, state, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts((f'{first_name} {last_name}', email, gender,
                                                   number,date, subject, hobby,
                                                   picture,
                                                   address, f'{state} {city}')))

    print("Выполнено успешно")
