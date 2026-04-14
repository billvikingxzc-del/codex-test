# Windows 本地 EXE 计算器

这是一个可在 Windows 本地运行的图形化计算器（Tkinter）。

## 功能

- 支持 `+ - * / %` 运算
- 支持小数
- 支持清空（`C`）和退格（`⌫`）
- 支持回车（Enter）直接计算

## 运行（源码方式）

1. 安装 Python 3.10+（Windows）
2. 在当前目录执行：

```bat
python calculator.py
```

## 打包为 exe（Windows）

### 方式一：一键脚本

双击运行：

```bat
build_exe.bat
```

打包成功后，生成：

```text
dist\Calculator.exe
```

### 方式二：手动命令

```bat
python -m pip install -r requirements.txt
python -m PyInstaller --onefile --windowed --name Calculator calculator.py
```

## 目录说明

- `calculator.py`：计算器主程序
- `build_exe.bat`：Windows 一键打包脚本
- `requirements.txt`：打包依赖


## 无法直接发送 EXE 时的获取方式

当前聊天窗口通常不能直接发送二进制安装包。你可以通过以下方式拿到 `Calculator.exe`：

1. 把代码推送到你的 GitHub 仓库。
2. 打开 **Actions**，运行工作流 **Build Windows EXE**。
3. 在该次运行页面下载产物 **Calculator-windows-exe**，里面就是 `Calculator.exe`。

对应工作流文件：`.github/workflows/build-windows-exe.yml`


## 常见问题（FAQ）

### 1) 执行 `build_exe.bat` 提示缺少 Python 环境

说明系统里没有可用的 `python` / `py` 命令。

解决步骤：

1. 安装 Python 3.10+：<https://www.python.org/downloads/windows/>
2. 安装时勾选 **Add python.exe to PATH**
3. 安装完成后，关闭并重新打开 CMD/PowerShell
4. 验证：

```bat
python --version
```

或：

```bat
py --version
```

如果能看到版本号，再运行：

```bat
build_exe.bat
```
