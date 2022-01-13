from appium import webdriver
import config_file.Capabilities as Caps
import config_file.ConfigFile as Configs


class InitDriver:

    @staticmethod
    def init_caps():
        if Configs.platform == "Android":
            url = "http://127.0.0.1:4723/wd/hub"
            return webdriver.Remote(url, Caps.android_desired_caps, keep_alive=True)
        else:
            return webdriver.Remote('http://127.0.0.1:4723/wd/hub', Caps.ios_desired_caps)
