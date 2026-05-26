from setuptools import setup

package_name = "fake_sensor_driver"

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
    description="TCP fake sensor driver for ROS2.",
    license="MIT",
    entry_points={
        "console_scripts": [
            "tcp_sensor_driver = fake_sensor_driver.tcp_sensor_driver:main",
        ],
    },
)

