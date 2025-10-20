@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ============================================
echo Medical Image Segmentation System
echo ============================================
echo.
echo Activating Conda environment...

:: 激活 Conda 环境
call E:\Anaconda\Scripts\activate.bat E:\Anaconda\envs\Pytorch

if errorlevel 1 (
    echo Error: Failed to activate Conda environment
    echo Please check if the path is correct: E:\Anaconda\envs\Pytorch
    pause
    exit /b 1
)

echo Environment activated successfully!
echo.
echo Starting application...
echo Please wait for browser to open automatically...
echo.

python gradio_app.py

pause
