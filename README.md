# test_automation_setup

This repository contains a challenge to help you start learning about automation testing concepts and test development using [Playwright](https://playwright.dev/).

The goal for this challenge is to get you familiar with developing test cases in Playwright.
One of the key objectives is to facilitate the onboarding process for team members joining the testing team.
It also helps to share the team knowledge with stakeholders involved in the same testing project.

This challenge is open to anyone with basic IT knowledge, regardless of whether they have prior experience in testing.

## Environment

1. **Inspector**: This is a container that includes the Playwright packages required to run a web browser and the inspector tool for creating the tests.
2. **Runner**: This is a container that will run the tests you have made with the inspector tool. It will run them from a volume mount at `/mount/test_run.py`

## Getting Started

To get started with this challenge, you need to have the below prerequisites:

- Visual Studio Code (VSCode)
- Docker or Podman packages equivalent.

Once you have these prerequisites, you can clone this repository and start the containers with the following steps.

1. Start the inspector container with start.bat on Windows or start.sh on Linux in the `/inspector` directory.
2. Build the runner Dockerfile with build.bat on Windows or build.sh on Linux in the `/runner/build` directory.

## Challenge

1. Start recording all steps within the browser by pressing "record" in the inspector tool window
2. Go to the application in the browser window that has opened
3. Go through the application test scenario step by step
4. Copy the code that the inspector generated and paste it in the test_run.py file in /mount
5. Run the runner container with start.bat on Windows or start.sh on Linux

## Instructions

## Conclusion

By participating in this hands-on experience, you have gained knowledge in how to interact with the playwright automation test suite.

## Troubleshooting F.A.Q

## Recommended extensions

### Windows

### Linux

```sh
    [pid=29][err] Authorization required, but no authorization protocol specified
  - [pid=29][err] [29:29:0607/122015.501614:ERROR:ozone_platform_x11.cc(244)] Missing X server or $DISPLAY
  - [pid=29][err] [29:29:0607/122015.501625:ERROR:env.cc(258)] The platform failed to initialize.  Exiting.
```

xhost local:docker
xhost +
source .venv/bin/activate && pip install Appium-Python-Client pytest-playwright && playwright install --with-deps