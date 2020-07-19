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
    try:
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('move_it_node', anonymous=True, disable_signals=True)
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        group_name = "FrontRight"
        FrontRightGroup = moveit_commander.MoveGroupCommander("FrontRight")
        BackLeftGroup = moveit_commander.MoveGroupCommander("BackLeft")

        joint_goal = FrontRightGroup.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = 0
        joint_goal[2] = 0
        FrontRightGroup.go(joint_goal, wait=True)
        FrontRightGroup.stop()
        FrontRightGroup.clear_pose_targets()

        joint_goal = BackLeftGroup.get_current_joint_values()
        joint_goal[0] = 0
        joint_goal[1] = 0
        joint_goal[2] = 0
        BackLeftGroup.go(joint_goal, wait=True)
        BackLeftGroup.stop()
        BackLeftGroup.clear_pose_targets()
        # exit()
        FrontRightGroup.set_goal_orientation_tolerance(100)
        coords = np.linspace(0, 2*3.14, 20)
        init_pose = FrontRightGroup.get_current_pose().pose
        x = init_pose.position.x
        y = init_pose.position.y
        z = init_pose.position.z
        points_front_right = [[x, y + 0.05, z + 0.15],
                  [x, y - 0.05, z + 0.15],
                  [x, y - 0.05, z + 0.05],
                  [x, y + 0.05, z + 0.05]]

        BackLeftGroup.set_goal_orientation_tolerance(100)
        coords = np.linspace(0, 2*3.14, 20)
        init_pose = BackLeftGroup.get_current_pose().pose
        x = init_pose.position.x
        y = init_pose.position.y
        z = init_pose.position.z
        points_back_left = [[x, y + 0.05, z + 0.15],
                  [x, y - 0.05, z + 0.15],
                  [x, y - 0.05, z + 0.05],
                  [x, y + 0.05, z + 0.05]]
        while not rospy.is_shutdown():
            for xyz_fr, xyz_bl in zip(points_front_right, points_back_left):
                pose_goal = geometry_msgs.msg.Pose()
                pose_goal.position.x = xyz_fr[0]
                pose_goal.position.y = xyz_fr[1]
                pose_goal.position.z = xyz_fr[2]
                FrontRightGroup.set_joint_value_target(pose_goal, 'FrontRightLink4', True)
                FrontRightGroup.go(wait=True)
                # FrontRightGroup.clear_pose_targets()

                pose_goal = geometry_msgs.msg.Pose()
                pose_goal.position.x = xyz_bl[0]
                pose_goal.position.y = xyz_bl[1]
                pose_goal.position.z = xyz_bl[2]
                BackLeftGroup.set_joint_value_target(pose_goal, 'BackLeftLink4', True)
                BackLeftGroup.go(wait=True)
                BackLeftGroup.clear_pose_targets()
                # exit()
    #     print("out")
    except rospy.ROSInterruptException:
        print("Exception occurred")
        pass
