cd %USERPROFILE%
 
REM create the venv
 
python -m venv venv
 
REM activate the venv, install distribute, install pip, create IDLE shortcut in desktop, install PILLOW
 
venv\Scripts\activate.bat
pip install -r requirement.txt

REM Enjoy!