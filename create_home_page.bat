@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo Creating home page with buttons for all sites...

(
echo ^<!DOCTYPE html^>
echo ^<html lang="en"^>
echo ^<head^>
echo     ^<meta charset="UTF-8"^>
echo     ^<meta name="viewport" content="width=device-width, initial-scale=1.0"^>
echo     ^<title^>Art Styles Gallery^</title^>
echo     ^<style^>
echo         * {
echo             margin: 0;
echo             padding: 0;
echo             box-sizing: border-box;
echo         }
echo         body {
echo             font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
echo             background: linear-gradient(135deg, #667eea 0%%, #764ba2 100%%^);
echo             min-height: 100vh;
echo             padding: 20px;
echo         }
echo         .container {
echo             max-width: 1400px;
echo             margin: 0 auto;
echo         }
echo         h1 {
echo             text-align: center;
echo             color: white;
echo             margin-bottom: 40px;
echo             font-size: 3em;
echo             text-shadow: 2px 2px 4px rgba(0,0,0,0.3^);
echo         }
echo         .buttons-grid {
echo             display: grid;
echo             grid-template-columns: repeat(auto-fill, minmax(300px, 1fr^)^);
echo             gap: 20px;
echo             padding: 20px;
echo         }
echo         .art-button {
echo             background: white;
echo             border: none;
echo             padding: 20px;
echo             border-radius: 12px;
echo             cursor: pointer;
echo             transition: all 0.3s ease;
echo             box-shadow: 0 4px 6px rgba(0,0,0,0.1^);
echo             text-decoration: none;
echo             display: block;
echo             color: #333;
echo             font-size: 1.1em;
echo             font-weight: 600;
echo             text-align: center;
echo         }
echo         .art-button:hover {
echo             transform: translateY(-5px^);
echo             box-shadow: 0 8px 15px rgba(0,0,0,0.2^);
echo             background: linear-gradient(135deg, #667eea 0%%, #764ba2 100%%^);
echo             color: white;
echo         }
echo         .art-button:active {
echo             transform: translateY(-2px^);
echo         }
echo     ^</style^>
echo ^</head^>
echo ^<body^>
echo     ^<div class="container"^>
echo         ^<h1^>🎨 Art Styles Gallery 🎨^</h1^>
echo         ^<div class="buttons-grid"^>
) > index.html

rem Process each HTML file in sites directory
for %%f in (sites\*.html) do (
    set "filename=%%~nf"
    if not "!filename!"=="index" (
        rem Replace hyphens with spaces for display
        set "displayname=!filename:-= !"
        echo             ^<a href="sites/%%~nxf" class="art-button"^>!displayname!^</a^> >> index.html
    )
)

(
echo         ^</div^>
echo     ^</div^>
echo ^</body^>
echo ^</html^>
) >> index.html

echo Home page created successfully as index.html
echo Total sites:
dir sites\*.html /b | find /c /v "" | set /p=
pause
