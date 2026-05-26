# ros2_fake_sensor_driver

第 11 周项目：模拟 TCP 传感器，并编写 ROS2 driver 节点解析数据。

## 协议

每行一条 CSV：

```text
timestamp_ms,temperature,battery,velocity
```

示例：

```text
1710000000000,36.5,82.0,0.42
```

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

## 验收

- 合法数据能发布到 `/fake_sensor/status`
- 非法数据被丢弃并打印 warning
- 服务器断开时 driver 不崩溃

