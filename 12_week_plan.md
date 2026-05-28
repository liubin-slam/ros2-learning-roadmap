# ROS2 开发实习 12 周计划

## 第 0 周：环境准备

目标：

- 安装 Ubuntu 22.04 和 ROS2 Humble
- 安装 VS Code、Git、CMake、colcon、rviz2、rqt
- 跑通官方 talker/listener

验收：

```bash
ros2 run demo_nodes_cpp talker
ros2 run demo_nodes_py listener
ros2 topic list
```

## 第 1-2 周：Linux、Git、C++、CMake

目标：

- 掌握 Linux 常用命令、Git 基本流程
- 掌握 C++ 类、STL、智能指针、文件 IO
- 能写 CMake 项目

项目：

- `projects/cpp_sensor_logger`

验收：

- 能编译并运行 C++ 日志程序
- 能解释类、构造函数、vector、map、unique_ptr/shared_ptr
- README 中记录编译运行命令

## 第 3-4 周：ROS2 核心通信

目标：

- workspace、package、node
- Topic、Service、Parameter、Launch
- rosbag、rqt、rviz2 基础

项目：

- `projects/ros2_robot_status_system`

验收：

- 能启动状态发布、监控、重置服务
- 能用 ros2 CLI 查看 topic/service/parameter
- 能录制并回放 rosbag

## 第 5-6 周：嵌入式接口、TF、URDF、RViz2

目标：

- 理解机器人上位机/下位机分工
- 理解 UART、USB、CAN、I2C、SPI 的用途
- 能在 Linux 下查看 `/dev/ttyUSB0`、`lsusb`、`dmesg`、udev 规则
- 能写一个串口 IMU ROS2 driver
- 理解 base_link、odom、map
- 能写一个两轮差速小车 URDF
- 能用 RViz2 查看模型和 TF

项目：

- `projects/ros2_serial_imu_driver`
- `projects/ros2_mobile_robot_description`

验收：

- 能解释传感器数据如何从 MCU/USB/串口进入 ROS2 Topic
- 能发布 `/imu/data_raw`
- RViz2 中小车模型显示正常
- TF 树完整
- README 包含截图位置和解释

## 第 7-8 周：仿真、导航、传感器设备调试

目标：

- 学 Gazebo/Gz 基础
- 学 Nav2、SLAM Toolbox 概念
- 能理解建图、定位、规划、控制的职责
- 学相机 `/dev/video0`、USB 设备权限、udev 固定设备名
- 理解传感器 SDK 如何封装成 ROS2 节点

建议项目：

- 在第 5-6 周小车基础上扩展仿真
- 后续可新建 `ros2_nav_sim_demo`

验收：

- 能让小车在仿真环境移动
- 能保存地图
- 能在 RViz2 中设置目标点
- 能解释相机、IMU、雷达驱动节点的共同职责

## 第 9-10 周：视觉或点云

默认先做视觉，因为普通电脑更容易验证。

项目：

- `projects/ros2_camera_opencv_detector`

验收：

- 能读取摄像头或视频
- 能发布处理后的图像
- 能解释 Image、PointCloud2、LaserScan 区别

## 第 11 周：驱动、通信、多线程

目标：

- TCP/UDP、串口、超时、断连处理
- C++/Python 多线程基本概念
- 驱动节点如何把外部设备数据转成 ROS2 Topic
- 理解真实机器人常见链路：Ubuntu + ROS2 上位机，STM32/ESP32/Arduino 下位机，串口/CAN/UDP 通信

项目：

- `projects/ros2_fake_sensor_driver`

验收：

- 模拟器输出数据
- driver 节点解析并发布 ROS2 Topic
- 能处理非法数据、断连、超时
- 能说明串口驱动和 TCP 驱动的共同点：读取字节流、按协议切包、校验、发布标准 ROS2 消息

## 第 12 周：作品集、简历、面试

必须整理：

- 3 个主项目 README
- 运行截图
- 简历项目描述
- 面试问题答案

优先放进简历：

1. `ros2_robot_status_system`
2. `ros2_mobile_robot_description`
3. `ros2_camera_opencv_detector` 或后续点云项目
4. 如果岗位强调硬件接口，补充 `ros2_serial_imu_driver`

材料：

- [interview_questions.md](./career/interview_questions.md)
- [resume_project_bullets.md](./career/resume_project_bullets.md)

