from driver_interactions.ElementsInteractions import ElementsInteractions
from driver_interactions.InitDriver import InitDriver

import utilities.Logger as Logger
import urllib3
import time

log = Logger.func_logger()

def before_all(context):
    urllib3.disable_warnings()
    log.info("Script started")

def after_all(context):
    log.info("Script ended")

def before_scenario(context, scenario):
    context.prepare_driver = InitDriver()
    context.driver = context.prepare_driver.init_caps()
    ElementsInteractions(context.driver)

def after_scenario(context, scenario):
    time.sleep(5)
    context.driver.quit()
