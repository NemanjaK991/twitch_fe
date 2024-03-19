import allure
from frontend.common.driver.driver_init import CustomDriver
from frontend.common.configuration.conf_reader import ConfReader
import logging
import datetime
from frontend.twitch.data.constants import CONF_FILE_PATH


def before_all(context):
    log_file_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    logging.basicConfig(level=logging.INFO, filename=r'frontend\twitch\logs\log{}.log'.format(log_file_name),
                        filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    context.conf_object = ConfReader(CONF_FILE_PATH)
    context.link = context.conf_object.get_url()
    context.browser = context.conf_object.get_browser()
    context.mobile_device = context.conf_object.mobile_device


def before_feature(context, feature):
    context.driver_object = CustomDriver(conf_file_path=CONF_FILE_PATH, browser=context.browser,
                                         headless=context.conf_object.headless_mode,
                                         mobile_emulator=True, mobile_device=context.mobile_device)
    context.selenium_driver = context.driver_object.return_driver()
    if not context.conf_object.headless_mode:
        context.selenium_driver.maximize_window()


def before_scenario(context, scenario):
    logging.info("Scenario: {}".format(scenario.name))


def after_scenario(context, scenario):
    if scenario.status == 'failed':
        allure.attach(context.selenium_driver.get_screenshot_as_png(), f"{scenario.name} - FAILED",
                      allure.attachment_type.PNG)


def after_feature(context, feature):
    context.selenium_driver.quit()
