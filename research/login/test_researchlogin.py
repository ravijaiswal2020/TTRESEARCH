import time

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup WebDriver with incognito mode
@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")  # Add incognito mode
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()



@allure.title("tc1")
@allure.description("login with invalid credentials")
@pytest.mark.test_login1
@pytest.mark.title("login_with_invalid_credentials")
@pytest.mark.negative
def test_login1(driver):
    driver.get("https://www.taxmann.com/gp/auth/login")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@class='tab-links']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']").send_keys("cog.testing202@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Ravi@123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//span[@class='checkmark']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@aria-label='Sign In']").click()
    assert driver.current_url == "https://www.taxmann.com/gp/auth/login"
    time.sleep(4)


@allure.title("tc2")
@allure.description("login with valid credentials")
@pytest.mark.research
@pytest.mark.test_login2
@pytest.mark.title("login_with_valid_credentials")
@pytest.mark.positive
def test_login2(driver):
    driver.get("https://www.taxmann.com/gp/auth/login")
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@class='tab-links']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Email']").send_keys("cog.testing2021+50@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").clear()
    driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys("Ravi@123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@aria-label='Sign In']").click()
    time.sleep(4)
    assert driver.current_url == "https://www.taxmann.com/research"
    time.sleep(3)

    print(driver.current_url)
