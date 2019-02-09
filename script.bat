@echo off

cmd /V /k For /F %%G IN ('dir /s /b *.py') do if not defined PYTHONPATH (set "PYTHONPATH=%%G") else (set PYTHONPATH=!PYTHONPATH!;%%G)
ECHO %PYTHONPATH%