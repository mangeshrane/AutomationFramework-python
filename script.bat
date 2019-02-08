@echo off 
set PYTHONPATH

for /F "tokens=*" A IN ('dir /s /b *.py') do if not defined PYTHONPATH (set "PYTHONPATH=%%A") else (set "PYTHONPATH=!PYTHONPATH!;%%A")

@echo %PYTHONPATH%