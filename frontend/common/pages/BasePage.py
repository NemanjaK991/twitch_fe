from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class GenericBasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, element, visible=False, clickable=False, invisible=False, presence=False,
                         timeout_value=20):
        if visible:
            WebDriverWait(self.driver, timeout_value).until(
                EC.visibility_of_element_located(element)
            )
        elif clickable:
            WebDriverWait(self.driver, timeout_value).until(
                EC.element_to_be_clickable(element)
            )
        elif invisible:
            WebDriverWait(self.driver, timeout_value).until(
                EC.invisibility_of_element_located(element)
            )
        elif presence:
            WebDriverWait(self.driver, timeout_value).until(
                EC.presence_of_element_located(element)
            )
        else:
            pass  # additional wait

    def wait_for_element_default(self, element, ec, timeout_value=5, poll_frequency_value=0.5):
        try:
            WebDriverWait(self.driver, timeout_value, poll_frequency_value).until(ec(element))
        except TimeoutException as e:
            print(e)

    def click_on_element(self, element, js_click=False, action_click=False):
        self.wait_for_element(element, clickable=True)
        if action_click:
            action = ActionChains(self.driver)
            action.click(on_element=self.driver.find_element(*element))
            action.perform()
        elif js_click:
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element))
        else:
            self.driver.find_element(*element).click()

    def input_values(self, element, value, enter_btn=False):
        self.wait_for_element(element, visible=True)
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(value)
        if enter_btn:
            self.driver.find_element(*element).send_keys(Keys.ENTER)

    def scroll_inside_element_by_offset(self, el_locator, horiz_scroll=0, vert_scroll=0):
        element = self.driver.find_element(*el_locator)
        self.driver.execute_script("arguments[0].scrollBy({}, {});".format(horiz_scroll, vert_scroll), element)

    def return_text_from_element(self, element):
        self.wait_for_element(element, visible=True)
        return self.driver.find_element(*element).text

    def is_element_available(self, element, wait_time=2):
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located(element))
            return True
        except TimeoutException:
            return False




