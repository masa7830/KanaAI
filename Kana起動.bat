@echo off
cd /d C:\dev\KanaAI
start "" http://127.0.0.1:5000
timeout /t 2 /nobreak >nul
python app.py
pause