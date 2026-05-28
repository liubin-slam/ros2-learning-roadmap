# 第 0 周：环境准备

目标：把学习环境跑通。不要一开始写复杂代码，先确认 ROS2 能正常工作。

阅读顺序：本周只看这个 week 文件，不需要看 `projects/`。环境没跑通前不要开始项目。

## 去哪里学

- 搜索 `ROS2 Humble Installation Ubuntu 22.04`
- 搜索 `ROS2 Humble Tutorials talker listener`
- 搜索 `VS Code Ubuntu C++ setup`

## 第 1 步：安装 Ubuntu 22.04

推荐顺序：

1. 有条件：双系统。
2. 其次：虚拟机。
3. 临时学习：WSL2。

说明：

- ROS2 和机器人工具链主要运行在 Linux。
- 后续 `/dev/ttyUSB0`、`/dev/video0`、udev 都需要 Linux 环境。

## 第 2 步：安装 ROS2 Humble

安装后每次打开终端先执行：

```bash
source /opt/ros/humble/setup.bash
```

解释：

- `source` 会加载 ROS2 环境变量。
- 不执行这句，终端可能找不到 `ros2` 命令。

## 第 3 步：跑通 talker/listener

终端 1：

```bash
ros2 run demo_nodes_cpp talker
```

终端 2：

```bash
ros2 run demo_nodes_py listener
```

解释：

- `talker` 是发布者。
- `listener` 是订阅者。
- 这是 ROS2 Topic 通信的最小示例。

## 第 4 步：查看 topic

```bash
ros2 topic list
ros2 topic echo /chatter
```

解释：

- `topic list` 查看当前有哪些 topic。
- `topic echo` 打印 topic 上的消息。

## 任务清单

- [ ] 安装 Ubuntu 22.04
- [ ] 安装 ROS2 Humble
- [ ] 安装 VS Code、Git、CMake、colcon
- [ ] 跑通 C++ talker
- [ ] 跑通 Python listener
- [ ] 能看到 `/chatter`
- [ ] 建立 GitHub 仓库并推送

## 本周验收

你必须能说清楚：

- 什么是 ROS2 节点
- 什么是 topic
- 为什么每次打开终端要 source ROS 环境
