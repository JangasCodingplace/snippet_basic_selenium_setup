# Readme (DE)
Dies ist das Setup sowie die Doku für den Bot. Für die anderen Instanzen bitte ich die individuellen Readme Dateien zu beachten.

## Techstack & Packages
- Python (3.7.6)
- Selenium
- Requests
- urllib

## Setup Guide
Dieses Programm wurde unter Python 3.7.6 auf einem MacOS programmiert.

1. Clone das Repository
2. erstelle eine Virtuelle Entwicklungsumgebung (optional)
3. Installiere die im Repo liegenden Requirements
4. In Abhängigkeit des Betriebssystem muss die `settings` Datei in der Datei `bot.py` ausgetauscht werden. Beachte hierzu bei den Imports den Kommentar
5. starte das Programm durch ausführen der Datei `tinderbot.py`

### Zusatzinfo
Das Grundsetup des Projekts entstammt meinem persönlichen und öffentlichen Repository: [Basic Selenium Setup](https://github.com/JangasCodingplace/snippet_basic_selenium_setup)
Die Setups wurden zu Zwecke der späteren Konvertierung in eine App bzw. .exe Datei angepasst.

## Documentation
Es wird ein Chromebrowser auf dem System benötigt!
Bei der Erstausführung des Programms wird automatisch der richtige Chromedriver heruntergeladen. Zusätzlich werden die eigenen Browserdaten kopiert und im Projektverzeichnis gespeichert. Dies kann eine Weile dauern.

### pathes.py
In dieser Datei liegen alle relevanten URLs & xPathes. Sollte sich eine URL ändern (z.B. die des Servers in der Lokalen Entwicklung) sollte die URL dort angepasst werden

### bot.py
In dieser Datei ist die Botlogik implementiert. Der Bot ist unterteilt in einzelne Module:
- **__get_tinder** Tinder öffnen
- **__swipe** Profile Swipen
- **__get_passport** Reisepassdaten ändern
- **__write_msg** Nachrichten schreiben
- **__execute_signal** Entscheidet was der Bot als nächstes tut
- **run** führt den Bot aus - das ist die einzige Instanz die von außen aufrubar sein sollte.

### settings_win.py
Settings Datei für das Windows Betriebssystem. Hier wird der chromedriver konfiguriert.

### settings_mac.py
Settings Datei für den MacOS. Hier wird der chromedriver konfiguriert.
