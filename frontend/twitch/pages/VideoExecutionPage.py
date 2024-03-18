import time

from frontend.twitch.pages.BasePage import BasePage
from frontend.twitch.pages.locators import VideoExecutionLocators


class VideoExecutionPage(BasePage):

    def wait_until_profile_details_are_shown(self):
        self.wait_for_element(VideoExecutionLocators.profile_details)

    def close_audio_muted_notification_if_it_is_shown(self):
        self.wait_until_profile_details_are_shown()
        if len(self.driver.find_elements(*VideoExecutionLocators.close_notification_btn)) > 0:
            self.click_on_element(VideoExecutionLocators.close_notification_btn)

    def wait_until_video_is_running(self):
        counter = 0
        self.wait_for_element(VideoExecutionLocators.video_locator, visible=True)
        video_element = self.driver.find_element(*VideoExecutionLocators.video_locator)
        while self.driver.execute_script("return arguments[0].paused;",
                                         video_element):
            time.sleep(0.5)

            counter += 0.5
            if counter == 5:
                break
