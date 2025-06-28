@echo off

pip install -r requirements.txt
if not %errorlevel%==0 (
    echo "Could not successfully install packages"
    exit /b 1
)
