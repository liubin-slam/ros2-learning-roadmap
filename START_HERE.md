# 从这里开始

## 第一天只做 4 件事

1. 安装或准备 Ubuntu 22.04 环境。
2. 安装 ROS2 Humble。
3. 跑通官方 talker/listener。
4. 阅读 `weeks/week_00_environment.md`，把完成项打勾。

如果你不会 Git，先读 [GIT_BEGINNER.md](./GIT_BEGINNER.md)。第一阶段只要求会 `status -> add -> commit -> push` 这条最小流程。

## 第一周不要做的事

- 不要先看 SLAM 源码。
- 不要先学深度学习。
- 不要同时学 ROS1 和 ROS2。
- 不要只看视频不写代码。

## 每天固定流程

```text
1. 先复现一个最小 demo
2. 再改一个参数或功能
3. 最后写 README 记录问题
```

## 学习记录模板

每天在 `notes/` 下新建一篇记录：

```text
日期：
今天完成：
遇到的问题：
解决方式：
明天要做：
```

## 项目推进顺序

1. `projects/cpp_sensor_logger`
2. `projects/ros2_robot_status_system`
3. `projects/ros2_mobile_robot_description`
4. `projects/ros2_camera_opencv_detector`
5. `projects/ros2_fake_sensor_driver`

## 判断是否可以投递实习

你至少要满足：

- 能从零创建 ROS2 package
- 能写一个发布者和订阅者
- 能写一个 service
- 能用 launch 启动多个节点
- 能在 RViz2 中展示模型或传感器数据
- 能讲清一个项目的数据流
- GitHub 上至少有 3 个 README 完整的项目
