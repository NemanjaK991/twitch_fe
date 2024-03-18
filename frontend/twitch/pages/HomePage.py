from twitch_fe.frontend.twitch.pages.BasePage import BasePage
from twitch_fe.frontend.twitch.pages.locators import HomePageLocators


class HomePage(BasePage):

    def click_on_search_btn(self):
        self.click_on_element(HomePageLocators.search_btn)

    def input_value_in_the_search_field(self, search_value):
        self.input_values(HomePageLocators.search_input_field, search_value, enter_btn=True)

        