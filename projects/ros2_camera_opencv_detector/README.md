# ros2_camera_opencv_detector

第 9-10 周项目：ROS2 + OpenCV 图像检测。

这个项目用于学习相机数据如何进入 ROS2，以及如何用 OpenCV 做基础视觉处理。

## 你要先学什么

1. OpenCV 读取图像。
2. BGR 和 HSV 颜色空间。
3. 阈值分割。
4. 轮廓检测。
5. ROS2 `sensor_msgs/msg/Image`。
6. `cv_bridge`。

## 去哪里学

搜索关键词：

```text
OpenCV Python VideoCapture
OpenCV HSV inRange findContours
ROS2 cv_bridge Python image publisher
rqt_image_view ROS2
```

优先看：

- OpenCV 官方 Python tutorial：只看 `VideoCapture`、颜色空间、轮廓。
- ROS2 cv_bridge 示例。

## 项目目标

数据流：

```text
camera -> OpenCV frame -> color_detector -> /camera/image_raw
                                     └──> /camera/image_processed
```

功能：

- 从摄像头读取图像。
- 发布原始图像。
- 检测绿色目标。
- 发布处理后图像。
- 打印目标中心点。

## 第 1 步：读取摄像头

代码：

```python
self.capture = cv2.VideoCapture(camera_index)
```

解释：

- `VideoCapture(0)` 打开默认摄像头。
- Linux 下通常对应 `/dev/video0`。
- 如果打不开，先检查摄像头权限和设备。

## 第 2 步：读取一帧图像

代码：

```python
ok, frame = self.capture.read()
```

解释：

- `ok` 表示是否读取成功。
- `frame` 是 OpenCV 图像矩阵。
- OpenCV 默认颜色格式是 BGR，不是 RGB。

## 第 3 步：转换 HSV

代码：

```python
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

解释：

- HSV 更适合按颜色做阈值分割。
- H 表示色相，S 表示饱和度，V 表示亮度。

## 第 4 步：阈值分割

代码：

```python
mask = cv2.inRange(hsv, lower_green, upper_green)
```

解释：

- `lower_green` 和 `upper_green` 定义绿色范围。
- `mask` 是二值图，目标区域是白色，其他区域是黑色。

## 第 5 步：轮廓检测

代码：

```python
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

解释：

- `findContours` 找出白色区域边界。
- `RETR_EXTERNAL` 只找外层轮廓。
- `CHAIN_APPROX_SIMPLE` 压缩轮廓点，减少数据量。

## 第 6 步：转换为 ROS2 Image

代码：

```python
self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
```

解释：

- OpenCV 图像不能直接发布到 ROS2。
- `cv_bridge` 负责 OpenCV 图像和 ROS Image 消息互转。
- `bgr8` 表示每个像素 8 位 BGR 格式。

## 构建运行

```bash
sudo apt install ros-humble-cv-bridge ros-humble-image-transport ros-humble-rqt-image-view python3-opencv
mkdir -p ~/ros2_ws/src
cp -r ros2_camera_opencv_detector ~/ros2_ws/src/
cd ~/ros2_ws
colcon build
source install/setup.bash
ros2 run camera_opencv_detector color_detector
rqt_image_view
```

## 你要自己完成的改动

- [ ] 把检测颜色从绿色改成红色。
- [ ] 新增参数 `min_area` 控制最小目标面积。
- [ ] 发布目标中心点到一个新 topic。
- [ ] README 放一张检测截图。

## 验收问题

- OpenCV 的 BGR 和 RGB 有什么区别？
- 为什么颜色检测常用 HSV？
- `cv_bridge` 做什么？
- `/dev/video0` 通常是什么？
- ROS2 Image 和普通 OpenCV frame 有什么区别？

