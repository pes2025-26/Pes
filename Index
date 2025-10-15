shutdown /s /f /t 5
@echo off
set count=30
set url=https://www.google.com
set delay=0    
for /L %%i in (1,1,%count%) do (
    start "" "%url%"
    timeout /t %delay% >nul
)
