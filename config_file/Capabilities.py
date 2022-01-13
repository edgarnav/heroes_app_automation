android_desired_caps = caps = {}
caps['platformName'] = 'Android'
caps['browserName'] = 'Chrome'
caps['appium:deviceName'] = 'Samsung Galaxy S6 GoogleAPI Emulator'
caps['appium:platformVersion'] = '8.0'
caps['extendedDebugging'] = True
caps['capturePerformance'] = True
caps['sauce:options'] = {}
caps['sauce:options']['appiumVersion'] = '1.20.2'
ios_desired_caps = {'platformVersion': '14.3', 'deviceName': 'iPhone 11 Pro', 'platformName': 'IOS',
                    'automationName': 'XCUITest', "app": "com.coppel.CoppelApp", 'noReset': 'true',
                    'autoGrantPermissions': 'true'}