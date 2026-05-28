# 第 3-4 周：ROS2 核心通信

目标：完成 `ros2_robot_status_system`，掌握 Topic、Service、Parameter、Launch。

阅读顺序：先看本文件安排每天任务；当任务提到 `ros2_robot_status_system` 时，再打开 [projects/ros2_robot_status_system/README.md](../projects/ros2_robot_status_system/README.md) 看项目步骤和代码解释。

## 去哪里学

看 ROS2 Humble 官方教程，搜索：

- `ROS2 Humble publisher subscriber C++`
- `ROS2 Humble service client C++`
- `ROS2 Humble parameters C++`
- `ROS2 Humble launch file`
- `ROS2 Humble rosbag`

## 第 1 天：workspace 和 package

学习：

- workspace 是多个 ROS2 包的工作区。
- package 是一个功能模块。
- `colcon build` 负责构建 workspace。

任务：

- 创建 `~/ros2_ws/src`
- 把 `ros2_robot_status_system` 放入 `src`
- 执行 `colcon build`

验收：

```bash
source install/setup.bash
ros2 pkg list | grep robot_status_system
```

## 第 2 天：Publisher

学习：

- `rclcpp::Node`
- `create_publisher`
- `create_wall_timer`
- `publish`

任务：

- 读 `src/status_publisher.cpp`
- 理解每 500ms 发布一次状态
- 改一次发布频率

验收：

```bash
ros2 run robot_status_system status_publisher
ros2 topic echo /robot/status
```

## 第 3 天：Subscriber

学习：

- `create_subscription`
- callback 回调函数
- 从消息中读取数据

任务：

- 读 `src/status_monitor.cpp`
- 理解收到状态后如何判断报警
- 新增一个速度报警条件

## 第 4 天：Parameter

学习：

- `declare_parameter`
- YAML 参数文件
- launch 中加载参数

任务：

- 修改 `config/status_thresholds.yaml`
- 观察报警阈值变化

## 第 5 天：Service

学习：

- Service 是请求/响应模型。
- Topic 是持续数据流。

任务：

- 读 `src/reset_alarm_server.cpp`
- 调用 `/reset_alarm`

验收：

```bash
ros2 service call /reset_alarm std_srvs/srv/Trigger "{}"
```

## 第 6-7 天：Launch 和 rosbag

任务：

- 用 launch 一键启动 3 个节点。
- 录制 `/robot/status`。
- 回放 rosbag。

命令：

```bash
ros2 launch robot_status_system status_system.launch.py
ros2 bag record /robot/status
ros2 bag play <bag目录>
```

## 最终验收

- [ ] 能解释 Topic、Service、Parameter、Launch 的区别
- [ ] 能用 `ros2 topic echo`
- [ ] 能用 `ros2 service call`
- [ ] 能用 `ros2 bag record/play`
- [ ] 项目 README 补充命令和截图
