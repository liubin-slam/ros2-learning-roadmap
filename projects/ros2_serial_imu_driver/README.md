# ros2_serial_imu_driver

第 5-6 周项目：串口 IMU 驱动节点。

这个项目用于补齐机器人 ROS 开发岗位常见的嵌入式接口能力。你不需要先成为嵌入式工程师，但必须知道上位机如何读取下位机或传感器数据，并发布成 ROS2 Topic。

## 你要先学什么

1. 上位机和下位机分工。
2. UART、USB、CAN、I2C、SPI 的用途。
3. Linux 设备文件：`/dev/ttyUSB0`、`/dev/video0`。
4. 串口权限：`dialout` 用户组。
5. udev 固定设备名。
6. ROS2 标准消息：`sensor_msgs/msg/Imu`。

## 去哪里学

搜索关键词：

```text
Linux ttyUSB0 dmesg lsusb udev
ROS2 sensor_msgs Imu
python pyserial tutorial
ROS2 rclpy publisher
```

优先看：

- ROS2 官方 `sensor_msgs` 消息定义。
- pyserial 官方文档的 `Serial.readline()` 示例。
- Linux 串口权限和 udev 教程。

## 项目目标

真实机器人常见链路：

```text
IMU / 编码器 / 底盘 MCU -> UART/CAN/USB -> Ubuntu 上位机 -> ROS2 driver node -> ROS2 Topic
```

本项目最小闭环：

```text
串口数据行 -> serial_imu_driver -> /imu/data_raw
```

## 协议设计

每行一条 CSV：

```text
timestamp_ms,ax,ay,az,gx,gy,gz
```

单位：

- `ax,ay,az`：线加速度，单位 m/s^2。
- `gx,gy,gz`：角速度，单位 rad/s。

示例：

```text
1710000000000,0.01,0.02,9.81,0.001,0.002,0.003
```

为什么要设计协议：

- 串口传输的是字节流，不是天然结构化数据。
- 你必须规定一行数据包含哪些字段。
- driver 节点按协议解析，再发布 ROS2 消息。

## 第 1 步：理解 parse_imu_line()

代码：

```python
def parse_imu_line(line: str) -> ImuPacket:
    parts = line.strip().split(",")
```

解释：

- `line` 是串口读到的一行文本。
- `strip()` 去掉换行符和空格。
- `split(",")` 按逗号切成字段。

校验：

```python
if len(parts) != 7:
    raise ValueError(...)
```

解释：

- 合法 IMU 行必须有 7 个字段。
- 字段数量不对就丢弃，不能让节点崩溃。

## 第 2 步：理解 ImuPacket

代码：

```python
@dataclass
class ImuPacket:
    timestamp_ms: int
    ax: float
    ay: float
    az: float
    gx: float
    gy: float
    gz: float
```

解释：

- `dataclass` 用来表示一组数据。
- `timestamp_ms` 是采样时间。
- `ax/ay/az` 是加速度。
- `gx/gy/gz` 是角速度。

## 第 3 步：理解参数

代码：

```python
self.declare_parameter("port", "/dev/ttyUSB0")
self.declare_parameter("baudrate", 115200)
self.declare_parameter("frame_id", "imu_link")
```

解释：

- `port`：串口设备路径。
- `baudrate`：波特率，必须和下位机一致。
- `frame_id`：IMU 所在坐标系。
- 参数化可以避免每换设备就改代码。

## 第 4 步：打开串口

代码：

```python
serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
```

解释：

- `port`：例如 `/dev/ttyUSB0`。
- `baudrate`：例如 `115200`。
- `timeout`：读取超时时间，防止程序一直卡住。

常见错误：

- 找不到设备：检查 `dmesg` 和 `ls /dev/ttyUSB*`。
- 没权限：把用户加入 `dialout`。
- 数据乱码：检查波特率是否一致。

## 第 5 步：发布 sensor_msgs/Imu

代码：

```python
message = Imu()
message.linear_acceleration.x = packet.ax
message.angular_velocity.z = packet.gz
self.publisher.publish(message)
```

解释：

- `Imu()` 是 ROS2 标准 IMU 消息。
- `linear_acceleration` 放加速度。
- `angular_velocity` 放角速度。
- `publish()` 发布到 `/imu/data_raw`。

为什么不用 `String`：

- 标准消息更容易被下游算法使用。
- 后续滤波、定位、导航模块通常都认 `sensor_msgs/Imu`。

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

真实项目不要长期依赖 `/dev/ttyUSB0`，因为插拔顺序变化会导致编号变化。应使用 udev 规则固定成：

```text
/dev/imu_usb
```

后续可以在 `/etc/udev/rules.d/99-robot-sensors.rules` 中配置。

## 构建运行

```bash
sudo apt install ros-humble-sensor-msgs python3-serial
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

## 你要自己完成的改动

- [ ] 新增参数 `topic_name`，允许修改发布 topic。
- [ ] 连续 10 次读不到数据时打印 warning。
- [ ] 给非法数据增加计数器。
- [ ] README 记录一次串口设备排查过程。

## 验收问题

- 上位机和下位机分别负责什么？
- UART 和 CAN 的区别是什么？
- `/dev/ttyUSB0` 是什么？
- udev 解决什么问题？
- 为什么 IMU 要发布成 `sensor_msgs/Imu`？

