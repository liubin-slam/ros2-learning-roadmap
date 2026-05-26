from setuptools import setup

package_name = "camera_opencv_detector"

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
    description="ROS2 OpenCV color detector example.",
    license="MIT",
    entry_points={
        "console_scripts": [
            "color_detector = camera_opencv_detector.color_detector:main",
        ],
    },
)

