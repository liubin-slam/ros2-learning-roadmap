# 简历项目描述模板

## ROS2 机器人状态监控系统

- 基于 ROS2 Humble 开发机器人状态监控系统，实现 Topic、Service、Parameter、Launch 集成。
- 使用 C++ 编写状态发布、报警监控和重置服务节点，支持电量、温度、速度等状态数据模拟与监控。
- 使用 ros2 CLI 和 rosbag 完成通信链路调试、数据录制和回放。

## ROS2 串口 IMU 驱动

- 基于 ROS2 开发串口 IMU 驱动节点，解析下位机输出的加速度和角速度数据，并发布 `sensor_msgs/Imu` 到 `/imu/data_raw`。
- 设计 CSV 行协议并实现非法数据过滤、串口超时处理和参数化配置，支持端口、波特率、frame_id 配置。
- 熟悉 Linux 串口设备、`/dev/ttyUSB0`、`dialout` 权限和 udev 固定设备名的基本排查流程。

## ROS2 移动机器人模型

- 基于 URDF/Xacro 构建两轮差速移动机器人模型，包含 base_link、左右轮、camera_link、laser_link。
- 使用 robot_state_publisher 和 joint_state_publisher_gui 发布机器人 TF，并在 RViz2 中完成模型可视化。
- 理解并能解释 base_link、odom、map 等常见机器人坐标系职责。

## ROS2 OpenCV 视觉检测

- 基于 ROS2 和 OpenCV 开发颜色目标检测节点，实现摄像头图像读取、HSV 阈值分割和目标中心点输出。
- 使用 cv_bridge 将 OpenCV 图像转换为 ROS2 Image 消息，发布原始图像和处理后图像 topic。
- 使用 rqt_image_view/RViz2 完成图像链路调试和可视化验证。

