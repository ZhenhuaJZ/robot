execute_process(COMMAND "/home/jim/project/robotics/catkin_ws/build/test_joint_pub/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jim/project/robotics/catkin_ws/build/test_joint_pub/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
