from dataclasses import dataclass

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

try:
    import serial
except ImportError:
    serial = None


@dataclass
class ImuPacket:
    timestamp_ms: int
    ax: float
    ay: float
    az: float
    gx: float
    gy: float
    gz: float


def parse_imu_line(line: str) -> ImuPacket:
    parts = line.strip().split(",")
    if len(parts) != 7:
        raise ValueError(f"expected 7 fields, got {len(parts)}")

    return ImuPacket(
        timestamp_ms=int(parts[0]),
        ax=float(parts[1]),
        ay=float(parts[2]),
        az=float(parts[3]),
        gx=float(parts[4]),
        gy=float(parts[5]),
        gz=float(parts[6]),
    )


class SerialImuDriver(Node):
    def __init__(self):
        super().__init__("serial_imu_driver")
        self.declare_parameter("port", "/dev/ttyUSB0")
        self.declare_parameter("baudrate", 115200)
        self.declare_parameter("timeout_sec", 0.1)
        self.declare_parameter("frame_id", "imu_link")

        self.publisher = self.create_publisher(Imu, "/imu/data_raw", 10)
        self.serial_port = self.open_serial()
        self.timer = self.create_timer(0.01, self.poll_serial)

    def open_serial(self):
        if serial is None:
            raise RuntimeError("pyserial is not installed. Install it with: sudo apt install python3-serial")

        port = self.get_parameter("port").value
        baudrate = self.get_parameter("baudrate").value
        timeout = self.get_parameter("timeout_sec").value
        self.get_logger().info(f"opening serial port {port} at {baudrate}")
        return serial.Serial(port=port, baudrate=baudrate, timeout=timeout)

    def poll_serial(self):
        try:
            raw_line = self.serial_port.readline()
        except serial.SerialException as error:
            self.get_logger().error(f"serial read failed: {error}")
            return

        if not raw_line:
            return

        try:
            line = raw_line.decode("utf-8")
            packet = parse_imu_line(line)
        except (UnicodeDecodeError, ValueError) as error:
            self.get_logger().warning(f"drop invalid IMU line: {error}")
            return

        message = Imu()
        message.header.stamp = self.get_clock().now().to_msg()
        message.header.frame_id = self.get_parameter("frame_id").value
        message.linear_acceleration.x = packet.ax
        message.linear_acceleration.y = packet.ay
        message.linear_acceleration.z = packet.az
        message.angular_velocity.x = packet.gx
        message.angular_velocity.y = packet.gy
        message.angular_velocity.z = packet.gz
        self.publisher.publish(message)

    def destroy_node(self):
        if hasattr(self, "serial_port") and self.serial_port is not None:
            self.serial_port.close()
        super().destroy_node()


def main():
    rclpy.init()
    node = SerialImuDriver()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

