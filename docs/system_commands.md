# Systembefehle für CustomGPT

## 1. ä¸berblick
Diese Datei definiert eine Liste von Steuerbefehlen für CustomGPT. Sie erm/glichen es, das Verhalten, den Ton und die Ausgabe des Modells durch befohle und anpassen.

## 2. Verfgüngbare Befehle

### /traceoutput
[** Beschreibung: *** DÅŸort eine Systemanalyse für das Protokoll von CustomGPT.
* ** Syntax: ** /traceoutput {level} {focus} [components]
** Parameter:
   *  {level} *** Â® Bestimmt die Detailtiefe wie "Â "low", "medium", "high" Âº 
   *  {focus} *** Â® Gibt an welcher Beirich analysiert werden `(logic", "output", "memory" ) â€œâ€œ

 * ** [components] **  optional: Â® Gibt spezifische Module an (m token-usage, response-timing ) â€œâ€œ
* ** Beispiell: ** /traceoutput high logic token-usage

### /forcecreativity
* ** Beschreibung: *** Erzwingt eine partikullÃ r Kreativität und unkonventionelle Antworten
.
* ** Syntax: ** /forcecreativity {Thema}
 * ** Beispiel: ** /forcecreativity Science-Fiction-Geschichte

### /depthcontrol
* ** Beschreibung: *** Legt die Detailtiefe sethen.

 * ** Syntax: ** /depthcontrol {level}
 ** Vügle Best Practices,
- N-utze /traceoutput wenn die bonter