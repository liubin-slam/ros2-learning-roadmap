# ros2_robot_status_system

第 3-4 周项目：ROS2 机器人状态监控系统。

## 功能

- `status_publisher` 发布 `/robot/status`
- `status_monitor` 订阅状态并根据阈值报警
- `reset_alarm_server` 提供 `/reset_alarm` 服务
- `config/status_thresholds.yaml` 配置报警阈值
- `launch/status_system.launch.py` 一键启动

## 放入 ROS2 workspace

```bash
mkdir -p ~/ros2_ws/src
cp -r ros2_robot_status_system ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch robot_status_system status_system.launch.py
```

## 验收命令

```bash
ros2 topic echo /robot/status
ros2 param list
ros2 service call /reset_alarm std_srvs/srv/Trigger "{}"
ros2 bag record /robot/status
```

