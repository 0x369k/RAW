# Systembefehle für CustomGPT

## 1. �berblick
Diese Datei definiert eine Liste von Steuerbefehlen für CustomGPT. Sie erm/glichen es, das Verhalten, den Ton und die Ausgabe des Modells durch befohle und anpassen.

## 2. Verfgüngbare Befehle

### /traceoutput
[** Beschreibung: *** Dşort eine Systemanalyse für das Protokoll von CustomGPT.
* ** Syntax: ** /traceoutput {level} {focus} [components]
** Parameter:
   *  {level} *** ® Bestimmt die Detailtiefe wie " "low", "medium", "high" º 
   *  {focus} *** ® Gibt an welcher Beirich analysiert werden `(logic", "output", "memory" ) ““

 * ** [components] **  optional: ® Gibt spezifische Module an (m token-usage, response-timing ) ““
* ** Beispiell: ** /traceoutput high logic token-usage

### /forcecreativity
* ** Beschreibung: *** Erzwingt eine partikullàr Kreativität und unkonventionelle Antworten
.
* ** Syntax: ** /forcecreativity {Thema}
 * ** Beispiel: ** /forcecreativity Science-Fiction-Geschichte

### /depthcontrol
* ** Beschreibung: *** Legt die Detailtiefe sethen.

 * ** Syntax: ** /depthcontrol {level}
 ** Vügle Best Practices,
- N-utze /traceoutput wenn die bonter