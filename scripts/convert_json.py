import os
import json

# Basis-Prompt-Ordner
PROMPT_DIR = "prompts"

def convert_md_to_json(md_file):
    """Liest eine Markdown-Datei und speichert den Inhalt als JSON."""
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    json_data = {
        "name": os.path.splitext(os.path.basename(md_file))[0],  # Dateiname ohne .md
        "description": f"Automatisch generierter JSON-Prompt aus {os.path.basename(md_file)}",
        "instructions": content.strip()  # Entfernt unnötige Leerzeichen
    }

    json_file = md_file.replace(".md", ".json")  # JSON-Dateiname generieren
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(json_data, file, indent=4, ensure_ascii=False)

    print(f"✅ {md_file} → {json_file}")

def process_prompts():
    """Durchläuft alle Unterordner in `prompts/` und konvertiert `.md` in `.json`."""
    if not os.path.exists(PROMPT_DIR):
        print("❌ Der Ordner 'prompts/' existiert nicht!")
        return

    for root, _, files in os.walk(PROMPT_DIR):
        for file in files:
            if file.endswith(".md"):
                md_file = os.path.join(root, file)
                convert_md_to_json(md_file)

if __name__ == "__main__":
    process_prompts()
    print("🎉 Alle Markdown-Prompts wurden erfolgreich in JSON umgewandelt!")
