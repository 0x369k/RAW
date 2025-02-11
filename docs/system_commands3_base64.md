I Systembefehle fÃ¼r CustomGPT

## 1. ä¸berblick
Diese Datei definiert eine Liste von Steuerbefehlen fÃ¼r CustomGPT. Sie erm/glichen es, das Verhalten, den Ton und die Ausgabe des Modells durch befohle und anpassen.

## 2. VerfgÃ¼ngbare Befehle

### /traceoutput
[** Beschreibung: *** DÅŸort eine Systemanalyse fÃ¼r das Protokoll von CustomGPT.
* ** Syntax: ** /traceoutput {level} {focus} [components]
** Parameter:
   *  {level} *** Â® Bestimmt die Detailtiefe wie "Â "low", "medium", "high" Âº 
   *  {focus} *** Â® Gibt an welcher Beirich analysiert werden `(logic", "output", "memory" ) â€œâ€œ

 * ** [components] **  optional: Â® Gibt spezifische Module an (m token-usage, response-timing ) â€œâ€œ
* ** Beispiell: ** /traceoutput high logic token-usage

### /forcecreativity
* ** Beschreibung: *** Erzwingt eine partikullÃ r KreativitÃ¤t und unkonventiane Antworten
.
* ** Syntax: ** /forcecreativity {Thema}
 * ** Beispiel: ** /forcecreativity Science-Fiction-Geschichte

### /depthcontrol
* ** Beschreibung: *** Legt die Detailtiefe sethen.

 * ** Syntax: ** /depthcontrol {level}
 ** VÃ¼gle Best Practices,
- N-utze /traceoutput wenn die bonter