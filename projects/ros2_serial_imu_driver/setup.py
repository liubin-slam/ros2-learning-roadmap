from setuptools import setup

package_name = "serial_imu_driver"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="ros2 learner",
    maintainer_email="student@example.com",
    description="ROS2 serial IMU driver example.",
    license="MIT",
    entry_points={
        "console_scripts": [
            "serial_imu_driver = serial_imu_driver.serial_imu_driver:main",
        ],
    },
)

