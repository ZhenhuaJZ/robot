import rospy
import numpy as np
from std_msgs.msg import Float64


class JointController:
    def __init__(self):
        self.init_joint_publishers()
        return

    def init_joint_publishers(self):
        self.FrontRightJoint1_pub = rospy.Publisher("/FrontRightJoint1_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.FrontRightJoint2_pub = rospy.Publisher("/FrontRightJoint2_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.FrontRightJoint3_pub = rospy.Publisher("/FrontRightJoint3_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.FrontLeftJoint1_pub = rospy.Publisher("/FrontLeftJoint1_position_controller/command",
                                                   Float64,
                                                   queue_size=1)
        self.FrontLeftJoint2_pub = rospy.Publisher("/FrontLeftJoint2_position_controller/command",
                                                   Float64,
                                                   queue_size=1)
        self.FrontLeftJoint3_pub = rospy.Publisher("/FrontLeftJoint3_position_controller/command",
                                                   Float64,
                                                   queue_size=1)
        self.BackRightJoint1_pub = rospy.Publisher("/BackRightJoint1_position_controller/command",
                                                     Float64,
                                                     queue_size=1)
        self.BackRightJoint2_pub = rospy.Publisher("/BackRightJoint2_position_controller/command",
                                                     Float64,
                                                     queue_size=1)
        self.BackRightJoint3_pub = rospy.Publisher("/BackRightJoint3_position_controller/command",
                                                     Float64,
                                                     queue_size=1)
        self.BackLeftJoint1_pub = rospy.Publisher("/BackLeftJoint1_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.BackLeftJoint2_pub = rospy.Publisher("/BackLeftJoint2_position_controller/command",
                                                    Float64,
                                                    queue_size=1)
        self.BackLeftJoint3_pub = rospy.Publisher("/BackLeftJoint3_position_controller/command",
                                                    Float64,
                                                    queue_size=1)

    def pos_reset(self):
        self.control_front_right_joint(0.01, 0.01, 0.01)
        self.control_front_left_joint(0.01, 0.01, 0.01)
        self.control_back_right_joint(0.01, 0.01, 0.01)
        self.control_back_left_joint(0.01, 0.01, 0.01)

    def control_front_right_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.FrontRightJoint1_pub.publish(data=joint1)
        if joint2:
            self.FrontRightJoint2_pub.publish(data=joint2)
        if joint3:
            self.FrontRightJoint3_pub.publish(data=joint3)

    def control_front_left_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.FrontLeftJoint1_pub.publish(data=joint1)
        if joint2:
            self.FrontLeftJoint2_pub.publish(data=joint2)
        if joint3:
            self.FrontLeftJoint3_pub.publish(data=joint3)

    def control_back_right_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.BackRightJoint1_pub.publish(data=joint1)
        if joint2:
            self.BackRightJoint2_pub.publish(data=joint2)
        if joint3:
            self.BackRightJoint3_pub.publish(data=joint3)

    def control_back_left_joint(self, joint1=None, joint2=None, joint3=None):
        if joint1:
            self.BackLeftJoint1_pub.publish(data=joint1)
        if joint2:
            self.BackLeftJoint2_pub.publish(data=joint2)
        if joint3:
            self.BackLeftJoint3_pub.publish(data=joint3)

    def __call__(self, joints):
        self.control_front_right_joint(joints[0, 0], joints[1, 0], joints[2, 0])
        self.control_front_left_joint(joints[0, 1], joints[1, 1], joints[2, 1])
        self.control_back_right_joint(joints[0, 2], joints[1, 2], joints[2, 2])
        self.control_back_left_joint(joints[0, 3], joints[1, 3], joints[2, 3])
