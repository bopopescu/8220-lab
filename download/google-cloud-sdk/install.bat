@echo off
rem Copyright 2013 Google Inc. All Rights Reserved.

echo %CmdCmdLine% | find /i "%~0" >nul
SET INTERACTIVE=%ERRORLEVEL%

echo Welcome to the Google Cloud SDK!

SETLOCAL EnableDelayedExpansion

rem install.bat lives in the root of the Cloud SDK installation directory.
SET CLOUDSDK_ROOT_DIR=%~dp0

IF "%CLOUDSDK_PYTHON%"=="" (
  SET BUNDLED_PYTHON=!CLOUDSDK_ROOT_DIR!\platform\bundledpython\python.exe
  IF EXIST !BUNDLED_PYTHON! (
    SET CLOUDSDK_PYTHON=!BUNDLED_PYTHON!
  ) ELSE (
    FOR %%i in (python.exe) do (SET CLOUDSDK_PYTHON=%%~$PATH:i)
  )
)
IF "%CLOUDSDK_PYTHON%"=="" (
  echo.
  echo To use the Google Cloud SDK, you must have Python installed and on your PATH.
  echo As an alternative, you may also set the CLOUDSDK_PYTHON environment variable
  echo to the location of your Python executable.
  "%COMSPEC%" /C exit 1
) ELSE (
  "%COMSPEC%" /C ""!CLOUDSDK_PYTHON!" "!CLOUDSDK_ROOT_DIR!\bin\bootstrapping\install.py" %*"
)

IF _%INTERACTIVE%_==_0_ (
  IF _%CLOUDSDK_CORE_DISABLE_PROMPTS%_==__ (
    echo Google Cloud SDK installer will now exit.
    PAUSE
  )
)

"%COMSPEC%" /C exit %ERRORLEVEL%
