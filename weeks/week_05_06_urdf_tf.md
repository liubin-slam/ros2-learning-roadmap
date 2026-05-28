# 第 5-6 周：嵌入式接口、TF、URDF、RViz2

## 学习任务

- [ ] 理解上位机和下位机分工
- [ ] 理解 UART、USB、CAN、I2C、SPI 的用途
- [ ] 学会查看 `/dev/ttyUSB0`、`lsusb`、`dmesg`
- [ ] 理解 Linux 串口权限和 `dialout` 用户组
- [ ] 理解 udev 固定设备名
- [ ] 完成 `ros2_serial_imu_driver`
- [ ] 理解 base_link、odom、map
- [ ] 学习 URDF link/joint
- [ ] 使用 xacro 管理模型
- [ ] 使用 robot_state_publisher
- [ ] 使用 joint_state_publisher_gui
- [ ] RViz2 查看模型和 TF
- [ ] 完成 `ros2_mobile_robot_description`

## 本周验收

- 能解释 MCU/传感器数据如何进入 ROS2 Topic
- 能运行串口 IMU driver，并发布 `/imu/data_raw`
- RViz2 中小车模型显示正常
- Fixed Frame 设置为 `base_link` 或 `odom`
- TF 树没有断裂

