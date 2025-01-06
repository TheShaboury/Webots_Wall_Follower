# Wall Follower Robot Simulation

## Description

This project implements a wall-following algorithm for a robot in the Webots simulation environment. The robot uses proximity sensors to detect walls and navigate through an environment by following walls on its left side.

The controller is written in Python and utilizes Webots' controller API to interact with the simulated robot and its sensors.

## Features

- Left wall following behavior
- Obstacle avoidance
- Utilizes 8 proximity sensors for environment detection
- Implements differential drive control

## Requirements

- Webots (R2023a or later recommended)
- Python 3.7 or higher

## Setup

1. Clone this repository to your local machine.
2. Open the Webots simulator.
3. Load the world file for this project (not provided in this repository).
4. Ensure the robot controller is set to `wall_follower_controller.py`.

## How it works

The robot controller performs the following steps:

1. Initializes the motors and proximity sensors.
2. Enters a main loop that runs for each simulation step.
3. Reads values from the proximity sensors.
4. Determines the presence of walls or obstacles.
5. Adjusts the robot's movement based on sensor readings:
   - If a front wall is detected, the robot turns right.
   - If a left wall is detected, the robot drives forward.
   - If no left wall is detected, the robot turns left to find a wall.
   - If the robot is too close to a left corner, it adjusts its path.
6. Sets the motor velocities based on the decision made.

## Customization

You can modify the following parameters in the `wall_follower_controller.py` file:

- `max_speed`: Maximum speed of the motors
- Sensor threshold values (currently set at 80)
- Motor speed ratios for different behaviors

## Contributing

Contributions to improve the wall-following algorithm or extend the functionality are welcome. Please fork the repository and submit a pull request with your changes.
