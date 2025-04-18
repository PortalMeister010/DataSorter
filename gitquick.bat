@echo off
echo ================================
echo   Git Quick Sync für DataSorter
echo ================================
echo.

:: Schritt 1: Pull von GitHub
echo 🔄 Änderungen von GitHub holen...
git pull --rebase
echo.

:: Schritt 2: Dateien zum Commit hinzufügen
echo 📁 Änderungen für Commit vormerken...
git add .

:: Schritt 3: Prüfen ob es überhaupt Änderungen gibt
git diff --cached --quiet
IF %ERRORLEVEL% EQU 0 (
    echo ⚠️  Keine Änderungen zum Commit. Abbruch.
    pause
    exit /b
)

:: Schritt 4: Commit-Nachricht eingeben
set /p MSG=📝 Commit-Nachricht: 

:: Schritt 5: Commit und Push
git commit -m "%MSG%"
echo 🚀 Änderungen werden gepusht...
git push

echo.
echo ✅ Erfolgreich synchronisiert mit GitHub!
pause