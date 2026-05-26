# ros2_mobile_robot_description

第 5-6 周项目：两轮差速小车 URDF/Xacro 模型。

## 功能

- `base_link`
- 左右轮
- `laser_link`
- `camera_link`
- RViz2 显示模型
- robot_state_publisher 发布 TF

## 构建运行

```bash
mkdir -p ~/ros2_ws/src
cp -r ros2_mobile_robot_description ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 launch mobile_robot_description display.launch.py
```

## 验收

- RViz2 中添加 RobotModel 和 TF
- Fixed Frame 设为 `base_link`
- 截图保存到 `docs/`

