#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import numpy as np


if __name__ == "__main__":
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_it_node', anonymous=True)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "FrontRight"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    planning_frame = move_group.get_planning_frame()
    print(func for func in dir(move_group))
    exit()
    print("============ Planning frame: %s" % planning_frame)

    # We can also print the name of the end-effector link for this group:
    eef_link = move_group.get_end_effector_link()
    print("============ End effector link: %s" % eef_link)

    # We can get a list of all the groups in the robot:
    group_names = robot.get_group_names()
    print("============ Available Planning Groups:", robot.get_group_names())

    # Sometimes for debugging it is useful to print the entire state of the
    # robot:
    print("============ Printing robot state", robot.get_current_state())

    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = 0
    joint_goal[2] = 0
    move_group.go(joint_goal, wait=True)
    move_group.stop()

    # pose_goal = geometry_msgs.msg.Pose()
    # curr_pose = move_group.get_current_pose().pose
    # pose_goal.position.x = curr_pose.position.x + 0.02
    # pose_goal.position.y = curr_pose.position.y
    # pose_goal.position.z = curr_pose.position.z + 0.2
    # move_group.set_pose_target(pose_goal, True)
    # move_group.go(wait=True)
    # move_group.stop()
    # print(move_group.get_current_pose().pose)
    # waypoints = []
    # wpose = move_group.get_current_pose().pose
    # wpose.position.x += 0.01
    # wpose.position.y += 0.01
    # waypoints.append(copy.deepcopy(wpose))
    # wpose.position.x += 0.01
    # wpose.position.y += 0.01
    # waypoints.append(copy.deepcopy(wpose))
    # wpose.position.x += 0.01
    # wpose.position.y += 0.01
    # waypoints.append(copy.deepcopy(wpose))
    # move_group.set_pose_target(pose_goal)

    # (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.1, 0.0)
    # move_group.execute(plan, wait=True)

    # move_group.stop()
    # move_group.clear_pose_targets()
    # try:
    #     print("out")
    # except rospy.ROSInterruptException:
    #     print("Exception occurred")
    #     pass
