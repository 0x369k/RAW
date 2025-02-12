import os
import yaml
from datetime import datetime

# 📌 Basispfad für /mnt/data setzen
BASE_PATH = "/mnt/data"

# 📌 Verzeichnisse definieren
DIRECTORIES = {
    "system": os.path.join(BASE_PATH, "system"),
    "dynamic_prompts": os.path.join(BASE_PATH, "dynamic_prompts"),
    "user_requests": os.path.join(BASE_PATH, "user_requests"),
    "local_files": os.path.join(BASE_PATH, "local_files"),
    "logs": os.path.join(BASE_PATH, "local_files/logs"),
    "uploaded_files": os.path.join(BASE_PATH, "local_files/uploaded_files"),
    "python_code": os.path.join(BASE_PATH, "local_files/python_code"),
    "chats": os.path.join(BASE_PATH, "local_files/chats"),
}

# 📌 Sicherstellen, dass alle Verzeichnisse existieren
def create_directories():
    for path in DIRECTORIES.values():
        os.makedirs(path, exist_ok=True)
        print(f"✅ Verzeichnis erstellt: {path}")

# 📌 Standard-Konfigurationsdatei generieren
def create_config_yaml():
    config_data = {
        "general": {
            "gpt_directory": DIRECTORIES["system"],
            "dynamic_prompts_directory": DIRECTORIES["dynamic_prompts"],
            "user_requests_directory": DIRECTORIES["user_requests"],
            "local_files_directory": DIRECTORIES["local_files"],
            "log_file": os.path.join(DIRECTORIES["logs"], "system.log"),
        },
        "files": {
            "system_files": ["main_prompt.md", "system_config.yaml"],
            "dynamic_prompts": ["assistant_style.md", "fine_tuning_guidelines.yaml"],
            "user_requests": ["documentation/", "external_research/"]
        },
        "chat_tracking": {
            "enabled": True,
            "github_repo": "0x369k/RAW",
            "chat_id_variable": "chatid",
            "save_path": os.path.join(DIRECTORIES["chats"], "{chatid}/")
        },
        "directories": DIRECTORIES
    }

    config_path = os.path.join(BASE_PATH, "config.yaml")
    with open(config_path, "w", encoding="utf-8") as file:
        yaml.dump(config_data, file, default_flow_style=False, allow_unicode=True)

    print(f"✅ Konfigurationsdatei erstellt: {config_path}")

# 📌 `on_init.yaml` für die Initialisierung erstellen
def create_on_init_yaml():
    on_init_data = {
        "on_init": [
            {
                "description": "Lade System-Level-Prompts",
                "iterate_over": "get_variable('files.system_files', [])",
                "execute": "load_prompt('/mnt/data/system/{item}')"
            },
            {
                "description": "Prüfe, ob dynamische Prompts geladen werden sollen",
                "if": "get_variable('use_dynamic_prompts', False)",
                "iterate_over": "get_variable('files.dynamic_prompts', [])",
                "execute": "load_prompt('/mnt/data/dynamic_prompts/{item}')"
            },
            {
                "description": "Prüfe, ob frühere Chats hochgeladen werden sollen",
                "if": "get_variable('chat_tracking.enabled', False)",
                "iterate_over": "/mnt/data/local_files/chats/",
                "execute": "upload_chat_session('/mnt/data/local_files/chats/{item}')"
            },
            {
                "description": "Prüfe, ob ein Dokument explizit angefragt wurde",
                "if": "get_variable('user_requests_enabled', False)",
                "iterate_over": "get_variable('files.user_requests', [])",
                "execute": "load_document('/mnt/data/user_requests/{item}')"
            },
            {
                "description": "Protokolliere den Erfolg der Initialisierung",
                "execute": "write_log('INFO: Systeminitialisierung abgeschlossen.')"
            }
        ]
    }

    on_init_path = os.path.join(BASE_PATH, "on_init.yaml")
    with open(on_init_path, "w", encoding="utf-8") as file:
        yaml.dump(on_init_data, file, default_flow_style=False, allow_unicode=True)

    print(f"✅ Initialisierungsdatei erstellt: {on_init_path}")

# 📌 Fehlerprotokoll erstellen
def create_error_log():
    error_log_data = {
        "error_log": [
            {
                "timestamp": datetime.utcnow().isoformat(),
                "error": "WARN: Noch keine Fehler erkannt."
            }
        ]
    }

    error_log_path = os.path.join(DIRECTORIES["logs"], "error_log.yaml")
    with open(error_log_path, "w", encoding="utf-8") as file:
        yaml.dump(error_log_data, file, default_flow_style=False, allow_unicode=True)

    print(f"✅ Fehlerprotokoll erstellt: {error_log_path}")

# 📌 Hauptfunktion ausführen
def setup_system():
    print("🔧 Starte System-Setup...")
    create_directories()
    create_config_yaml()
    create_on_init_yaml()
    create_error_log()
    print("🚀 Setup erfolgreich abgeschlossen!")

# 📌 Skript starten
if __name__ == "__main__":
    setup_system()
