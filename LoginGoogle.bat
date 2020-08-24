@ECHO OFF
ECHO RODANDO O BOT
CALL %~dp0\Python\Scripts\activate
python PythonScripts\login_google.py
ECHO welcome
PAUSE
