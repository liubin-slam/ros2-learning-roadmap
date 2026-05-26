cmake_minimum_required(VERSION 3.8)
project(robot_status_system)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)

add_executable(status_publisher src/status_publisher.cpp)
ament_target_dependencies(status_publisher rclcpp std_msgs)

add_executable(status_monitor src/status_monitor.cpp)
ament_target_dependencies(status_monitor rclcpp std_msgs)

add_executable(reset_alarm_server src/reset_alarm_server.cpp)
ament_target_dependencies(reset_alarm_server rclcpp std_srvs)

install(TARGETS
  status_publisher
  status_monitor
  reset_alarm_server
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

