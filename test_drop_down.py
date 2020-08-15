from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from variables_and_locators.variables_and_locators import *
from selenium.webdriver.common.action_chains import ActionChains
import time

#initializing browser

@pytest.fixture(scope="module")
def start_browser():

    global driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    global wait
    wait = WebDriverWait(driver, 20)
    yield
    driver.quit()

# nvavigating to site

@pytest.fixture(scope="function")
def navigate_to_site():
    driver.get("https://www.gulftalent.com/")


@pytest.mark.usefixtures("start_browser","navigate_to_site")
def test_salaries():

    salaries = driver.find_element_by_xpath("//li[contains(@class,'dropdown section-salaries sub-menu-parent')]")
    Action = ActionChains(driver)
    Action.move_to_element(salaries)
    Action.perform()

    view_more_categories = "//div[contains(@class,'col-sm-13')]//a[contains(text(),'View More Categories')]"
    wait.until(EC.visibility_of_element_located((By.XPATH,view_more_categories)))
    driver.find_element_by_xpath(view_more_categories).click()
    wait.until(EC.title_is(view_more_categories_page_title))
    time.sleep(3)
    assert driver.title == view_more_categories_page_title
