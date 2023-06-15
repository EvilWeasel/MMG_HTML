from bs4 import BeautifulSoup
import os

def generate_node_mappings():
    # Der Pfad zum Verzeichnis, in dem sich die HTML-Dateien befinden
    directory = './Learning-Paths/'

    # Ein leeres Dictionary, um die Daten zu speichern
    node_mappings = {}

    # Durchlaufen von allen Unterordnern im Verzeichnis
    for subdir, dirs, files in os.walk(directory):
        # Finde die eine HTML Datei in diesem Ordner
        for file in files:
            if file.endswith('.html'):
                # Extrahiere den absoluten Pfad zur Datei
                filepath = os.path.abspath(os.path.join(subdir, file))
                
                # Öffnen Sie die Datei und erstellen Sie ein BeautifulSoup-Objekt
                with open(filepath, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f.read(), 'html.parser')
                    
                    # Extrahieren Sie den Inhalt des <title>-Tags
                    title = soup.title.string
                    
                    # Speichern Sie die Daten im Dictionary
                    node_mappings[title] = filepath

    return node_mappings
