# ros2_camera_opencv_detector

第 9-10 周项目：ROS2 + OpenCV 图像检测。

## 功能

- 从摄像头读取图像
- 发布 `/camera/image_raw`
- 检测绿色目标
- 发布 `/camera/image_processed`
- 输出目标中心点日志

## 依赖

```bash
sudo apt install ros-humble-cv-bridge ros-humble-image-transport ros-humble-rqt-image-view python3-opencv
```

## 构建运行

```bash
mkdir -p ~/ros2_ws/src
cp -r ros2_camera_opencv_detector ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run camera_opencv_detector color_detector
rqt_image_view
```

