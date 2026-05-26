# 第 3-4 周：ROS2 核心通信

## 学习任务

- [ ] 创建 ROS2 workspace
- [ ] 创建 C++ package
- [ ] Topic 发布/订阅
- [ ] Service 请求/响应
- [ ] Parameter 配置
- [ ] Launch 一键启动
- [ ] rosbag 录制和回放
- [ ] 完成 `ros2_robot_status_system`

## 本周验收命令

```bash
colcon build
source install/setup.bash
ros2 launch robot_status_system status_system.launch.py
ros2 topic echo /robot/status
ros2 service call /reset_alarm std_srvs/srv/Trigger "{}"
```

