# cpp_sensor_logger

第 1-2 周项目：用 C++ 模拟机器人传感器数据，并写入 CSV 文件。

这个项目不是让你直接复制 `src/main.cpp`。你要按下面步骤自己敲一遍，每一步都理解它解决什么问题。

## 你要先学什么

按顺序学，不要跳：

1. C++ 程序基本结构：`#include`、`main()`、变量、函数、编译运行。
2. `struct`：把一组相关数据放在一起。
3. `class`：把数据和操作数据的函数放在一起。
4. 文件写入：`std::ofstream`。
5. 时间：`std::chrono`。
6. 随机数：`std::mt19937` 和 `std::uniform_real_distribution`。
7. CMake：用 `CMakeLists.txt` 管理编译。

## 去哪里学

优先使用这些资料：

- C++ 基础：搜索 `菜鸟教程 C++`，只看变量、函数、类、文件 IO。
- CMake 基础：搜索 `CMake Tutorial add_executable`。
- Linux 命令：搜索 `鸟哥 Linux 常用命令`，只看 `cd`、`ls`、`mkdir`、`cat`、`ps`。

学习要求：每看一个知识点，必须在本项目里改一行代码验证。不要只看视频。

## 项目目标

最终程序要做到：

- 每 100ms 生成一条机器人状态数据。
- 数据包括：时间戳、温度、电量、速度。
- 数据写入 `sensor_log.csv`。
- 同时在终端打印当前数据。
- 使用 CMake 编译。

输出 CSV 示例：

```text
timestamp_ms,temperature_c,battery_percent,velocity_mps
1710000000000,36.42,99.98,0.47
1710000000100,36.61,99.96,0.52
```

## 第 1 步：先写最小 C++ 程序

先只写：

```cpp
#include <iostream>

int main() {
  std::cout << "hello sensor logger\n";
  return 0;
}
```

解释：

- `#include <iostream>`：引入终端输入输出库。
- `int main()`：程序入口。程序从这里开始执行。
- `std::cout`：向终端输出文字。
- `return 0`：告诉系统程序正常结束。

验收：

```bash
g++ src/main.cpp -o cpp_sensor_logger
./cpp_sensor_logger
```

能看到 `hello sensor logger` 再进入下一步。

## 第 2 步：设计一条传感器数据

添加：

```cpp
struct SensorSample {
  long long timestamp_ms;
  double temperature_c;
  double battery_percent;
  double velocity_mps;
};
```

解释：

- `struct` 适合表示一组纯数据。
- `timestamp_ms`：毫秒时间戳。
- `double`：小数类型，适合温度、速度。
- 这个结构体相当于一行 CSV 数据。

为什么不用多个散变量：

```cpp
double temperature;
double battery;
double velocity;
```

因为后面函数传参会混乱。用 `SensorSample` 可以明确表示“这是一条完整样本”。

## 第 3 步：写传感器模拟器类

添加：

```cpp
class SensorSimulator {
public:
  SensorSample sample();

private:
  double battery_percent_{100.0};
};
```

解释：

- `class` 用来封装行为。
- `public`：外部可以调用的接口。
- `private`：内部状态，外部不能直接乱改。
- `battery_percent_{100.0}`：电量初始值是 100。
- `sample()`：每调用一次生成一条数据。

为什么这里用类：

- 传感器模拟器需要记住当前电量。
- 如果用普通函数，电量状态不好管理。

## 第 4 步：获取当前时间

核心代码：

```cpp
const auto now = std::chrono::system_clock::now();
const auto timestamp_ms =
    std::chrono::duration_cast<std::chrono::milliseconds>(
        now.time_since_epoch())
        .count();
```

解释：

- `std::chrono`：C++ 标准时间库。
- `system_clock::now()`：获取当前系统时间。
- `time_since_epoch()`：当前时间距离 1970-01-01 00:00:00 的时间长度。
- `duration_cast<std::chrono::milliseconds>`：把时间转换成毫秒。
- `.count()`：取出数字。
- `auto`：让编译器自动推断变量类型。

机器人开发里为什么要时间戳：

- 传感器数据必须知道采集时间。
- 后续 IMU、雷达、相机融合都依赖时间同步。

## 第 5 步：加入随机噪声

核心代码：

```cpp
std::mt19937 rng_;
std::uniform_real_distribution<double> temperature_noise_;
```

