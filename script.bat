for /f "tokens=*" %a in ('dir *.py /s /b') do set PYTHONPATH=%PYTHONPATH%;%~fa 

