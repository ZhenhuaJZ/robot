#!/usr/bin/env python3.7

import numpy as np
import rospy
from std_msgs.msg import Float64


def pub():
    publisher = rospy.Publisher("/sample_hexapod_robot/LeftFrontJoint2_position_controller/state",
                                Float64)
    rospy.init_node("test_pub", anonymous=True)
    rate = rospy.Rate(10)
    i = 0
    while not rospy.is_shutdown():
        joint_rad = np.pi*np.sin(i/100)
        rospy.loginfo(joint_rad)
        publisher.publish(data=joint_rad)
        rate.sleep()


if __name__ == "__main__":
    try:
        pub()
    except rospy.ROSInterruptException:
        print("Exception occurred")
        pass
