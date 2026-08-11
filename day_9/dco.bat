@echo off

echo Adding files...
git add .

echo Committing changes...
git commit -m "Updated code"

echo Pushing to GitHub...
git push

echo.
echo ============================
echo Code pushed to GitHub!
echo ============================
pause