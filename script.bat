for /f "tokens=*" %a in ('dir *.py /s /b') do echo %~fa 

