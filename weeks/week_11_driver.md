# 第 11 周：驱动、通信、多线程

## 学习任务

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

