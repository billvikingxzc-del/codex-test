@echo off
chcp 65001 >nul
setlocal

REM 优先使用 py 启动器，其次使用 python 命令
set "PY_CMD="
where py >nul 2>nul
if %errorlevel%==0 set "PY_CMD=py"
if not defined PY_CMD (
  where python >nul 2>nul
  if %errorlevel%==0 set "PY_CMD=python"
)

if not defined PY_CMD (
  echo [错误] 未检测到 Python 环境。
  echo.
  echo 请先安装 Python 3.10+，并勾选 "Add python.exe to PATH"。
  echo 下载地址：https://www.python.org/downloads/windows/
  echo 安装后重新打开终端再执行本脚本。
  pause
  exit /b 1
)

echo [信息] 使用解释器：%PY_CMD%

echo [1/3] 升级 pip...
%PY_CMD% -m pip install --upgrade pip
if errorlevel 1 (
  echo [错误] pip 升级失败，请检查网络或 Python 安装。
  pause
  exit /b 1
)

echo [2/3] 安装打包依赖...
%PY_CMD% -m pip install -r requirements.txt
if errorlevel 1 (
  echo [错误] 依赖安装失败，请检查网络连接或 pip 源。
  pause
  exit /b 1
)

echo [3/3] 正在生成 exe...
%PY_CMD% -m PyInstaller --noconfirm --onefile --windowed --name Calculator calculator.py
if errorlevel 1 (
  echo [错误] 打包失败。
  pause
  exit /b 1
)

echo.
echo 打包完成！exe 位于 dist\Calculator.exe
pause
