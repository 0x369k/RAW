#!/bin/bash
echo "🔄 Automatische Synchronisation mit GitHub..."

# Stelle sicher, dass wir im richtigen Repository sind
cd "$(dirname "$0")/.." || exit 1  

# Stelle sicher, dass Git auf dem neuesten Stand ist
git pull origin main --rebase  

# Füge alle Änderungen hinzu, EXKLUSIVE der Dateien aus `.gitignore`
git add .

# Falls es nichts zu committen gibt, abbrechen
if git diff --cached --quiet; then
    echo "✅ Keine Änderungen zum Commit."
    exit 0
fi

# Commit mit Standardnachricht (kann angepasst werden)
git commit -m "🔄 Automatische Synchronisation"

# Push zum Remote-Repository
git push origin main

echo "✅ Änderungen erfolgreich gepusht!"
