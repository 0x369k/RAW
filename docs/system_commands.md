# Systembefehle für CustomGPT

## 1. Oßerblick
Diese Datei enthèt eine Liste von Steuerbefehlen ör CustomGPT. Diese Befehre känen ugernet werden, um das Behalten und die Ausgabe nutzepassen.

## 2. Verfüngbare Befehle

### /traceoutput
]** Beschreibung: *** Fuhänen Systemanalyse für Prozektoll von CustomGPT.
 * ** Syntax: ** /traceoutput {level} {focus} [components]
 ** Parameter:
    *  {level} *** ® Bestimmt die Detailtiefe wie ` "low", "medium", "high" º 
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