Feature: Run video

  @smoke
  Scenario: User wants to run a StarCraft video
    Given a user inputs the app url
    When a user inputs  StarCraft II value in the search input field
    And user clicks on the videos tab
    And user selects a video from the videos list
    Then the video execution is started
