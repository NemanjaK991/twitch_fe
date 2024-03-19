# Python Automation Project

This project demonstrates automated testing using Python.

## Project Setup

1. Clone the repository:

```
git clone https://github.com/NemanjaK991/twitch_fe.git
```

2. Navigate to the project directory:

```
cd twitch_fe
```

3. Install the required dependencies:

```
pip install -r frontend\requirements.txt
```

## Running Tests

This project uses Behave for behavior-driven development (BDD) testing. To run the tests, follow these steps:

1. Navigate to the project root directory (twitch_fe):

```
cd twitch_fe
```

2. Run Behave:

```
behave frontend\twitch\features\run_video.feature
```

This command will execute all tests in the run_video.feature file.

## Additional Information

- `frontend\twitch\features`: Contains feature files written in Gherkin syntax.
- `frontend\twitch\features\steps`: Contains step definitions for the feature files.
- `requirements.txt`: Contains a list of Python dependencies required for this project.
- `README.md`: This file, containing project information and instructions.

![Demo GIF](demo.gif)