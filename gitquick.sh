#!/bin/bash

echo "=============================="
echo "  Git Quick Push (Linux/Mac)"
echo "=============================="
echo

# Schritt 1: Änderungen von GitHub holen
echo "🔄 Änderungen von GitHub abrufen..."
git pull --rebase

# Schritt 2: Dateien zum Commit hinzufügen
echo "📁 Änderungen für Commit vormerken..."
git add .

# Schritt 3: Prüfen, ob es überhaupt Änderungen gibt
if git diff --cached --quiet; then
    echo "⚠️  Keine Änderungen zum Commit. Abbruch."
    exit 0
fi

# Schritt 4: Commit-Nachricht abfragen
read -p "📝 Commit-Nachricht: " msg

# Schritt 5: Commit ausführen
git commit -m "$msg"

# Schritt 6: Push zu GitHub
echo "🚀 Änderungen werden gepusht..."
git push

echo
echo "✅ Synchronisation mit GitHub abgeschlossen!"
