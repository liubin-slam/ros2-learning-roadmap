# ros2_serial_imu_driver

第 5-6 周项目：串口 IMU 驱动节点。这个项目用于补齐机器人 ROS 开发岗位常见的嵌入式接口能力。

## 目标

真实机器人里常见结构：

```text
IMU / 编码器 / 底盘 MCU -> UART/CAN/USB -> Ubuntu 上位机 -> ROS2 driver node -> ROS2 Topic
```

本项目先实现最小闭环：

- 下位机或模拟器按行输出 IMU 数据
- ROS2 节点通过串口读取
- 解析加速度和角速度
- 发布 `/imu/data_raw`

## 协议

每行一条 CSV：

```text
timestamp_ms,ax,ay,az,gx,gy,gz
```

单位：

- `ax,ay,az`：m/s^2
- `gx,gy,gz`：rad/s

示例：

```text
1710000000000,0.01,0.02,9.81,0.001,0.002,0.003
```

## 依赖

```bash
sudo apt install ros-humble-sensor-msgs python3-serial
```

## 构建运行

```bash
mkdir -p ~/ros2_ws/src
cp -r ros2_serial_imu_driver ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run serial_imu_driver serial_imu_driver --ros-args -p port:=/dev/ttyUSB0 -p baudrate:=115200
```

查看数据：

```bash
ros2 topic echo /imu/data_raw
```

## Linux 设备排查

插入 USB 串口后：

```bash
lsusb
dmesg | tail -n 30
ls -l /dev/ttyUSB*
```

如果没有权限：

```bash
sudo usermod -aG dialout $USER
```

然后重新登录系统。

## udev 固定设备名

真实项目里不要长期依赖 `/dev/ttyUSB0`，因为插拔顺序变化会导致编号变化。应使用 udev 规则固定成类似：

```text
/dev/imu_usb
```

后续可以在 `/etc/udev/rules.d/99-robot-sensors.rules` 中配置。

## 验收

- 能解释上位机/下位机分工
- 能解释 UART、USB、CAN、I2C、SPI 基本用途
- 能读取串口 IMU 数据
- 能发布 `/imu/data_raw`
- 能处理非法行数据，不让节点崩溃

