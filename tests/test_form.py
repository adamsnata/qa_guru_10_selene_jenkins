import os

import allure
from allure_commons.types import Severity
from selene import browser
from selene.support.conditions import have, be

from qa_guru.pages.registration_form import RegistrationPage



@allure.tag('web')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'aksana')
@allure.feature('Allure')
@allure.story('Allure with steps')
def test_form_submission(setup_browser):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('test_name')
    registration_page.fill_last_name('test_lastName')
    registration_page.fill_email('test@mail.com')
    registration_page.select_gender('Male')
    registration_page.fill_user_number('1234567890')
    registration_page.fill_date_of_birth('01', 'January', '1999')
    registration_page.select_subject('Maths')
    registration_page.select_hobbies('Music')
    registration_page.upload_picture('cat.png')
    registration_page.insert_address("test")
    registration_page.select_state('ncr')
    registration_page.select_city('delhi')
    registration_page.submit()
    registration_page.check_submitting_the_form()
    registration_page.check_input_data('test_name', 'test_lastName', 'test@mail.com', 'Male',
                                               '1234567890', '01 January,1999', 'Maths', 'Music',
                                                'cat.png','test', 'NCR', 'Delhi')


    # #open
    # browser.open('/automation-practice-form')
    # browser.execute_script('document.querySelector("#fixedban").remove()')
    # browser.element('footer').execute_script('element.remove()')
    # #fill_first_name
    # browser.element('#firstName').should(be.blank).type('test_name')
    # #fill_last_name
    # browser.element('#lastName').should(be.blank).type('test_lastName')
    # #fill_email
    # browser.element('#userEmail').should(be.blank).type('test@mail.com')
    # #select_gender
    # browser.element('[for="gender-radio-1"]').click()
    # #fill_user_number
    # browser.element('#userNumber').should(be.blank).type('1234567890')
    # #fill_date_of_birth
    # browser.element('#dateOfBirthInput').click()
    # browser.element(".react-datepicker__month-select>option[value='1']").click()
    # browser.element(".react-datepicker__year-select>option[value='1999']").click()
    # browser.element('.react-datepicker__day--019').click()
    # #select_subject
    # browser.element('#subjectsInput').should(be.blank).type('Maths').press_enter()
    # #select_hobbies
    # browser.element("[for='hobbies-checkbox-3']").click()
    # #upload_picture
    # browser.element('#uploadPicture').send_keys(os.path.abspath('resources/cat.png'))
    # #insert_address
    # browser.element('#currentAddress').type("test")
    # #select_state
    # browser.element('#react-select-3-input').type('ncr').press_enter()
    # #select_city
    # browser.element('#react-select-4-input').type('delhi').press_enter()
    # #submit
    # browser.element('#submit').press_enter()
    # #check_submitting_the_form
    # browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    # #check_input_data
    # browser.element('.table').should(have.text('test_name test_lastName' and 'test@mail.com' and 'Male' and
    #                                            '1234567890' and '1 January,1999' and 'Maths' and 'Music' and
    #                                            'cat.png' and
    #                                            'test' and 'NCR Delhi'))
    print("Выполнено успешно")