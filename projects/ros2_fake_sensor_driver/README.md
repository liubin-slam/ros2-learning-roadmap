# ros2_fake_sensor_driver

第 11 周项目：模拟 TCP 传感器，并编写 ROS2 driver 节点解析数据。

这个项目用于学习“驱动节点”的通用思路。真实设备可能通过串口、CAN、USB、TCP、UDP 或厂商 SDK 输出数据，但 ROS2 driver 的核心流程类似。

## 你要先学什么

1. TCP server/client 基础。
2. 字节流和按行协议。
3. 超时、断连、重连。
4. ROS2 参数。
5. ROS2 publisher。

## 去哪里学

搜索关键词：

```text
Python socket server client
TCP stream readline protocol
ROS2 rclpy publisher parameter
robot sensor driver architecture
```

优先看：

- Python 官方 `socket` 文档中的 TCP server/client 示例。
- ROS2 rclpy publisher 和 parameter 教程。

## 项目目标

数据流：

```text
fake_sensor_server.py -> TCP 9000 -> tcp_sensor_driver -> /fake_sensor/status
```

功能：

- 模拟器每 100ms 输出一行传感器数据。
- driver 连接 TCP server。
- driver 解析 CSV。
- driver 发布 ROS2 topic。
- 断连后不崩溃。

## 协议

每行一条 CSV：

```text
timestamp_ms,temperature,battery,velocity
```

示例：

```text
1710000000000,36.5,82.0,0.42
```

## 第 1 步：理解模拟器

文件：

```text
scripts/fake_sensor_server.py
```

关键代码：

```python
server.bind((host, port))
server.listen(1)
conn, addr = server.accept()
```

解释：

- `bind`：绑定 IP 和端口。
- `listen`：开始监听连接。
- `accept`：等待客户端连接。

发送数据：

```python
conn.sendall(line.encode("utf-8"))
```

解释：

- TCP 只能发送 bytes。
- 字符串要先 `encode("utf-8")`。
- 每行末尾加 `\n`，driver 才知道一条数据结束。

## 第 2 步：理解 driver 连接

代码：

```python
self.sock = socket.create_connection((host, port), timeout=timeout)
```

解释：

- `host` 默认 `127.0.0.1`。
- `port` 默认 `9000`。
- `timeout` 防止连接一直卡住。

## 第 3 步：理解 buffer

代码：

```python
self.buffer += chunk
while "\n" in self.buffer:
    line, self.buffer = self.buffer.split("\n", 1)
```

解释：

- TCP 是字节流，不保证一次 `recv()` 正好是一整行。
- 可能半行，也可能多行。
- 所以要用 `buffer` 缓存数据。
- 遇到 `\n` 才切出完整一行。

这是驱动开发中非常重要的思维：不能假设一次读取就是一条完整消息。

## 第 4 步：理解 parse_packet()

代码：

```python
parts = line.strip().split(",")
if len(parts) != 4:
    raise ValueError(...)
```

解释：

- 按逗号切字段。
- 字段数量不对，说明协议错误或数据损坏。
- driver 应该丢弃非法数据，而不是崩溃。

## 第 5 步：发布 ROS2 Topic

代码：

```python
message = String()
message.data = "..."
self.publisher.publish(message)
```

解释：

- 当前项目为了简单使用 `std_msgs/String`。
- 真实项目应尽量使用标准结构化消息，例如 `sensor_msgs/Imu`、`sensor_msgs/LaserScan`、`nav_msgs/Odometry`。

## 运行

终端 1：

```bash
python3 scripts/fake_sensor_server.py
```

终端 2：

```bash
mkdir -p ~/ros2_ws/src
cp -r ros2_fake_sensor_driver ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run fake_sensor_driver tcp_sensor_driver
```

终端 3：

```bash
ros2 topic echo /fake_sensor/status
```

## 你要自己完成的改动

- [ ] 新增参数 `topic_name`。
- [ ] 服务器每 50 条数据故意发送一条非法数据。
- [ ] driver 统计丢弃了多少非法包。
- [ ] 断开服务器后观察 driver 是否崩溃。
- [ ] README 记录一次断连测试结果。

## 验收问题

- TCP 和串口 driver 的共同点是什么？
- 为什么 TCP 需要 buffer？
- 为什么不能假设一次 `recv()` 就是一条消息？
- driver 遇到非法数据应该怎么处理？
- 真实传感器 SDK 接入 ROS2 的流程是什么？

