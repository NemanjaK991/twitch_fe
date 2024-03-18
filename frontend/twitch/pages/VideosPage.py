from frontend.twitch.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class VideosPage(BasePage):

    def click_on_nth_tab_option(self, tab_position):
        live_video = (By.CSS_SELECTOR, 'img[class="tw-image"]')
        self.wait_for_element(live_video, visible=True)

        tab_btn = (By.CSS_SELECTOR, 'ul[role = "tablist"] li:nth-child({}) a'.format(tab_position))
        self.click_on_element(tab_btn)

        video = (By.CSS_SELECTOR, 'div[role="list"] div img')
        self.wait_for_element(video, visible=True)

    def scroll_videos_list(self, scroll_offset=0):
        el_loc = (By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 sc-9012bd00-1 lcptHf uJEBc"]')
        self.scroll_inside_element_by_offset(el_loc, vert_scroll=scroll_offset)

    def click_on_nth_video(self, video_num):
        video_locator = (By.CSS_SELECTOR, 'div[role="list"] div:nth-child({}) a'.format(video_num))
        self.click_on_element(video_locator)


