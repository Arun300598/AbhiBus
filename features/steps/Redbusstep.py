import sys
import time

import allure
from allure_commons.types import AttachmentType
from behave import *
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'Launch the chrome Browser')
def launchbrowser(context):
    #context.driver = webdriver.Chrome(executable_path='C:\\Users\\Arun\\Downloads\\chromedriver-win64\\chromedriver.exe')
    context.driver=webdriver.Chrome()

@when(u'Open Abhibus page')
def openhomepage(context):
    context.driver.get("https://www.abhibus.com/")
    context.driver.delete_all_cookies()
    context.driver.maximize_window()


@then(u'Verify the title of webpage')
def verifytitle(context):
    title=context.driver.title
    print(title)
    assert "Book Bus Tickets Online at Lowest Fare, Upto ₹350 Cashback On Bus Booking | AbhiBus" in title

@then(u'close the browser')
def closebrowser(context):
    context.driver.close()

@when(u'Enter from "{From}" and To "{To}"')
def enterfromandtostation(context,From,To):
    context.driver.find_element(By.XPATH, "//input[@placeholder='To Station']").send_keys(To)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@placeholder='To Station']").send_keys(Keys.RETURN)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@placeholder='From Station']").send_keys(From)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@placeholder='From Station']").send_keys(Keys.RETURN)


@when(u'click today button and click search')
def step_impl(context):
     context.driver.find_element(By.XPATH, "//a[text()='Search']").click()


@when(u'search for bus name "{Busname}"')
def step_impl(context, Busname):
    context.element_locator="((//h5[text()='{}'])[1]/ancestor::div)[11]/following-sibling::div/div/div/div/strong/span".format(Busname)
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, context.element_locator)))
    context.l = context.driver.find_element(By.XPATH, context.element_locator).text



@then(u'verify the bus fare as "{Busfare}"')
def step_impl(context,Busfare):
    assert context.l in Busfare




