import cv2
import rclpy
from cv_bridge import CvBridge
from rclpy.node import Node
from sensor_msgs.msg import Image


class ColorDetector(Node):
    def __init__(self):
        super().__init__("color_detector")
        self.declare_parameter("camera_index", 0)
        self.declare_parameter("publish_period_sec", 0.1)

        camera_index = self.get_parameter("camera_index").value
        period = self.get_parameter("publish_period_sec").value

        self.bridge = CvBridge()
        self.capture = cv2.VideoCapture(camera_index)
        if not self.capture.isOpened():
            raise RuntimeError(f"failed to open camera index {camera_index}")

        self.raw_pub = self.create_publisher(Image, "/camera/image_raw", 10)
        self.processed_pub = self.create_publisher(Image, "/camera/image_processed", 10)
        self.timer = self.create_timer(period, self.process_frame)

    def process_frame(self):
        ok, frame = self.capture.read()
        if not ok:
            self.get_logger().warning("failed to read frame")
            return

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_green = (35, 60, 60)
        upper_green = (85, 255, 255)
        mask = cv2.inRange(hsv, lower_green, upper_green)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area < 500:
                continue
            x, y, w, h = cv2.boundingRect(contour)
            cx = x + w // 2
            cy = y + h // 2
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
            self.get_logger().info(f"green target center=({cx}, {cy}), area={area:.1f}")
            break

        self.raw_pub.publish(self.bridge.cv2_to_imgmsg(frame, encoding="bgr8"))
        self.processed_pub.publish(self.bridge.cv2_to_imgmsg(frame, encoding="bgr8"))

    def destroy_node(self):
        self.capture.release()
        super().destroy_node()


def main():
    rclpy.init()
    node = ColorDetector()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

