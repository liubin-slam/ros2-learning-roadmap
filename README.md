# ROS2 开发实习 12 周学习仓库

这个仓库用于从零基础学习到可以投递机器人 ROS 开发实习。主线环境默认：

- Ubuntu 22.04
- ROS2 Humble
- C++17
- Python 3
- CMake、colcon、Git、RViz2、rqt

## 先看哪个文件

只按这个顺序看，不要在目录里乱点：

1. [START_HERE.md](./START_HERE.md)：第一天从哪里开始。
2. [HOW_TO_USE_THIS_REPO.md](./HOW_TO_USE_THIS_REPO.md)：解释 `weeks/` 和 `projects/` 分别什么时候看。
3. [GIT_BEGINNER.md](./GIT_BEGINNER.md)：Git 零基础流程。
4. [LEARNING_RESOURCES.md](./LEARNING_RESOURCES.md)：每个阶段去哪里学。
5. [12_week_plan.md](./12_week_plan.md)：12 周总览。
6. `weeks/week_xx.md`：每天真正照着执行的任务单。
7. `projects/xxx/README.md`：当 week 文件要求你做某个项目时，再打开对应项目教程。

## 最重要的规则

`weeks/` 是学习路线和每天任务，回答“今天该做什么”。  
`projects/` 是项目教程和代码解释，回答“这个项目怎么一步一步做”。  

所以每天的正确流程是：

```text
先看对应 week 文件
  -> week 让你做哪个项目
  -> 再打开对应 projects/项目名/README.md
  -> 按项目 README 写代码、运行、截图
  -> 回到 week 文件打勾
  -> Git commit
```

## 项目目录

| 阶段 | 先看 week | 再看 project |
| --- | --- | --- |
| 第 0 周 | [week_00_environment.md](./weeks/week_00_environment.md) | 暂无项目，先装环境 |
| 第 1-2 周 | [week_01_02_cpp_cmake.md](./weeks/week_01_02_cpp_cmake.md) | [cpp_sensor_logger](./projects/cpp_sensor_logger) |
| 第 3-4 周 | [week_03_04_ros2_communication.md](./weeks/week_03_04_ros2_communication.md) | [ros2_robot_status_system](./projects/ros2_robot_status_system) |
| 第 5-6 周 | [week_05_06_urdf_tf.md](./weeks/week_05_06_urdf_tf.md) | [ros2_serial_imu_driver](./projects/ros2_serial_imu_driver)、[ros2_mobile_robot_description](./projects/ros2_mobile_robot_description) |
| 第 7-8 周 | [week_07_08_nav_sim.md](./weeks/week_07_08_nav_sim.md) | 先扩展前面的模型项目 |
| 第 9-10 周 | [week_09_10_vision_pointcloud.md](./weeks/week_09_10_vision_pointcloud.md) | [ros2_camera_opencv_detector](./projects/ros2_camera_opencv_detector) |
| 第 11 周 | [week_11_driver.md](./weeks/week_11_driver.md) | [ros2_fake_sensor_driver](./projects/ros2_fake_sensor_driver) |
| 第 12 周 | [week_12_portfolio.md](./weeks/week_12_portfolio.md) | 整理所有项目 README 和简历材料 |

## 最终验收

完成后你应该至少具备：

- 能独立创建 ROS2 workspace 和 package
- 能写 C++/Python ROS2 节点
- 能解释 Topic、Service、Action、Parameter、Launch、TF、URDF、rosbag
- 能解释 UART、USB、CAN、I2C、SPI 的基本用途
- 能在 Linux 下排查 `/dev/ttyUSB0`、`/dev/video0`、USB 权限和 udev 固定设备名
- 能在 RViz2 中查看模型、坐标系、图像或点云
- 能把 3 个项目写进简历，并在面试中讲清数据流和工程取舍

