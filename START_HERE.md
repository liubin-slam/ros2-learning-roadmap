# 从这里开始

你不要先点 `projects/`。第一天只看这 3 个文件：

1. 当前文件：`START_HERE.md`
2. [HOW_TO_USE_THIS_REPO.md](./HOW_TO_USE_THIS_REPO.md)
3. [weeks/week_00_environment.md](./weeks/week_00_environment.md)

## 这个仓库怎么读

最简单规则：

- `weeks/`：每天看。它告诉你今天学什么、做到哪一步。
- `projects/`：week 文件让你做项目时再看。它解释代码、函数和项目步骤。
- `career/`：第 12 周整理简历和面试时再看。
- `notes/`：你每天写学习记录。

## 第一天只做 4 件事

1. 安装或准备 Ubuntu 22.04 环境。
2. 安装 ROS2 Humble。
3. 跑通官方 talker/listener。
4. 阅读 [weeks/week_00_environment.md](./weeks/week_00_environment.md)，把完成项打勾。

如果你不会 Git，先读 [GIT_BEGINNER.md](./GIT_BEGINNER.md)。第一阶段只要求会：

```text
git status -> git add -> git commit -> git push
```

## 每天固定流程

```text
1. 打开当天对应的 weeks/week_xx.md
2. 按里面的“第几天”任务学习
3. 如果它要求做项目，再打开 projects/项目名/README.md
4. 按项目 README 一步一步写代码
5. 运行项目，截图或记录输出
6. 回到 week 文件，把完成项打勾
7. 写 notes/当天记录
8. git commit
```

## 项目推进顺序

不要自己改变顺序。按下面来：

1. `projects/cpp_sensor_logger`
2. `projects/ros2_robot_status_system`
3. `projects/ros2_serial_imu_driver`
4. `projects/ros2_mobile_robot_description`
5. `projects/ros2_camera_opencv_detector`
6. `projects/ros2_fake_sensor_driver`

## 第一周不要做的事

- 不要先看 SLAM 源码。
- 不要先学深度学习。
- 不要同时学 ROS1 和 ROS2。
- 不要只看视频不写代码。
- 不要直接复制 `src/main.cpp`，要按项目 README 的步骤自己敲。

## 学习记录模板

每天在 `notes/` 下新建一篇记录：

```text
日期：
今天看了哪个 week 文件：
今天做了哪个 project：
今天完成：
遇到的问题：
解决方式：
明天要做：
```

## 判断是否可以投递实习

你至少要满足：

- 能从零创建 ROS2 package
- 能写一个发布者和订阅者
- 能写一个 service
- 能用 launch 启动多个节点
- 能在 RViz2 中展示模型或传感器数据
- 能讲清一个项目的数据流
- GitHub 上至少有 3 个 README 完整的项目

