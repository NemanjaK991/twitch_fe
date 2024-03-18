from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CustomDriver:

    def __init__(self, conf_file_path, browser=None, headless=False, mobile_emulator=False,
                 arguments=('disable-gpu', 'no-sandbox', 'headless',
                            'window-size=1920x1080')):

        if headless:
            options = Options()
            for argument in arguments:
                options.add_argument(f"--{argument}")
            if mobile_emulator:
                device_name = 'iPhone X'
                options.add_experimental_option('mobileEmulation', {'deviceName': device_name})

        else:
            options = None

            if mobile_emulator:
                options = Options()
                device_name = 'iPhone X'
                options.add_experimental_option('mobileEmulation', {'deviceName': device_name})

        if browser == 'Chrome' or browser is None:
            self.selenium_driver = webdriver.Chrome(options=options)
        elif browser == 'Firefox':
            self.selenium_driver = webdriver.Firefox(options=options)
        elif browser == 'Edge':
            self.selenium_driver = webdriver.Edge(options=options)

        self.conf_file_path = conf_file_path

    def return_driver(self):
        return self.selenium_driver

