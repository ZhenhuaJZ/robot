search_mode=OPTIMIZE_MAX_JOINT
srdf_filename=doggo_robot.srdf
robot_name_in_srdf=doggo_robot
moveit_config_pkg=src/doggo_bot/
robot_name=doggo_robot
planning_group_name=FrontRight
ikfast_plugin_pkg=doggo_robot_ikfast_FrontRight_plugin
base_link_name=base_link
eef_link_name=FrontRightLink4
ikfast_output_path=/home/jim/project/robotics/robot/src/doggo_robot_ikfast_FrontRight_plugin/src/doggo_robot_FrontRight_ikfast_solver.cpp

rosrun moveit_kinematics create_ikfast_moveit_plugin.py\
  --search_mode=$search_mode\
  --srdf_filename=$srdf_filename\
  --robot_name_in_srdf=$robot_name_in_srdf\
  --moveit_config_pkg=$moveit_config_pkg\
  $robot_name\
  $planning_group_name\
  $ikfast_plugin_pkg\
  $base_link_name\
  $eef_link_name\
  $ikfast_output_path
