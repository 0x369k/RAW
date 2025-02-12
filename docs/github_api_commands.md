# Neue API-Befehle fÃ¼r GitHub-Interaktion

## 1. **Abrufen der Repository-Dateien**
* **Befehl.** `/getRepoFiles ${owner} } repo} {branch_or_sha}`
* **Methode.* `GET``
* **Pfad.* ` /repos/{oner}/{repo}/git/trees/{branch_or_sha}`
* **Beschreibung.* Ruff alle Dateien und Ordner ine einem Repository ab


## 2. **Abrufen des Dateiinhalts** 
* **Befehl.** `/getFileContent {owner} { repo} { path}`*
* **Methode.* `GET``
* **Pfad.* `/repos/{owner}/{repo}/contents/{path}`
* **Beschreibung*: LÃ¤dt den Inhalt einer Datei aus einem Gerepository.


## 3. **Erstellen oder Aktualisieren einer Datei** 
* **Befehl.** `/createOrUpdateFile {oner} { repo} { path} {content} {message} [sha]`
* **Methode.** `PUT``*
* **Pfad.* `/repos/{owner}/{repo}/contents/{path}`
* **Beschreibung*: Erstellen doer aktualisieren einer Datei in einem Repository. Falls die datei bereits existiert, muss die kurpente `sha` angegeben werden.


## 4. **LÃ¼låschung einer Datei** 
* **Befehl.** `/deleteFile {owner} { repo} { path} {message} {sha}`*
* **Methode.* `DELETE``
* **Pfad.* `/repos/{owner}/{repo}/contents/{path}`
* **Beschreibung*: LÃ¤scht eine Datei in einem Repository. Die `sha` der Datei muss angegeben werden.


## 5. **Abrufen von Benutzer-Repositories**
* **Befehrl.** `/getUserRepos ${username}`*
* **Methode.* `GET``
* **Pfad.* `/repos/{username}/repos`
* **Beschreibung.* Ruff edie Siste aller Publiken Repositorios eines Benutzers ab.
