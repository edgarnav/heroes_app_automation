import inspect
import logging
import allure


def func_logger():

    log_name = inspect.stack()[1][3]
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler("../HeroesAppAutomation/reports/ScriptLog.log")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def allure_log(text):
    with allure.step(text):
        pass
