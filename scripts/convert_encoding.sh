#!/bin/bash

# Verzeichnis mit den Dateien
WORKSPACE_DIR="/workspaces"

# Farben für die Ausgabe
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m' # Keine Farbe

# Prüfe, ob das Verzeichnis existiert
if [ ! -d "$WORKSPACE_DIR" ]; then
  echo -e "${RED}❌ Fehler: Das Verzeichnis $WORKSPACE_DIR existiert nicht!${NC}"
  exit 1
fi

echo -e "${YELLOW}🔍 Scanne Dateien in $WORKSPACE_DIR auf ISO-8859-1 Kodierung...${NC}"

# Finde alle Dateien mit ISO-8859-1 Kodierung
found_files=()
while IFS= read -r file; do
  found_files+=("$file")
done < <(find "$WORKSPACE_DIR" -type f -exec file --mime {} + | grep 'iso-8859-1' | cut -d: -f1)

# Falls keine Dateien gefunden wurden
if [ ${#found_files[@]} -eq 0 ]; then
  echo -e "${GREEN}✅ Keine Dateien mit ISO-8859-1 gefunden.${NC}"
  exit 0
fi

# Verarbeitung jeder Datei
for file in "${found_files[@]}"; do
  echo -e "${YELLOW}⚠️ Datei gefunden: ${NC}$file"
  echo -e "${YELLOW}👉 Möchtest du sie nach UTF-8 konvertieren? (y/n) ${NC}"

  # Warte auf eine einzelne Tasteingabe (kein Enter nötig)
  while true; do
    read -n 1 -s key
    if [[ "$key" == "y" || "$key" == "Y" ]]; then
      echo -e "\n🔄 ${GREEN}Konvertiere: $file${NC}"
      iconv -f ISO-8859-1 -t UTF-8 "$file" -o "$file.utf8" && mv "$file.utf8" "$file"
      echo -e "${GREEN}✅ Erfolgreich konvertiert.${NC}"
      break
    elif [[ "$key" == "n" || "$key" == "N" ]]; then
      echo -e "\n⏭️ ${RED}Überspringe: $file${NC}"
      break
    fi
  done
done

echo -e "${GREEN}🎉 Fertig!${NC}"
