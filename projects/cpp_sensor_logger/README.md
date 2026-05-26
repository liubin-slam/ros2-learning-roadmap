# cpp_sensor_logger

第 1-2 周项目：用 C++ 模拟机器人传感器数据，并写入 CSV。

## 功能

- 每 100ms 生成一条数据
- 字段：timestamp_ms、temperature_c、battery_percent、velocity_mps
- 写入 `sensor_log.csv`
- 使用 CMake 构建

## 构建运行

```bash
mkdir -p build
cd build
cmake ..
cmake --build .
./cpp_sensor_logger
```

Windows PowerShell 下可运行：

```powershell
cmake -S . -B build
cmake --build build
.\build\Debug\cpp_sensor_logger.exe
```

## 学习点

- 类和构造函数
- STL 和文件 IO
- 随机数模拟
- CMake 基础

