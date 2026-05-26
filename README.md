# ROS2 开发实习 12 周学习仓库

这个仓库用于从零基础学习到可以投递机器人 ROS 开发实习。主线环境默认：

- Ubuntu 22.04
- ROS2 Humble
- C++17
- Python 3
- CMake、colcon、Git、RViz2、rqt

## 使用方式

1. 先读 [START_HERE.md](./START_HERE.md)。
2. Git 零基础先读 [GIT_BEGINNER.md](./GIT_BEGINNER.md)。
3. 再读 [12_week_plan.md](./12_week_plan.md)。
4. 每周按 `weeks/` 里的清单推进。
5. 每完成一个项目，在项目 README 中补充运行截图、问题记录和改进点。
6. 每周至少提交 5 次 Git commit。

## 项目目录

| 阶段 | 项目 | 目标 |
| --- | --- | --- |
| 第 1-2 周 | [cpp_sensor_logger](./projects/cpp_sensor_logger) | C++、CMake、日志、基础工程能力 |
| 第 3-4 周 | [ros2_robot_status_system](./projects/ros2_robot_status_system) | ROS2 Topic、Service、Parameter、Launch |
| 第 5-6 周 | [ros2_mobile_robot_description](./projects/ros2_mobile_robot_description) | URDF、TF、RViz2 机器人模型 |
| 第 9-10 周 | [ros2_camera_opencv_detector](./projects/ros2_camera_opencv_detector) | ROS2 图像话题、OpenCV、cv_bridge |
| 第 11 周 | [ros2_fake_sensor_driver](./projects/ros2_fake_sensor_driver) | TCP 传感器模拟、驱动节点、多线程思路 |

## 最终验收

完成后你应该至少具备：

- 能独立创建 ROS2 workspace 和 package
- 能写 C++/Python ROS2 节点
- 能解释 Topic、Service、Action、Parameter、Launch、TF、URDF、rosbag
- 能在 RViz2 中查看模型、坐标系、图像或点云
- 能把 3 个项目写进简历，并在面试中讲清数据流和工程取舍
