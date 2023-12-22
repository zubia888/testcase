import random
import time
from faker import Faker
from Pages import RunCount
from Pages import RandomPassword
from Base import InitiateDriver
from Pages import RegistrationPage
from selenium.webdriver.support.wait import WebDriverWait

data = []
sheet_data = []


def test_find_elements():
    driver = InitiateDriver.start_browser()
    WebDriverWait(driver, 100)
    register = RegistrationPage.Registration(driver)
    fake = Faker()

    # Run Count
    count_run = str(RunCount.current_run_count)
    test_run = "Test Run: " + count_run
    data.append(test_run)
    sheet_data.append(count_run)

    # User Name
    random_name = fake.name()
    register.enter_username(random_name)
    user = "User Name: " + random_name
    data.append(user)
    sheet_data.append(random_name)

    # Email Address
    name = random_name.lower()
    name = name.replace(" ", ".")
    email_format = name + "@gmail.com"
    register.enter_email(email_format)
    email = "Email Address: " + email_format
    data.append(email)
    sheet_data.append(email_format)

    # Password
    pass_code = RandomPassword.password_generator()
    register.enter_password(pass_code)
    password = "Password: " + pass_code
    data.append(password)
    sheet_data.append(pass_code)

    # Confirm Password
    register.enter_confirm_password(pass_code)
    confirm_password = "Confirm Password: " + pass_code
    data.append(confirm_password)
    sheet_data.append(pass_code)

    # DOB
    month = random.randint(1, 11)
    if month == "2":
        date = str(random.randint(1, 28))
    else:
        if month % 2 == 0 and month <= 6:
            date = str(random.randint(1, 30))
        elif month % 2 != 0 and month <= 6:
            date = str(random.randint(1, 31))
        elif month % 2 == 0 and month <= 7:
            date = str(random.randint(1, 31))
        else:
            date = str(random.randint(1, 30))
    year = str(random.randint(1980, 2005))
    birthday = str(month) + "/" + date + "/" + year
    register.enter_dob(birthday)
    date_of_birth = "Date of Birth: " + birthday
    data.append(date_of_birth)
    sheet_data.append(birthday)

    # Save DOB
    register.save_dob()

    # Phone Number
    number = str(random.randint(3000000000, 3459999999))
    num = "0" + number
    register.enter_phone(num)
    phone = "Phone Number: " + num
    data.append(phone)
    sheet_data.append(num)

    # Address
    random_address = fake.address()
    register.enter_address(random_address)
    address = "Address: " + random_address
    data.append(address)
    sheet_data.append(random_address)

    # Address Type
    time.sleep(3)
    register.enter_address_type()

    # Gender
    gender_type = register.gender_name()
    gender = "Gender: " + gender_type.get_attribute('textContent')
    gender_ = gender_type.get_attribute('textContent')
    data.append(gender)
    sheet_data.append(gender_)

    # Country
    country_select = register.country_name()
    country = "Country: " + country_select.get_attribute('textContent')
    country_ = country_select.get_attribute('textContent')
    data.append(country)
    sheet_data.append(country_)
    time.sleep(5)

    # State
    state_select = register.state_name()
    state = "State: " + state_select.get_attribute('textContent')
    state_ = state_select.get_attribute('textContent')
    data.append(state)
    sheet_data.append(state_)
    time.sleep(5)

    # City
    city_select = register.city_name()
    city = "City: " + city_select.get_attribute('textContent')
    city_ = city_select.get_attribute('textContent')
    data.append(city)
    sheet_data.append(city_)

    # Zip Code
    postal = random_address.split()
    zip = postal[len(postal) - 1]
    register.zip_code(zip)
    zipCode = "Zip Code: " + zip
    data.append(zipCode)
    sheet_data.append(zip)

    # Terms & Conditions
    register.terms()

    # Date & Time
    date_time = InitiateDriver.date_time()
    data.append("Time: " + date_time)
    sheet_data.append(date_time)


def test_create_sheet():
    driver = InitiateDriver.create_sheet(sheet_data)


def test_save_data():
    driver = InitiateDriver.save_data(data)


def test_screenshot():
    driver = InitiateDriver.screen_shot()


def test_close():
    driver = InitiateDriver.close_browser()
