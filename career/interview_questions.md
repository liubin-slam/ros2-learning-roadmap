# ROS 开发实习面试问题

## ROS/ROS2

1. ROS 和 ROS2 的区别是什么？
2. Topic、Service、Action 的区别是什么？
3. ROS2 节点之间如何通信？
4. DDS 在 ROS2 中起什么作用？
5. Parameter 和普通配置文件有什么区别？
6. launch 文件解决什么问题？
7. rosbag 有什么用？

## 机器人基础

1. 什么是 TF？
2. base_link、odom、map 分别表示什么？
3. URDF 是什么？
4. LaserScan、Image、PointCloud2 的区别是什么？
5. SLAM、定位、路径规划、控制分别解决什么问题？

## 嵌入式接口和传感器驱动

1. 上位机和下位机分别负责什么？
2. UART、USB、CAN、I2C、SPI 分别适合什么场景？
3. Linux 下 `/dev/ttyUSB0` 和 `/dev/video0` 分别通常代表什么？
4. 如何排查串口设备没有权限？
5. udev 规则解决什么问题？
6. 一个 IMU driver 节点通常要做哪些事？
7. 传感器 SDK 接入 ROS2 的基本流程是什么？

## C++/工程

1. CMake 和 colcon 分别负责什么？
2. 智能指针解决什么问题？
3. mutex 和 atomic 的区别是什么？
4. 传感器 driver 节点一般负责什么？
5. 如何排查一个 ROS2 topic 没有数据？

