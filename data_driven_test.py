from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from variables_and_locators.variables_and_locators import *


#initializing browser

@pytest.fixture(scope="module")
def start_browser():

    global driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()

# nvavigating to site

@pytest.fixture(scope="function")
def navigate_to_site():
    driver.get("https://www.gulftalent.com/")

# testing the website title when user enter different jobs in search box

@pytest.mark.parametrize("job",jobs)
@pytest.mark.usefixtures("start_browser","navigate_to_site")
def test_textbox(job):

    driver.find_element_by_xpath(search_box).send_keys(job)
    wait = WebDriverWait(driver,20)
    wait.until(EC.text_to_be_present_in_element_value((By.XPATH,search_box),job))
    driver.find_element_by_xpath(search_button).click()
    wait.until(EC.title_is(expected_title))
    assert driver.title == expected_title
