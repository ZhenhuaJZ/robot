#!/usr/bin/env python

import numpy as np
import rospy
from std_msgs.msg import Float64


class JointController:
    def __init__(self):
        self.init_joint_publishers()
        return

    def init_joint_publishers(self):
        self.RightFrontJoint2_pub = rospy.Publisher("/sample_hexapod_robot/RightFrontJoint2_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.RightFrontJoint3_pub = rospy.Publisher("/sample_hexapod_robot/RightFrontJoint3_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.RightFrontJoint4_pub = rospy.Publisher("/sample_hexapod_robot/RightFrontJoint4_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.LeftFrontJoint2_pub = rospy.Publisher("/sample_hexapod_robot/LeftFrontJoint2_position_controller/command",
                                                   Float64,
                                                   queue_size=1)
        self.LeftFrontJoint3_pub = rospy.Publisher("/sample_hexapod_robot/LeftFrontJoint3_position_controller/command",
                                                   Float64,
                                                   queue_size=1)
        self.LeftFrontJoint4_pub = rospy.Publisher("/sample_hexapod_robot/LeftFrontJoint4_position_controller/command",
                                                   Float64,
                                                   queue_size=1)
        self.MiddleRightJoint2_pub = rospy.Publisher("/sample_hexapod_robot/MiddleRightJoint2_position_controller/command",
                                                     Float64,
                                                     queue_size=1)
        self.MiddleRightJoint3_pub = rospy.Publisher("/sample_hexapod_robot/MiddleRightJoint3_position_controller/command",
                                                     Float64,
                                                     queue_size=1)
        self.MiddleRightJoint4_pub = rospy.Publisher("/sample_hexapod_robot/MiddleRightJoint4_position_controller/command",
                                                     Float64,
                                                     queue_size=1)
        self.MiddleLeftJoint2_pub = rospy.Publisher("/sample_hexapod_robot/MiddleLeftJoint2_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.MiddleLeftJoint3_pub = rospy.Publisher("/sample_hexapod_robot/MiddleLeftJoint3_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.MiddleLeftJoint4_pub = rospy.Publisher("/sample_hexapod_robot/MiddleLeftJoint4_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.BottomRightJoint2_pub = rospy.Publisher("/sample_hexapod_robot/BottomRightJoint2_position_controller/command",
                                                     Float64,
                                                     queue_size=1)
        self.BottomRightJoint3_pub = rospy.Publisher("/sample_hexapod_robot/BottomRightJoint3_position_controller/command",
                                                     Float64,
                                                     queue_size=1)
        self.BottomRightJoint4_pub = rospy.Publisher("/sample_hexapod_robot/BottomRightJoint4_position_controller/command",
                                                     Float64,
                                                     queue_size=1)
        self.BottomLeftJoint2_pub = rospy.Publisher("/sample_hexapod_robot/BottomLeftJoint2_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.BottomLeftJoint3_pub = rospy.Publisher("/sample_hexapod_robot/BottomLeftJoint3_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.BottomLeftJoint4_pub = rospy.Publisher("/sample_hexapod_robot/BottomLeftJoint4_position_controller/command",
                                                    Float64,
                                                    queue_size=1)

    def pos_reset(self):
        self.control_front_right_joint(0, 0, 0)
        self.control_front_left_joint(0, 0, 0)
        self.control_middle_right_joint(0, 0, 0)
        self.control_middle_left_joint(0, 0, 0)
        self.control_bottom_right_joint(0, 0, 0)
        self.control_bottom_left_joint(0, 0, 0)

    def control_front_right_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.RightFrontJoint2_pub.publish(data=joint1)
        if joint2:
            self.RightFrontJoint3_pub.publish(data=joint2)
        if joint3:
            self.RightFrontJoint4_pub.publish(data=joint3)

    def control_front_left_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.LeftFrontJoint2_pub.publish(data=joint1)
        if joint2:
            self.LeftFrontJoint3_pub.publish(data=joint2)
        if joint3:
            self.LeftFrontJoint4_pub.publish(data=joint3)

    def control_middle_right_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.MiddleRightJoint2_pub.publish(data=joint1)
        if joint2:
            self.MiddleRightJoint3_pub.publish(data=joint2)
        if joint3:
            self.MiddleRightJoint4_pub.publish(data=joint3)

    def control_middle_left_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.MiddleLeftJoint2_pub.publish(data=joint1)
        if joint2:
            self.MiddleLeftJoint3_pub.publish(data=joint2)
        if joint3:
            self.MiddleLeftJoint4_pub.publish(data=joint3)

    def control_bottom_right_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.BottomRightJoint2_pub.publish(data=joint1)
        if joint2:
            self.BottomRightJoint3_pub.publish(data=joint2)
        if joint3:
            self.BottomRightJoint4_pub.publish(data=joint3)

    def control_bottom_left_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.BottomLeftJoint2_pub.publish(data=joint1)
        if joint2:
            self.BottomLeftJoint3_pub.publish(data=joint2)
        if joint3:
            self.BottomLeftJoint4_pub.publish(data=joint3)

    def __call__(self, joint):
        self.control_front_right_joint(0.1, joint, 0.1)
        self.control_front_left_joint(0.1, -joint, 0.1)
        self.control_middle_right_joint(0.1, joint, 0.1)
        self.control_middle_left_joint(0.1, -joint, 0.1)
        self.control_bottom_right_joint(0.1, joint, 0.1)
        self.control_bottom_left_joint(0.1, -joint, 0.1)


def frontRightIK(x, y, z):
    # x_offset =
    # y_offset =
    l1 = 1.13 * 0.0254
    l2 = 2.97 * 0.0254
    l3 = 3.65 * 0.0254
    # x = x + l1 * np.cos(45) + 0.02
    # y = y + l1 * np.sin(45) + 0.02
    # print(l1 + l2 + l3)
    offsets_q2 = np.pi / 4
    d = np.sqrt((x - l1 * np.cos(np.pi / 4))**2 + (y - l1 * np.cos(np.pi / 4))**2 + z**2)
    print("distance d: ", d)
    print("(2 * l2 * l3)", (2 * l2 * l3))
    # print(d)
    q1 = np.arctan(x/y) - np.pi / 4
    q3 = -np.pi + np.arccos((l2**2 + l3**2 - d**2) / (2 * l2 * l3)) + (offsets_q2 + np.pi / 2)
    # print((l2**2 + l3**2 - d**2), (2 * l2 * l3))
    q2 = -np.arctan(z/y) + np.arccos((d**2 + l2**2 - l3**2) / (2 * d * l2)) - offsets_q2
    return q1, q2, q3


def pub():
    controller = JointController()
    rospy.init_node("test_pub", anonymous=True)
    rate = rospy.Rate(10)
    controller.pos_reset()
    rate.sleep()
    controller.pos_reset()
    rate.sleep()
    i = 0
    joint_loop = np.arange(-0.15, 0.15, 0.001)
    # joint_loop = np.arange(-2.2, 2.2, 0.05)
    while not rospy.is_shutdown():
        for x in joint_loop:
            q1, q2, q3 = frontRightIK(x, 0.05, 0.01)
            print("joint_output: ", q1, q2, q3)
            print("coordinates: ", x, 0.1, 0.1)
            controller.control_front_right_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            controller.control_front_left_joint(joint1=q1, joint2=q2, joint3=q3)
            controller.control_middle_right_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            controller.control_middle_left_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            controller.control_bottom_right_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            controller.control_bottom_left_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            rate.sleep()

        for x in joint_loop:
            q1, q2, q3 = frontRightIK(-x, (1.13*0.0254) / 4, 0.05)
            print("joint_output: ", q1, q2, q3)
            controller.control_front_right_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            controller.control_front_left_joint(joint1=q1, joint2=q2, joint3=q3)
            controller.control_middle_right_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            controller.control_middle_left_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            controller.control_bottom_right_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            controller.control_bottom_left_joint(joint1=0.01, joint2=0.01, joint3=0.01)
            rate.sleep()
        # for x in loops:
        #     q1, q2, q3 = frontRightIK(-x, (1.13*0.0254) / 4, 0.05)
        #     controller.LeftFrontJoint2_pub.publish(q1)
        #     rate.sleep()
        #     controller.LeftFrontJoint3_pub.publish(-q2)
        #     rate.sleep()
        #     controller.LeftFrontJoint4_pub.publish(q3)
        #     rate.sleep()
        #     print(q1, q2, q3)
        #     exit()
        # exit()
        # joint_rad = np.pi*np.sin(i)
        # while joint_rad < np.pi / 4:
        #     joint_rad = np.pi*np.sin(i)
        #     print(joint_rad)
        #     controller(joint_rad)
        #     i += 0.005
        #     rate.sleep()
        # while joint_rad > -np.pi / 4:
        #     joint_rad = np.pi*np.sin(i)
        #     controller(joint_rad)
        #     i -= 0.005
        #     rate.sleep()
        # i += 1
        # print(i)
        # print(joint_rad)
        # rospy.loginfo(joint_rad)
        # publisher.publish(data=joint_rad)



if __name__ == "__main__":
    try:
        pub()
    except rospy.ROSInterruptException:
        print("Exception occurred")
        pass
