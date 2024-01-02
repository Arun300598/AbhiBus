import allure
from allure_commons.types import AttachmentType


def after_scenario(context, scenario, webdriver):
    context.driver = webdriver.Chrome()
    context.driver.get(
        "https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python")
    context.driver.delete_all_cookies()
    context.driver.maximize_window()
    if scenario.status == "failed":

        allure.attach(context.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

