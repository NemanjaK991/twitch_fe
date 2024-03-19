from selenium.webdriver.common.by import By


class CommonLocators:
    page_title = (By.CSS_SELECTOR, '.navigate-left-title')


class HomePageLocators:
    search_btn = (By.CSS_SELECTOR, 'a[aria-label="Search"]')
    search_input_field = (By.CSS_SELECTOR, 'input[type="search"]')


class VideoExecutionLocators:
    profile_details = (By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 cEROUd"]')
    close_notification_btn = (By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 dwSJaB"] svg')
    video_locator = (By.CSS_SELECTOR, 'div[class="sc-6150ba6-0 etDpaL"] video')
    subscribers_msg = (By.CSS_SELECTOR, 'p[class*="sc-1txzju1-0 eDsrGf"]')


