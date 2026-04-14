@echo off
chcp 65001 >nul

echo [1/2] 正在安装打包依赖...
python -m pip install -r requirements.txt

if errorlevel 1 (
  echo 依赖安装失败，请检查 Python / pip 环境。
  pause
  exit /b 1
)

echo [2/2] 正在生成 exe...
python -m PyInstaller --noconfirm --onefile --windowed --name Calculator calculator.py

if errorlevel 1 (
  echo 打包失败。
  pause
  exit /b 1
)

echo 打包完成！exe 位于 dist\Calculator.exe
pause
