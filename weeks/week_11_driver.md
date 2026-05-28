# 第 11 周：驱动、通信、多线程

## 学习任务

- [ ] 复盘串口驱动：读取、切包、解析、校验、发布
- [ ] 理解 CAN 在机器人底盘中的常见用途
- [ ] TCP server/client
- [ ] 超时和断连处理
- [ ] 数据协议设计
- [ ] 驱动节点职责
- [ ] ROS2 参数配置
- [ ] 完成 `ros2_fake_sensor_driver`

## 协议约定

模拟器每行输出：

```text
timestamp_ms,temperature,battery,velocity
```

示例：

```text
1710000000000,36.5,82.0,0.42
```

## 本周验收

- driver 能解析合法数据
- driver 能丢弃非法数据
- 断连后程序不崩溃
- 能说明真实硬件驱动和模拟驱动的差异

