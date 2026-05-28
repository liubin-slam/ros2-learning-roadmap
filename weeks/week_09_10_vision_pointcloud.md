# 第 9-10 周：视觉或点云

默认先做视觉项目 `ros2_camera_opencv_detector`，因为普通电脑没有雷达也能完成。

阅读顺序：先看本文件安排每天任务；当任务提到视觉项目时，再打开 [projects/ros2_camera_opencv_detector/README.md](../projects/ros2_camera_opencv_detector/README.md) 看项目步骤和代码解释。

## 去哪里学

视觉方向搜索：

- `OpenCV Python VideoCapture`
- `OpenCV HSV inRange findContours`
- `ROS2 cv_bridge Python`
- `rqt_image_view ROS2`

点云方向搜索：

- `ROS2 PointCloud2 PCL tutorial`
- `PCL voxel grid filter`

## 第 1 天：OpenCV 读取摄像头

学习：

- `cv2.VideoCapture`
- `capture.read()`
- `/dev/video0`

任务：

- 先写一个纯 OpenCV 脚本读取摄像头。
- 能显示或保存一张图片。

## 第 2 天：颜色空间

学习：

- BGR
- HSV
- `cv2.cvtColor`

任务：

- 把图像从 BGR 转 HSV。
- 打印某个像素的 HSV 值。

## 第 3 天：阈值分割

学习：

- `cv2.inRange`
- mask 二值图

任务：

- 检测绿色目标。
- 调整阈值，让目标区域尽量稳定。

## 第 4 天：轮廓检测

学习：

- `cv2.findContours`
- `cv2.boundingRect`
- 面积过滤

任务：

- 找到目标外接框。
- 计算目标中心点。

## 第 5 天：ROS2 Image 发布

学习：

- `sensor_msgs/msg/Image`
- `cv_bridge`
- `rqt_image_view`

任务：

- 发布 `/camera/image_raw`
- 发布 `/camera/image_processed`

## 第 6-7 天：项目整理

任务：

- [ ] 增加参数 `camera_index`
- [ ] 增加参数 `min_area`
- [ ] README 放截图
- [ ] 解释图像链路：camera -> OpenCV -> ROS2 topic -> viewer

## 最终验收

- 能读取摄像头或视频
- 能发布处理后的图像
- 能解释 Image、PointCloud2、LaserScan 区别
- 能讲清楚 `cv_bridge` 的作用