解释：

- `std::mt19937`：随机数生成器。
- `std::uniform_real_distribution<double>`：生成指定范围内的均匀分布小数。
- `temperature_noise_(-0.4, 0.4)`：温度噪声在 -0.4 到 0.4 之间。

为什么要加噪声：

- 真实传感器不会每次输出完全一样的数据。
- 模拟噪声能让程序更接近真实设备。

## 第 6 步：写 CSV 文件

核心代码：

```cpp
std::ofstream file_;
```

解释：

- `std::ofstream`：output file stream，用来写文件。
- 构造 `CsvLogger("sensor_log.csv")` 时打开文件。
- `file_ << ...`：把数据写入文件。

构造函数：

```cpp
explicit CsvLogger(const std::string &path) : file_(path) {
  if (!file_) {
    throw std::runtime_error("failed to open output file: " + path);
  }
  file_ << "timestamp_ms,temperature_c,battery_percent,velocity_mps\n";
}
```

解释：

- `explicit`：防止隐式类型转换，先记住这是更安全的写法。
- `const std::string &path`：传入文件路径，`&` 表示引用，避免复制字符串。
- `: file_(path)`：成员初始化列表，用 `path` 初始化文件对象。
- `if (!file_)`：检查文件是否打开失败。
- `throw std::runtime_error`：抛出运行时错误。

## 第 7 步：主循环

核心代码：

```cpp
for (int i = 0; i < 100; ++i) {
  const auto sample = simulator.sample();
  logger.write(sample);
  std::this_thread::sleep_for(std::chrono::milliseconds(100));
}
```

解释：

- `for`：循环 100 次。
- `simulator.sample()`：生成一条数据。
- `logger.write(sample)`：写入 CSV。
- `sleep_for(100ms)`：暂停 100ms，模拟 10Hz 传感器。

机器人开发里的频率概念：

- 100ms 一次 = 10Hz。
- IMU 可能是 100Hz 或 200Hz。
- 相机可能是 30Hz。
- 控制循环可能是 50Hz 或 100Hz。

## 第 8 步：异常处理

核心代码：

```cpp
try {
  // 正常逻辑
} catch (const std::exception &error) {
  std::cerr << "error: " << error.what() << '\n';
  return 1;
}
```

解释：

- `try`：包住可能失败的代码。
- `catch`：捕获错误。
- `std::exception`：C++ 标准异常基类。
- `std::cerr`：输出错误信息。
- `return 1`：告诉系统程序异常结束。

## CMakeLists.txt 解释

```cmake
cmake_minimum_required(VERSION 3.16)
project(cpp_sensor_logger)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(cpp_sensor_logger
  src/main.cpp
)
```

逐行解释：

- `cmake_minimum_required`：声明最低 CMake 版本。
- `project`：声明项目名。
- `CMAKE_CXX_STANDARD 17`：使用 C++17。
- `add_executable`：生成一个可执行程序。
- `src/main.cpp`：参与编译的源文件。

## 构建运行

Ubuntu/Linux：

```bash
mkdir -p build
cd build
cmake ..
cmake --build .
./cpp_sensor_logger
```

Windows PowerShell：

```powershell
cmake -S . -B build
cmake --build build
.\build\Debug\cpp_sensor_logger.exe
```

如果你电脑没有 `cmake`，先安装：

- Windows：安装 Visual Studio Build Tools 或 CMake 官方安装包。
- Ubuntu：`sudo apt install build-essential cmake`

## 你要自己完成的改动

完成基础版本后，按顺序改：

1. 把循环次数从 100 改成 200。
2. 把采样周期从 100ms 改成 50ms。
3. 新增一个字段 `current_a` 表示电流。
4. 当电量低于 20% 时，在终端打印 `low battery`。
5. 把输出文件名改成命令行参数。

## 验收标准

你完成本项目后，必须能回答：

- `struct` 和 `class` 有什么区别？
- 为什么传感器数据需要时间戳？
- `std::ofstream` 是做什么的？
- `std::chrono` 是做什么的？
- 10Hz 是什么意思？
- CMake 的 `add_executable` 是做什么的？

## 面试表达

可以这样写进简历：

> 使用 C++17 和 CMake 实现传感器数据模拟与 CSV 日志记录，支持温度、电量、速度等字段生成，理解采样频率、时间戳、文件 IO 和基础工程构建流程。

