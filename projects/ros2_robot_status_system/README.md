# ros2_robot_status_system

第 3-4 周项目：ROS2 机器人状态监控系统。

这个项目用于学习 ROS2 最核心的通信机制：Topic、Service、Parameter、Launch。

## 你要先学什么

按顺序学：

1. ROS2 workspace 是什么。
2. ROS2 package 是什么。
3. node 是什么。
4. Topic 发布/订阅。
5. Service 请求/响应。
6. Parameter 参数。
7. Launch 一键启动多个节点。

## 去哪里学

优先看 ROS2 官方教程：

- `docs.ros.org -> Humble -> Tutorials -> Beginner: CLI tools`
- `docs.ros.org -> Humble -> Tutorials -> Writing a simple publisher and subscriber C++`
- `docs.ros.org -> Humble -> Tutorials -> Writing a simple service and client C++`
- `docs.ros.org -> Humble -> Tutorials -> Using parameters in a class C++`
- `docs.ros.org -> Humble -> Tutorials -> Creating launch files`

搜索关键词：

```text
ROS2 Humble publisher subscriber C++
ROS2 Humble service client C++
ROS2 Humble parameters C++
ROS2 Humble launch file
```

## 项目目标

最终系统包含 3 个节点：

```text
status_publisher  ->  /robot/status  ->  status_monitor
reset_alarm_server <- /reset_alarm
```

功能：

- `status_publisher`：模拟机器人状态，发布 `/robot/status`。
- `status_monitor`：订阅 `/robot/status`，超过阈值时报警。
- `reset_alarm_server`：提供 `/reset_alarm` 服务。
- `config/status_thresholds.yaml`：配置报警阈值。
- `launch/status_system.launch.py`：一键启动。

## 第 1 步：理解 package.xml

`package.xml` 描述这个 ROS2 包需要什么依赖。

关键内容：

```xml
<depend>rclcpp</depend>
<depend>std_msgs</depend>
<depend>std_srvs</depend>
```

解释：

- `rclcpp`：ROS2 C++ 客户端库，写 C++ 节点必须用。
- `std_msgs`：标准消息包，本项目用 `std_msgs/msg/String`。
- `std_srvs`：标准服务包，本项目用 `std_srvs/srv/Trigger`。

## 第 2 步：理解 CMakeLists.txt

关键语句：

```cmake
find_package(rclcpp REQUIRED)
add_executable(status_publisher src/status_publisher.cpp)
ament_target_dependencies(status_publisher rclcpp std_msgs)
install(TARGETS status_publisher DESTINATION lib/${PROJECT_NAME})
```

解释：

- `find_package`：找到 ROS2 依赖。
- `add_executable`：编译一个节点程序。
- `ament_target_dependencies`：把 ROS2 库链接到节点。
- `install`：让 `ros2 run` 能找到这个可执行文件。

## 第 3 步：写发布者 status_publisher

核心概念：

```cpp
class StatusPublisher : public rclcpp::Node
```

解释：

- 每个 ROS2 C++ 节点通常继承 `rclcpp::Node`。
- `StatusPublisher` 是你自己定义的节点类。

发布者：

```cpp
publisher_ = create_publisher<std_msgs::msg::String>("/robot/status", 10);
```

解释：

- `create_publisher` 创建发布者。
- `std_msgs::msg::String` 是消息类型。
- `"/robot/status"` 是 topic 名称。
- `10` 是队列长度，先理解为最多缓存 10 条消息。

定时器：

```cpp
timer_ = create_wall_timer(500ms, [this]() { publishStatus(); });
```

解释：

- 每 500ms 调用一次 `publishStatus()`。
- 500ms 一次 = 2Hz。
- `[this]` 是 C++ lambda 捕获，让 lambda 可以调用类成员函数。

## 第 4 步：写订阅者 status_monitor

订阅者：

```cpp
subscription_ = create_subscription<std_msgs::msg::String>(
    "/robot/status", 10,
    [this](const std_msgs::msg::String::SharedPtr message) {
      inspect(message->data);
    });
```

解释：

- `create_subscription` 创建订阅者。
- 收到 `/robot/status` 消息后执行 lambda。
- `message->data` 是字符串内容。
- `inspect()` 负责判断是否报警。

参数：

```cpp
declare_parameter("min_battery_percent", 20.0);
declare_parameter("max_temperature_c", 42.0);
```

解释：

- `declare_parameter` 声明参数。
- 参数可以从 YAML 或命令行修改。
- 这比把阈值写死在代码里更适合工程项目。

## 第 5 步：写服务 reset_alarm_server

服务：

```cpp
service_ = create_service<std_srvs::srv::Trigger>("/reset_alarm", callback);
```

解释：

- Service 适合“一次请求，一次响应”。
- `Trigger` 是无请求参数、返回 `success/message` 的简单服务。
- 重置报警、开始标定、保存地图都常用 service。

## 第 6 步：写 launch 文件

`launch/status_system.launch.py` 同时启动 3 个节点。

关键结构：

```python
Node(
    package="robot_status_system",
    executable="status_publisher",
    output="screen",
)
```

解释：

- `package`：包名。
- `executable`：CMake install 后的可执行文件名。
- `output="screen"`：日志输出到终端。

## 构建运行

```bash
mkdir -p ~/ros2_ws/src
cp -r ros2_robot_status_system ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch robot_status_system status_system.launch.py
```

## 调试命令

查看 topic：

```bash
ros2 topic list
ros2 topic echo /robot/status
```

查看服务：

```bash
ros2 service list
ros2 service call /reset_alarm std_srvs/srv/Trigger "{}"
```

查看参数：

```bash
ros2 param list
ros2 param get /status_monitor min_battery_percent
```

录包：

```bash
ros2 bag record /robot/status
ros2 bag play <bag目录>
```

## 你要自己完成的改动

- [ ] 把 `/robot/status` 改成 `/robot/health`
- [ ] 新增一个参数 `max_velocity_mps`
- [ ] 当速度超过阈值时报警
- [ ] 把发布频率从 2Hz 改成 5Hz
- [ ] README 中补充一次 `ros2 topic echo` 截图

## 验收问题

你必须能回答：

- Topic 和 Service 的区别是什么？
- 为什么报警阈值要用 Parameter？
- Launch 文件解决了什么问题？
- `rclcpp::Node` 是什么？
- `create_publisher` 和 `create_subscription` 分别做什么？

