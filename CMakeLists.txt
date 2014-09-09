cmake_minimum_required(VERSION 2.8.3)
project(wifi_im)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS message_runtime
  CATKIN_DEPENDS rospy
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
  bin/wifi_im
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
