from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from pathlib import Path


def generate_launch_description():
    package_share = Path(get_package_share_directory("robot_status_system"))
    config_file = package_share / "config" / "status_thresholds.yaml"

    return LaunchDescription([
        Node(
            package="robot_status_system",
            executable="status_publisher",
            name="status_publisher",
            output="screen",
        ),
        Node(
            package="robot_status_system",
            executable="status_monitor",
            name="status_monitor",
            parameters=[str(config_file)],
            output="screen",
        ),
        Node(
            package="robot_status_system",
            executable="reset_alarm_server",
            name="reset_alarm_server",
            output="screen",
        ),
    ])

