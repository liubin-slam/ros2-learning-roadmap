# ros2_mobile_robot_description

第 5-6 周项目：两轮差速小车 URDF/Xacro 模型。

这个项目用于学习机器人建模、坐标系和 RViz2 可视化。

## 你要先学什么

1. link：机器人上的一个刚体部件。
2. joint：两个 link 之间的连接关系。
3. URDF：用 XML 描述机器人结构。
4. Xacro：带变量和宏的 URDF。
5. TF：机器人坐标系树。
6. RViz2：查看机器人模型、坐标系、传感器数据的工具。

## 去哪里学

优先看：

- `docs.ros.org -> Humble -> Tutorials -> URDF`
- `docs.ros.org -> Humble -> Tutorials -> TF2`

搜索关键词：

```text
ROS2 Humble URDF tutorial
ROS2 robot_state_publisher xacro
ROS2 RViz2 RobotModel TF
```

## 项目目标

建立一个最小差速小车：

```text
base_link
├── left_wheel_link
├── right_wheel_link
├── laser_link
└── camera_link
```

## 第 1 步：理解 link

示例：

```xml
<link name="base_link">
  <visual>
    <geometry>
      <box size="0.45 0.30 0.12"/>
    </geometry>
  </visual>
</link>
```

解释：

- `link` 表示一个机器人部件。
- `name="base_link"` 是部件名字。
- `visual` 表示在 RViz2 中怎么显示。
- `box` 表示用长方体显示底盘。

## 第 2 步：理解 joint

示例：

```xml
<joint name="camera_joint" type="fixed">
  <parent link="base_link"/>
  <child link="camera_link"/>
  <origin xyz="0.23 0 0.12" rpy="0 0 0"/>
</joint>
```

解释：

- `joint` 表示两个 link 的关系。
- `parent` 是父坐标系。
- `child` 是子坐标系。
- `origin` 表示子 link 相对父 link 的位置和姿态。
- `fixed` 表示固定连接。

## 第 3 步：理解 continuous joint

轮子关节：

```xml
<joint name="left_wheel_joint" type="continuous">
  <axis xyz="0 1 0"/>
</joint>
```

解释：

- `continuous` 表示可以一直旋转。
- `axis` 表示绕哪个轴旋转。
- 轮子一般用 continuous joint。

## 第 4 步：理解 xacro 变量

示例：

```xml
<xacro:property name="base_length" value="0.45"/>
```

解释：

- xacro 变量能避免重复写数字。
- 修改 `base_length` 后，所有引用它的地方一起变化。

## 第 5 步：理解 launch

`display.launch.py` 启动：

- `robot_state_publisher`：读取 URDF 并发布 TF。
- `joint_state_publisher_gui`：给可动关节发布状态。
- `rviz2`：打开可视化界面。

## 构建运行

```bash
mkdir -p ~/ros2_ws/src
cp -r ros2_mobile_robot_description ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch mobile_robot_description display.launch.py
```

## RViz2 操作

1. Fixed Frame 设置为 `base_link`。
2. 添加 `RobotModel`。
3. 添加 `TF`。
4. 添加 `Grid`。
5. 截图保存到 `docs/`。

## 你要自己完成的改动

- [ ] 新增一个 `imu_link`
- [ ] 把相机位置向前移动 5cm
- [ ] 改变底盘颜色
- [ ] 在 README 中画出 TF 树

## 验收问题

- link 和 joint 的区别是什么？
- base_link 是什么？
- TF 树为什么不能断？
- URDF 和 Xacro 有什么区别？
- robot_state_publisher 做什么？

