# robotics test github repository

This github is for experimentation on ros and development of prototype robotics system.

## ROS Installation

Follow [ROS Installation](http://wiki.ros.org/ROS/Installation) based on your operating system.

## Usage

Clone the repository into the desired directionary and build the directory with following commands.

```bash
cd robot
# Initialize ros if its not already in .bashrc
source /opt/ros/melodic/setup.bash (ububtu 18)
source /opt/ros/kinetic/setup.bash (ububtu 16)
catkin_make
```

Run the following to start simulation and move the robot.

Note that each of the roslaunch and rosrun command will require new terminal to run.

Each terminal the ros and catkin workspace will need to be Initialized.

```bash
# Initialize ros if its not already in .bashrc
source /opt/ros/melodic/setup.bash
# Initialize the current catkin workspace
source devel/setup.bash
# Start Gazebo simulation
roslaunch sample_hexapod_robot gazebo.launch
# Start ROS to Gazebo joint controller
roslaunch sample_hexapod_controller sample_hexapod_controller.launch
# Run the joint publisher to control the robot in Gazebo to move
rosrun test_joint_pub publisher.py
```
