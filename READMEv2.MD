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

1. Start the inspector container by executing start.bat (for Windows) or start.sh (for Linux) in the terminal. These files are located in the /inspector directory and contain the commands to start the inspector container.
2. Build the runner Dockerfile by executing build.bat (for Windows) or build.sh (for Linux) in the terminal or command line. These files are located in the /runner/build directory and contain the commands to build the runner Dockerfile.

**Note**: `.bat` and `.sh` files are script files used to automate tasks in Windows and Linux systems respectively. They contain a series of command line instructions that are executed sequentially. Whenever you see these files mentioned in the instructions, remember that they are used to automate a series of command line tasks that can be kicked off in the terminal.

## Challenge

In this workshop, the challenge is to create and execute an automated browser test using Playwright, including API interactions. Participants will record, script, and run a test scenario, validating their ability to automate web application testing effectively.

## Instructions

1. **Record Steps**: Start by recording all the steps within the browser using the "record" feature in the Playwright's inspector tool window.
2. **Navigate and Interact**: Proceed to the web application in the newly opened browser window and interact with it according to the test scenario you want to automate. Stop the recording once you've finished navigating.
3. **Generate and Copy Code**: The inspector tool will generate code corresponding to your interactions. Copy this code and paste it into the `test_run.py` file located in the `/mount` directory.
4. **Run Test**: Finally, run the test scenario by executing the runner container using `start.bat` (for Windows) or `start.sh` (for Linux).

## Conclusion

By participating in this hands-on experience, you have gained knowledge in how to interact with the playwright automation test suite.

## Troubleshooting F.A.Q

### Windows

### Linux

```sh
    [pid=29][err] Authorization required, but no authorization protocol specified
  - [pid=29][err] [29:29:0607/122015.501614:ERROR:ozone_platform_x11.cc(244)] Missing X server or $DISPLAY
  - [pid=29][err] [29:29:0607/122015.501625:ERROR:env.cc(258)] The platform failed to initialize.  Exiting.
```

xhost local:docker
xhost +
