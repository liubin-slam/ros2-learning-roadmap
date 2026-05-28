# 这个仓库到底怎么看

你之前困惑的是：到底看 `weeks/` 还是看 `projects/`。答案很明确：

```text
先看 weeks，再看 projects。
```

## 两个目录的分工

| 目录 | 作用 | 什么时候看 |
| --- | --- | --- |
| `weeks/` | 学习日程表 | 每天先看 |
| `projects/` | 项目教程和代码解释 | week 文件要求你做项目时再看 |
| `career/` | 简历和面试材料 | 第 12 周看 |
| `notes/` | 你的学习记录 | 每天写 |

## 一个具体例子

如果今天是第 1 周第 3 天：

1. 先打开 [weeks/week_01_02_cpp_cmake.md](./weeks/week_01_02_cpp_cmake.md)。
2. 找到“第 3 天：理解类”。
3. 它会要求你做 `cpp_sensor_logger`。
4. 再打开 [projects/cpp_sensor_logger/README.md](./projects/cpp_sensor_logger/README.md)。
5. 在项目 README 里看 `class SensorSimulator` 的解释。
6. 按步骤写代码。
7. 运行。
8. 回到 week 文件，把当天任务打勾。

## 每天的标准动作

```text
打开 week 文件
  -> 学当天概念
  -> 打开 project README
  -> 写代码
  -> 运行验证
  -> 记录问题
  -> git commit
```

## 不同文件回答不同问题

| 你的问题 | 去哪里找答案 |
| --- | --- |
| 我今天该学什么？ | `weeks/week_xx.md` |
| 我该去哪里找教程？ | `LEARNING_RESOURCES.md` 和对应 week 文件 |
| 这个项目怎么一步一步写？ | `projects/项目名/README.md` |
| 代码里的函数是什么意思？ | `projects/项目名/README.md` |
| Git 怎么用？ | `GIT_BEGINNER.md` |
| 简历怎么写？ | `career/resume_project_bullets.md` |
| 面试问什么？ | `career/interview_questions.md` |

## 阅读顺序总表

| 阶段 | 第一步 | 第二步 |
| --- | --- | --- |
| 第 0 周 | `weeks/week_00_environment.md` | 安装环境，没有项目 README |
| 第 1-2 周 | `weeks/week_01_02_cpp_cmake.md` | `projects/cpp_sensor_logger/README.md` |
| 第 3-4 周 | `weeks/week_03_04_ros2_communication.md` | `projects/ros2_robot_status_system/README.md` |
| 第 5-6 周 | `weeks/week_05_06_urdf_tf.md` | `projects/ros2_serial_imu_driver/README.md`，再看 `projects/ros2_mobile_robot_description/README.md` |
| 第 7-8 周 | `weeks/week_07_08_nav_sim.md` | 扩展 `ros2_mobile_robot_description` |
| 第 9-10 周 | `weeks/week_09_10_vision_pointcloud.md` | `projects/ros2_camera_opencv_detector/README.md` |
| 第 11 周 | `weeks/week_11_driver.md` | `projects/ros2_fake_sensor_driver/README.md` |
| 第 12 周 | `weeks/week_12_portfolio.md` | `career/` 下的简历和面试材料 |

## 不要这样学

不要一上来打开 `src/main.cpp` 从头复制。  
不要从 GitHub 文件树里随便点。  
不要跳过 week 文件直接看项目代码。  
不要只看视频不改代码。

## 应该这样学

每个知识点都要经过 4 步：

1. 在 week 文件里知道今天学它。
2. 在项目 README 里读解释。
3. 在代码里亲手改一处。
4. 运行验证结果。

