import socket
from dataclasses import dataclass

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


@dataclass
class SensorPacket:
    timestamp_ms: int
    temperature: float
    battery: float
    velocity: float


def parse_packet(line: str) -> SensorPacket:
    parts = line.strip().split(",")
    if len(parts) != 4:
        raise ValueError(f"expected 4 fields, got {len(parts)}")
    return SensorPacket(
        timestamp_ms=int(parts[0]),
        temperature=float(parts[1]),
        battery=float(parts[2]),
        velocity=float(parts[3]),
    )


class TcpSensorDriver(Node):
    def __init__(self):
        super().__init__("tcp_sensor_driver")
        self.declare_parameter("host", "127.0.0.1")
        self.declare_parameter("port", 9000)
        self.declare_parameter("timeout_sec", 1.0)

        self.publisher = self.create_publisher(String, "/fake_sensor/status", 10)
        self.timer = self.create_timer(0.1, self.poll)
        self.sock = None
        self.buffer = ""

    def connect(self):
        host = self.get_parameter("host").value
        port = self.get_parameter("port").value
        timeout = self.get_parameter("timeout_sec").value

        self.sock = socket.create_connection((host, port), timeout=timeout)
        self.sock.settimeout(timeout)
        self.get_logger().info(f"connected to fake sensor at {host}:{port}")

    def poll(self):
        if self.sock is None:
            try:
                self.connect()
            except OSError as error:
                self.get_logger().warning(f"connect failed: {error}")
                return

        try:
            chunk = self.sock.recv(1024).decode("utf-8")
            if not chunk:
                raise ConnectionError("server closed connection")
            self.buffer += chunk
        except (OSError, ConnectionError) as error:
            self.get_logger().warning(f"read failed: {error}")
            self.close_socket()
            return

        while "\n" in self.buffer:
            line, self.buffer = self.buffer.split("\n", 1)
            try:
                packet = parse_packet(line)
            except ValueError as error:
                self.get_logger().warning(f"drop invalid packet: {error}")
                continue

            message = String()
            message.data = (
                f"timestamp_ms={packet.timestamp_ms},"
                f"temperature={packet.temperature:.2f},"
                f"battery={packet.battery:.2f},"
                f"velocity={packet.velocity:.2f}"
            )
            self.publisher.publish(message)

    def close_socket(self):
        if self.sock is not None:
            self.sock.close()
            self.sock = None

    def destroy_node(self):
        self.close_socket()
        super().destroy_node()


def main():
    rclpy.init()
    node = TcpSensorDriver()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()

