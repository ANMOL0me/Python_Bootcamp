@echo off

echo ============================
echo       Git Auto Push
echo ============================
echo.

set /p message=Enter commit message: 

if "%message%"=="" (
    echo.
    echo Error: Commit message cannot be empty.
    pause
    exit /b
)

echo.
echo Adding files...
git add .

echo.
echo Committing changes...
git commit -m "%message%"

echo.
echo Pushing to GitHub...
git push origin main

echo.
echo ============================
echo       Push Complete!
echo ============================
echo ANMOL SONI
