# 第 12 周：作品集、简历、面试

目标：把项目整理成能投实习的作品集，而不是只把代码放在 GitHub。

阅读顺序：先看本文件；然后整理各项目 README；最后看 `career/` 下的简历和面试材料。

## 去哪里学

搜索：

- `GitHub README project portfolio`
- `ROS developer resume project description`
- `STAR method interview project`

## 第 1 步：整理 README

每个主项目 README 必须包含：

- 项目目标
- 学习资料入口
- 数据流图
- 构建运行命令
- 关键代码解释
- 运行截图
- 常见问题
- 你自己完成的改动

## 第 2 步：整理截图

每个项目至少一张图：

- `ros2_robot_status_system`：`ros2 topic echo` 或 launch 终端截图。
- `ros2_serial_imu_driver`：`ros2 topic echo /imu/data_raw` 截图。
- `ros2_mobile_robot_description`：RViz2 模型截图。
- `ros2_camera_opencv_detector`：检测结果截图。

## 第 3 步：整理简历

先读：

```text
career/resume_project_bullets.md
```

然后根据你实际完成内容改写。不要写没有做过的东西。

## 第 4 步：准备面试表达

每个项目按这个结构讲：

```text
项目背景：
我负责什么：
系统数据流：
关键技术点：
遇到的问题：
怎么解决：
结果：
```

## 第 5 步：录演示视频

每个主项目录 2-3 分钟：

- 先展示 README
- 再运行命令
- 再展示结果
- 最后解释一个关键函数

## 任务清单

- [ ] 整理 3 个主项目 README
- [ ] 每个项目补充运行截图
- [ ] 每个项目补充架构图
- [ ] 整理简历项目描述
- [ ] 准备面试问题答案
- [ ] 录制 2-3 分钟项目演示视频

## 简历项目选择

优先放：

1. `ros2_robot_status_system`
2. `ros2_serial_imu_driver`
3. `ros2_mobile_robot_description`
4. `ros2_camera_opencv_detector` 或后续点云项目
