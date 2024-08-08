@echo off
REM Check for Python installation
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python before running this script.
    exit /b 1
)

REM Remove existing virtual environment if it exists
if exist venv rmdir /s /q venv

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate

REM Install required packages
pip install -r requirements.txt

echo Setup complete. To start the application, run 'venv\Scripts\activate' and then 'python app.py'.
echo Type 'Ctrl+C' and hit Enter to stop the application. Run 'deactivate' to stop the virtual environment.
