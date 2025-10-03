@echo off
REM --- הגדרות מעודכנות לפרויקט החדש ---
SET GITHUB_USERNAME=Zevik
SET REPOSITORY_NAME=zevik-ai

git init
git add .
git commit -m "Initial project setup with all sites"
git branch -M main

REM --- קישור למאגר המרוחק החדש ---
git remote add origin https://github.com/%GITHUB_USERNAME%/%REPOSITORY_NAME%.git

REM --- דחיפה למאגר החדש ---
git push -u origin main

echo.
echo Project uploaded to zevik-ai repository!
pause