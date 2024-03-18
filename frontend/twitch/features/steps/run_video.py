from behave import *
from twitch_fe.frontend.twitch.pages.HomePage import HomePage
from twitch_fe.frontend.twitch.pages.VideosPage import VideosPage
from twitch_fe.frontend.twitch.pages.VideoExecutionPage import VideoExecutionPage
from twitch_fe.frontend.twitch.data.constants import SS_PATH


@given(u'a user inputs the app url')
def step_impl(context):
    context.selenium_driver.get(context.link)
    context.home_page = HomePage(context.selenium_driver)
    context.videos_page = VideosPage(context.selenium_driver)
    context.video_execution_page = VideoExecutionPage(context.selenium_driver)


@when(u'a user inputs  StarCraft II value in the search input field')
def step_impl(context):
    context.home_page.click_on_search_btn()
    context.home_page.input_value_in_the_search_field('StarCraft II')


@when(u'user clicks on the videos tab')
def step_impl(context):
    context.videos_page.click_on_nth_tab_option(4)


@when(u'user selects a video from the videos list')
def step_impl(context):
    context.videos_page.scroll_videos_list(50)
    context.videos_page.scroll_videos_list(300)
    # time.sleep(1)
    context.videos_page.click_on_nth_video(5)


@then(u'the video execution is started')
def step_impl(context):
    # context.selenium_driver.get('https://m.twitch.tv/videos/2092779200')  # testing purpose -> mute modal
    context.video_execution_page.close_audio_muted_notification_if_it_is_shown()
    context.video_execution_page.wait_until_video_is_running()
    context.selenium_driver.save_screenshot(SS_PATH)
    # time.sleep(5)

# https://m.twitch.tv/videos/2092779200 -> testing purpose -> blocked content
# locator notifikacije div[class="Layout-sc-1xcs6mc-0 kpxuvv"]