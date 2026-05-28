# 第 7-8 周：仿真、导航、传感器设备调试

阅读顺序：先看本文件。本周主要扩展第 5-6 周的小车模型，不新开独立项目；需要回看 [projects/ros2_mobile_robot_description/README.md](../projects/ros2_mobile_robot_description/README.md)。

## 学习任务

- [ ] 学相机设备 `/dev/video0`
- [ ] 学 USB 设备排查：`lsusb`、`dmesg`
- [ ] 学 udev 固定设备名
- [ ] 理解传感器 SDK 接入 ROS2 的基本方式
- [ ] 学 Gazebo/Gz 基础
- [ ] 学差速小车控制概念
- [ ] 学 LaserScan
- [ ] 学 SLAM Toolbox
- [ ] 学 Nav2 基础流程

## 建议扩展

在 `ros2_mobile_robot_description` 基础上添加仿真配置，再逐步接入 Nav2。

## 本周验收

- 能解释建图、定位、规划、控制的区别
- 能解释相机、IMU、雷达驱动节点的共同职责
- 能保存地图
- 能在 RViz2 中查看路径规划结果
