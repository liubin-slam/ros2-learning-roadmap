# 第 1-2 周：Linux、Git、C++、CMake

目标不是“看完 C++ 教程”，而是完成一个能编译、能运行、能解释的 C++ 小项目。

阅读顺序：先看本文件安排每天任务；当任务提到 `cpp_sensor_logger` 时，再打开 [projects/cpp_sensor_logger/README.md](../projects/cpp_sensor_logger/README.md) 看项目步骤和代码解释。

## 去哪里学

按这个顺序：

1. C++ 基础：搜索 `菜鸟教程 C++`，看变量、函数、类、文件 IO。
2. CMake：搜索 `CMake Tutorial add_executable`。
3. Linux：搜索 `鸟哥 Linux 常用命令`，只看文件、目录、进程。
4. Git：读仓库里的 [GIT_BEGINNER.md](../GIT_BEGINNER.md)。

不要一开始看复杂模板、智能指针源码、操作系统内核。

## 第 1 天：能编译一个 C++ 程序

学习：

- `#include`
- `main()`
- `std::cout`
- `return 0`

任务：

- 打开 `projects/cpp_sensor_logger/src/main.cpp`
- 先写一个 hello world
- 用 `g++` 或 CMake 编译

验收：

```bash
./cpp_sensor_logger
```

能输出文字。

## 第 2 天：理解数据结构

学习：

- `int`
- `double`
- `std::string`
- `struct`

任务：

- 写出 `SensorSample`
- 包含时间戳、温度、电量、速度
- 在 `main()` 里创建一个样本并打印

验收：

你能解释：

- 为什么温度用 `double`
- 为什么时间戳用 `long long`
- 为什么把四个字段放进一个 `struct`

## 第 3 天：理解类

学习：

- `class`
- `public`
- `private`
- 构造函数
- 成员变量

任务：

- 写 `SensorSimulator`
- 提供 `sample()` 函数
- 每调用一次生成一条数据

验收：

你能解释：

- `class` 为什么适合做模拟器
- `private` 为什么能防止外部乱改状态
- 构造函数什么时候执行

## 第 4 天：写入 CSV

学习：

- `std::ofstream`
- 文件打开失败处理
- CSV 格式

任务：

- 写 `CsvLogger`
- 构造时写入表头
- 每次 `write()` 写一行数据

验收：

运行后能看到：

```text
sensor_log.csv
```

里面有多行数据。

## 第 5 天：CMake 构建

学习：

- `CMakeLists.txt`
- `cmake -S . -B build`
- `cmake --build build`

任务：

- 不再手动用 `g++`
- 用 CMake 编译整个项目

验收：

你能解释：

- `project()` 是什么
- `add_executable()` 是什么
- `src/main.cpp` 为什么要写进 CMake

## 第 6-7 天：项目改造

必须完成这些改动：

- [ ] 把采样周期改成 50ms
- [ ] 新增电流字段 `current_a`
- [ ] 电量低于 20% 时输出报警
- [ ] README 补充运行截图和你遇到的问题
- [ ] Git 至少提交 2 次

## 最终验收

完成后你必须能独立讲清楚：

- 程序从 `main()` 开始如何运行
- `SensorSimulator` 负责什么
- `CsvLogger` 负责什么
- 数据如何从模拟器进入 CSV
- 如果文件打不开，程序会怎么处理
- 这个项目和真实机器人日志记录有什么关系
