from driver_interactions.ElementsInteractions import ElementsInteractions

import time


class MainPage(ElementsInteractions):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    name_activity_main = ".MainActivity"

    def verify_main_activity(self):
        self.verify_activity(self.name_activity_main)
        time.sleep(5)
