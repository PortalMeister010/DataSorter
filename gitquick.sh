!/bin/bash

# Automatischer Git-Commit & Push
echo "🔄 Änderungen werden erfasst..."

# Dateien zum Commit hinzufügen
git add .

# Abfrage für Commit-Nachricht
read -p "📝 Commit-Nachricht: " msg

# Commit ausführen
git commit -m "$msg"

# Änderungen pushen
git push

echo "✅ Alles erfolgreich gepusht!"