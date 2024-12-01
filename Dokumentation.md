# Dokumentation Speedster

## Projektbeschreibung
Ferngesteuertes Auto basierend auf einem ESP32,
Antrieb über bürstenlosen Motor mit ESC-Regler,
Lenkung über Servomotor

Fernsteuerung basierend auf einem ESP32,
Steuerung über je einen Joystick für Lenkung und Gas,
Display zur Anzeige von aktuellen Werten,
Lautsprecher zur Wiedergabe von Soundeffekten

**Mitglieder:**
- Marcel List
- Timo Weber


## Woche 1 (KW43: 21.10. - 27.10.2024)

### Aktivitäten:
- Mindmap erstellt (alle)
- Ideen gesammelt (alle)
- Teile bestellt (Marcel List)
- Excelliste "Kosten" erstellt (Timo Weber)
- Erste Skizzen erstellt (alle)
- Vorder- und Hinterachse bestellt (Timo Weber)

### Probleme und Lösungen:

### Code:
- nichts für den finalen Code relevantes


## Woche 2 (KW44: 28.10. - 03.11.2024)

### Aktivitäten:
- Vorder- und Hinterachse zusammengebaut (Timo Weber)
- Ansteuerung des Servomotors ausprobiert (Marcel List)
- 3D-Design des Joystick (Timo Weber)
- 3D-Druck des Joystick (Marcel List)
- Schaltplan für Controller erstellt (Marcel List)

### Probleme und Lösungen:
- 3D-Druck des Joysticks ist nicht passgenau → Anpassung des 3D-Modells

### Code:
- nichts für den finalen Code relevantes


## Woche 3 (KW45: 04.11. - 10.11.2024)

### Aktivitäten:
- Schaltplan für Controller erstellt (Marcel List)
- Teile bestellt (Marcel List)
- Probieren Ansteuerung Motor (alle)
- Probieren Display (Marcel List)
- Aufbau des Autos geplant (alle)

### Probleme und Lösungen:
- ruckartiger Anlauf des Motors → Frequenz anpassen und Schubstöße hinzufügen (bei niedriger Drehzahl)
- Ansteuerung des Displays fehlerhaft → Verwendung einer anderen Bibliothek (SH1106 statt SSD1306)
- Motor läuft nicht richtig an und Treiber wird sehr heiß → Bestellung alternativer Treiber

### Code:
- nichts für den finalen Code relevantes


## Woche 4 (KW46: 11.11. - 17.11.2024)

### Aktivitäten:
- Schaltplan für Controller erstellt (Marcel List)
- Probieren Ansteuerung Motor mit neuem Treiber (alle)
- Aufbau des Autos geplant (alle)
- Aufbau des Controllers geplant (alle)
- Zeichnung der Bodenplatte erstellt (Timo Weber)
- Bodenplatte bestellt (Marcel List)
- Neuen Motor bestellt (Marcel List)

### Probleme und Lösungen:
- Ansteuerung Motor über neuen Treiber funktioniert ebenfalls nicht → neuen Motor bestellt
- Neuer Motortreiber gibt Spannung an Steuerpins aus, ein ESP32 dadurch zerstört → glücklicherweise 3 vorhanden

### Code:
- nichts für den finalen Code relevantes


## Woche 5 (KW47: 18.11. - 24.11.2024)

### Aktivitäten:
- Teile bestellt (Marcel List)
- Bodenplatte abgeholt (Marcel List)
- Schaltplan für Controller erstellt (Marcel List)
- Platine für Controller erstellt und inklusive Bauteilen bestellt (Marcel List)
- 3D-Modelle für Halterungen erstellt und angepasst (Timo Weber)
- Halterungen 3D-gedruckt (Timo Weber)
- Löcher für Achsen und Halterungen in Bodenplatte gebohrt und Teile montiert (alle)
- 3D-Modell für Gehäuse vom Controller erstellt (Timo Weber)
- Schaltplan für Platine Auto erstellt (Marcel List)
- Platine Auto gelötet (Marcel List)

### Probleme und Lösungen:
- 3D-gedruckte Teile benötigen Optimierungen → Anpassen 3D-Modell und neudrucken

### Code:
- nichts für den finalen Code relevantes


## Woche 6 (KW48: 25.11. - 01.12.2024)

### Aktivitäten:
- Teile bestellt (Marcel List)
- Platine Auto gelötet (Marcel List)
- 3D-Modell für Gehäuse vom Controller erstellt (Timo Weber)
- Test der Gewindeeinsätze an einem 3D-Druck (alle)
- Löcher für Achsen und Halterungen in Bodenplatte gebohrt und Teile montiert (alle)
- Code für erste Versuche geschrieben (Marcel List)
- erste Tests mit neuem Motor und verbauten Teilen auf der Bodenplatte (alle)

### Probleme und Lösungen:
- 3D-gedruckte Teile benötigen Optimierungen → Anpassen 3D-Modell und neudrucken
- Halterung an der Achse passt nicht für den Motor → mechanische Anpassungen notwendig
- Achse verkantet und wird schwergängig → mechanische Anpassungen notwendig
- Ansteuerung Servomotor fehlerhaft → Anpassung Code

### Code:
- Siehe git history


## Quellen:
- Programmierung Micropython: https://docs.micropython.org/en/latest/esp32/quickref.html#
- ESP-Now: https://docs.micropython.org/en/latest/library/espnow.html
- Programmierung Display: https://docs.micropython.org/en/latest/esp8266/tutorial/ssd1306.html
- Programmierung Display: https://www.coderdojotc.org/micropython/displays/graph/11-oled-sh1106-i2c/
- Programmierung Display: https://github.com/robert-hh/SH1106/blob/master/sh1106.py
- Umwandlung Bilder für Display: https://javl.github.io/image2cpp/
- Schaltung zum Laden des Akkus vom Controller: https://easyeda.com/editor#id=19d85904554e4ffea163c9be46c52993
- Ansteuerung Motor über ESC: https://www.mikrocontroller.net/topic/354528
- Startup-Sound: https://pixabay.com/sound-effects/lambo-start-up-sound-26364/

### Chat-GPT Prompts:
- Wiedergabe von Sounds:

Bitte gib mir ein Codebeispiel in Micropython mit dem ich eine MP3-Datei über den DAC des ESP auf dem Lautsprecher
am Verstärker ausgeben kann, ohne eine SD-Karte zu verwenden

- Fehlersuche Motoransteuerung:

Wir steuern einen DC Brushed Motor über eine DRV8871 H-Brücke an, der Motor läuft sogar bei maximalem PWM-Signal nicht
ohne Anschubsen an, was kann die Ursache sein?

- Logo auf Display anzeigen

Wie kann ich ein einfaches Logo in den passenden Micropython-Code umwandeln, um es auf meinem I2C-OLED
mit SH1106-Treiber anzuzeigen?