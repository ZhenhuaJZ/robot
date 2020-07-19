export MYROBOT_NAME="doggo_robot"
export PLANNING_GROUP="BackLeft"
export URDF_PATH="src/doggo_robot/urdf"

openrave-robot.py $URDF_PATH/"$MYROBOT_NAME".dae --info links

export BASE_LINK="1"
export EEF_LINK="5"
export IKFAST_OUTPUT_PATH=$URDF_PATH/ikfast61_"$PLANNING_GROUP".cpp

python `openrave-config --python-dir`/openravepy/_openravepy_/ikfast.py --robot=$URDF_PATH/"$MYROBOT_NAME".dae --iktype=translation3d --baselink="$BASE_LINK" --eelink="$EEF_LINK" --savefile="$IKFAST_OUTPUT_PATH"

export MOVEIT_IK_PLUGIN_PKG="$MYROBOT_NAME"_ikfast_"$PLANNING_GROUP"_plugin
cd src
catkin_create_pkg "$MOVEIT_IK_PLUGIN_PKG"
cd ../
catkin_make
rosrun moveit_kinematics create_ikfast_moveit_plugin.py "$MYROBOT_NAME" "$PLANNING_GROUP" "$MOVEIT_IK_PLUGIN_PKG" "base_link" $PLANNING_GROUP"Link4" "$IKFAST_OUTPUT_PATH"
