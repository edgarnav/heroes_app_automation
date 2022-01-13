from traceback import print_stack

from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction

import config_file.Constants as Constants
import config_file.ConfigFile as ConfigFile
import utilities.Logger as Log
import allure
import time


class ElementsInteractions:

    log = Log.func_logger()

    def __init__(self, driver):
        self.driver = driver

    def locator(self, locator_type):
        if locator_type == "id" and ConfigFile.platform == "Android":
            return By.ID
        elif locator_type == "id" and ConfigFile.platform == "iOS":
            return By.NAME
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "tag":
            return By.TAG_NAME
        else:
            self.log.error("Locator Type : " + locator_type + " entered is not found")
        return False

    def verify_activity(self, activity_name):
        cont_max_time = 0
        while cont_max_time > 10:
            time.sleep(1)
            cont_max_time += 1
            if activity_name == self.driver.current_activity:
                self.log.info("Activity name match with: " + activity_name)
                break
            elif activity_name != self.driver.current_activity and cont_max_time == 10:
                self.take_screenshot(self.driver.activity_name)
                self.log.info("Activity name expected: " + activity_name)
                assert False

    def explicit_wait(self, locator_value, locator_type, max_time):
        try:
            locator_by_type = self.locator(locator_type)
            WebDriverWait(self.driver, max_time).until(ec.presence_of_all_elements_located((locator_by_type, locator_value)))
            self.log.info(Constants.found_locator + locator_value + Constants.locator_type + locator_by_type)
            return True
        except Exception:
            self.log.error(Constants.not_found_locator + locator_value + Constants.locator_type + locator_type)
            return False

    def get_element(self, locator_value, locator_type):
        element = None
        try:
            locator_by_type = self.locator(locator_type)
            element = self.driver.find_element(locator_by_type, locator_value)
            self.log.info(Constants.found_locator + locator_value + Constants.locator_type + locator_by_type)
        except Exception:
            self.log.error(Constants.not_found_locator + locator_value + Constants.locator_type + locator_type)
            print_stack()
        return element

    def press_element(self, locator_value, locator_type):
        try:
            element = self.wait_element(locator_value, locator_type)
            element.click()
            self.log.info(" Clicked on element with locator value " + locator_value + Constants.locator_type + locator_type)
        except Exception:
            self.log.error(" Unable to Click on element with locator value " + locator_value + Constants.locator_type + locator_type)
            print_stack()
            assert False

    def double_click_element(self, locator_value, locator_type):
        try:
            element = self.wait_element(locator_value, locator_type)
            action = ActionChains(self.driver)
            action.double_click(element)
            self.log.info(" Clicked on element with locator value " + locator_value + Constants.locator_type + locator_type)
        except Exception:
            self.log.error(" Unable to Click on element with locator value " + locator_value + Constants.locator_type + locator_type)
            print_stack()
            assert False

    def send_text(self, locator_value, locator_type, text):
        try:
            element = self.wait_element(locator_value, locator_type)
            element.send_keys(text)
            self.log.info( " Sent the text " + text + Constants.in_locator + locator_value + Constants.locator_type + locator_type)
        except Exception:
            self.log.error(" Unable to Sent the text " + text + Constants.in_locator + locator_value + Constants.locator_type + locator_type)
            print_stack()
            self.take_screenshot(locator_type)
            assert False

    def get_text(self, locator_value, locator_type):
        element_text = None
        try:
            element = self.wait_element(locator_value, locator_type)
            element_text = element.text
            self.log.info(" Got the text " + element_text + Constants.from_locator + locator_value + Constants.locator_type + locator_type)
        except Exception:
            self.log.error(" Unable to get the text from element with locator value " + locator_value + Constants.locator_type + locator_type)
            print_stack()
        return element_text

    def clear_text_filed(self, locator_value, locator_type):
        try:
            element = self.wait_element(locator_value, locator_type)
            element.clear()
            self.log.info( " Erased text in" + Constants.in_locator + locator_value + Constants.locator_type + locator_type)
        except Exception:
            self.log.error(" Unable to erase text " + Constants.in_locator + locator_value + Constants.locator_type + locator_type)
            print_stack()
            self.take_screenshot(locator_type)
            assert False

    def get_attribute(self, locator_value, locator_type, attribute_name):
        attribute = None
        try:
            element = self.wait_element(locator_value, locator_type)
            attribute = element.get_attribute(attribute_name)
            self.log.info(" Got the attribute " + attribute_name + " -> " + attribute + Constants.from_locator + locator_value + Constants.locator_type + locator_type)
        except Exception:
            self.log.error(" Unable to get the attribute " + attribute_name + Constants.from_locator + locator_value + Constants.locator_type + locator_type)
            print_stack()
        return attribute

    def is_element_displayed(self, locator_value, locator_type):
        element_displayed = None
        try:
            element = self.wait_element(locator_value, locator_type)
            element_displayed = element.is_displayed()
            self.log.info(" Element is Displayed on web page with locator value " + locator_value + Constants.locator_type + locator_type)
        except Exception:
            self.log.error(" Element is not Displayed on web page with locator value " + locator_value + Constants.locator_type + locator_type)
            print_stack()
        return element_displayed

    def get_all_elements(self, locator_value, locator_type):
        elements = None
        try:
            self.wait_element(locator_value, locator_type)
            locator_by_type = self.locator(locator_type)
            elements = self.driver.find_elements(locator_by_type, locator_value)
            self.log.info(" Elements found with locator " + locator_value + Constants.locator_type + locator_by_type)
        except Exception:
            self.log.error(" Elements not found with locator " + locator_value + Constants.locator_type + locator_type)
            print_stack()
        return elements

    def scroll_to_element(self, locator_value, locator_type):
        action = TouchAction(self.driver)
        locator_by_type = self.locator(locator_type)
        try:
            element = self.driver.find_element(locator_by_type, locator_value)
            found_element = element.is_displayed()
        except Exception:
            found_element = False
        while not found_element:
            action.press(x = 200, y = 600).wait(500).move_to(x = 207, y = 300).release().perform()
            time.sleep(0.3)
            try:
                element = self.driver.find_element(locator_by_type, locator_value)
                found_element = element.is_displayed()
            except Exception:
                found_element = False
        return True

    def wait_element(self, locator_value, locator_type):
        try:
            locator_by_type = self.locator(locator_type)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            element = wait.until(ec.presence_of_element_located((locator_by_type, locator_value)))
            self.log.info(Constants.found_locator + locator_value + Constants.locator_type + locator_type)
        except Exception:
            self.log.error(Constants.not_found_locator + locator_value + Constants.locator_type + locator_type)
            print_stack()
            self.take_screenshot(locator_type)
            assert False
        return element

    def take_screenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)
