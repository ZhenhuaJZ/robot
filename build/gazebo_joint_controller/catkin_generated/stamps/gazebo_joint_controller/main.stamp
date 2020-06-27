import rospy
import std_msgs
import gazebo_msgs


def callback(data):
    print(data)


def recieve_joint_status():
    rospy.init_node('joint_listener')
    rospy.Subscriber("/get_link_status", gazebo_msgs.GetLinkState, callback)

    rospy.spin()


if __name__ == "__main__":
    recieve_joint_status()
