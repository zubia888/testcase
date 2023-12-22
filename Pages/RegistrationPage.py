import random
from Library import ConfigFileReader
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Registration:

    def __init__(self, obj):
        global driver
        driver = obj
        data = []

    def enter_username(self, username):
        user_name = driver.find_element(By.NAME, ConfigFileReader.fetchElements('Registration', 'user_name'))
        user_name.send_keys(username)

    def enter_email(self, email):
        user_email = driver.find_element(By.NAME, ConfigFileReader.fetchElements('Registration', 'email'))
        user_email.send_keys(email)

    def enter_password(self, password):
        password_code = driver.find_element(By.NAME, ConfigFileReader.fetchElements('Registration', 'password'))
        password_code.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        cpassword = driver.find_element(By.NAME, ConfigFileReader.fetchElements('Registration', 'confirm_password'))
        cpassword.send_keys(confirm_password)

    def enter_dob(self, dob):
        date = driver.find_element(By.ID, ConfigFileReader.fetchElements('Registration', 'dob'))
        date.send_keys(dob)

    def save_dob(self):
        driver.find_element(By.CLASS_NAME, ConfigFileReader.fetchElements('Registration', 'save_date')).click()

    def enter_phone(self, phone):
        phone_number = driver.find_element(By.NAME, ConfigFileReader.fetchElements('Registration', 'phone'))
        phone_number.send_keys(phone)

    def enter_address(self, address):
        full_address = driver.find_element(By.NAME, ConfigFileReader.fetchElements('Registration', 'address'))
        full_address.send_keys(address)

    def enter_address_type(self):
        type = driver.find_element(By.CSS_SELECTOR, ConfigFileReader.fetchElements("Registration", "address_type"))
        type.click()

    def gender_name(self):
        gender_name = driver.find_element(By.NAME, ConfigFileReader.fetchElements('Registration', 'gender_name'))
        gender = Select(gender_name)
        options = gender.options
        random_index = random.randint(1, len(options) - 1)
        gender.select_by_index(random_index)
        gender_select = gender.first_selected_option
        return gender_select

    def country_name(self):
        country = driver.find_element(By.ID, ConfigFileReader.fetchElements('Registration', 'country'))
        country = Select(country)
        options = country.options
        random_index = random.randint(1, len(options) - 1)
        country.select_by_index(random_index)
        country_select = country.first_selected_option
        return country_select

    def state_name(self):
        global state_select
        state = driver.find_element(By.ID, ConfigFileReader.fetchElements('Registration', 'state'))
        state = Select(state)
        options = state.options
        random_index = random.randint(1, len(options) - 1)
        state.select_by_index(random_index)
        state_select = state.first_selected_option
        return state_select

    def city_name(self):
        city = driver.find_element(By.ID, ConfigFileReader.fetchElements('Registration', 'city'))
        city = Select(city)
        try:
            options = city.options
            random_index = random.randint(1, len(options) - 1)
            print(random_index)
            city.select_by_index(random_index)
            city_select = city.first_selected_option
        except:
            city_select = state_select
        return city_select

    def zip_code(self, zip):
        zipCode = driver.find_element(By.NAME, ConfigFileReader.fetchElements('Registration', 'zip_code'))
        zipCode.send_keys(zip)

    def terms(self):
        terms = driver.find_element(By.NAME, ConfigFileReader.fetchElements('Registration', 'terms'))
        terms.click()


