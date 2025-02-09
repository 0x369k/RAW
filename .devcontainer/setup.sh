#!/bin/bash
echo "📥 Initialisiere Codespace & synchronisiere Dateien..."

# Speicherort für temporäre Dateien innerhalb des Codespaces
DATA_DIR="${CODESPACE_VSCODE_FOLDER}/data"

# Stelle sicher, dass der Speicherordner existiert
mkdir -p "$DATA_DIR"

# Lade die Dateiliste aus GitHub
FILES=$(curl -s "https://api.github.com/repos/$GITHUB_USER/RAW/git/trees/main?recursive=1" | jq -r '.tree[] | select(.type=="blob") | .path')

# Lade jede Datei herunter & speichere sie in $DATA_DIR
for FILE in $FILES; do
    echo "📄 Lade herunter: $FILE"
    curl -s -o "$DATA_DIR/$(basename $FILE)" "https://raw.githubusercontent.com/$GITHUB_USER/RAW/main/$FILE"
done

echo "✅ Synchronisation abgeschlossen! Alle Dateien gespeichert in: $DATA_DIR"
