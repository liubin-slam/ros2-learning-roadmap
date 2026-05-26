# Git 零基础使用说明

Git 的作用：记录你的代码和学习笔记每一次变化。以后你投实习时，GitHub 上的提交记录可以证明你是真做过项目，不是临时复制来的。

## 先理解 4 个词

| 词 | 含义 |
| --- | --- |
| 仓库 repo | 一个被 Git 管理的项目文件夹 |
| 暂存 add | 告诉 Git：这些文件我要保存到版本记录里 |
| 提交 commit | 保存一次版本快照，并写一句说明 |
| 推送 push | 把本地仓库上传到 GitHub |

你现在的文件夹：

```text
C:\Users\Administrator\Documents\work\ros2-learning-roadmap
```

就是学习仓库。

## 第一次使用 Git

打开 PowerShell，进入仓库：

```powershell
cd C:\Users\Administrator\Documents\work\ros2-learning-roadmap
```

查看当前状态：

```powershell
git status
```

如果提示没有配置用户名和邮箱，执行：

```powershell
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

例子：

```powershell
git config --global user.name "zhangsan"
git config --global user.email "zhangsan@example.com"
```

## 每天固定三步

每次写完代码或笔记，执行：

```powershell
git status
git add .
git commit -m "完成第0周环境准备记录"
```

这三步含义：

1. `git status`：看哪些文件变了。
2. `git add .`：把当前文件夹下的改动加入暂存区。
3. `git commit -m "..."`：保存一次版本记录。

## commit 信息怎么写

不要写：

```text
update
111
修改
```

建议写清楚你完成了什么：

```text
完成第0周环境准备清单
完成cpp_sensor_logger基础版本
添加ROS2 topic学习笔记
修复status_monitor阈值配置
补充RViz2运行截图说明
```

## 一周至少 5 次 commit

示例节奏：

| 时间 | commit 信息 |
| --- | --- |
| 周一 | 添加Linux基础命令笔记 |
| 周二 | 完成C++传感器数据结构 |
| 周三 | 添加CSV日志写入功能 |
| 周四 | 补充CMake构建说明 |
| 周五 | 完成cpp_sensor_logger README |

这样面试官能看到你持续学习，而不是最后一天一次性上传。

## 创建 GitHub 仓库并上传

先去 GitHub 新建一个空仓库，名字建议：

```text
ros2-learning-roadmap
```

不要勾选自动生成 README，因为本地已经有 README。

GitHub 创建完成后会给你一个地址，类似：

```text
https://github.com/你的用户名/ros2-learning-roadmap.git
```

然后在 PowerShell 执行：

```powershell
git remote add origin https://github.com/你的用户名/ros2-learning-roadmap.git
git branch -M main
git push -u origin main
```

以后每次本地 commit 后，只需要：

```powershell
git push
```

## 最常用命令

```powershell
git status
```

看当前有哪些改动。

```powershell
git add .
```

把所有改动加入暂存区。

```powershell
git commit -m "说明这次做了什么"
```

保存一次版本。

```powershell
git log --oneline
```

查看提交历史。

```powershell
git push
```

上传到 GitHub。

```powershell
git pull
```

从 GitHub 拉取最新内容。

## 不要手动操作 `.git` 文件夹

你在资源管理器里看到的 `.git` 文件夹是正常的。它记录 Git 的内部数据。

不要删除、移动、重命名它。平时只操作这些文件夹：

```text
career/
notes/
projects/
weeks/
```

## 出错时先做什么

先运行：

```powershell
git status
```

把输出复制出来，再判断下一步。不要随便运行网上看到的 `reset --hard`、`checkout --`，这些命令可能会丢失你的改动。

