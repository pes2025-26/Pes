@echo off
:: Set your desired time (24-hour format)
set target_time=21:30

:wait
for /f "tokens=1-2 delims=:" %%a in ("%time%") do set current_time=%%a:%%b
if "%current_time%"=="%target_time%" (
    start https://www.google.com
    exit
)
timeout /t 30 >nul
goto wait
