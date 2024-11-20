import os
from solve import read_input, get_winner


# Hauptfunktion
def main(file_path, verbose):
    # alle Werte Buchstaben in einem Dictionary speichern
    buchstaben_werte = {chr(i + 96): i for i in range(1, 27)}
    buchstaben_werte["ä"] = 27
    buchstaben_werte["ö"] = 28
    buchstaben_werte["ü"] = 29
    buchstaben_werte["ß"] = 30

    if verbose:
        print(f"\nVerarbeite Datei: {file_path}")

    # text einlesen
    text = read_input(file_path)
    # alle Zeichen, die keine Buchstaben sind nicht abspeichern und alle Buchstaben zu kleinen Buchstaben umwandeln
    text_clean = [buchstabe.lower() for buchstabe in text if buchstabe.isalpha()]

    result = get_winner(text_clean, buchstaben_werte, 0, 1)
    print(f"Ergebnis für '{file_path}': {result}")


# argparse für die Argumente verwenden
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Hopsen-Spiel zwischen Amira und Bela.")
    parser.add_argument(
        "file_path",
        nargs="?",
        type=str,
        help="Pfad zur Eingabedatei (optional). "
             "Wenn nicht angegeben, werden die Dateien hopsen1.txt bis hopsen5.txt durchlaufen.",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Ausführliche Ausgabe aktivieren"
    )
    args = parser.parse_args()

    if args.file_path:
        if os.path.exists(args.file_path):
            main(args.file_path, args.verbose)
        else:
            print(f"Datei {args.file_path} nicht gefunden.")
    else:
        # Dateien von hopsen1.txt bis hopsen5.txt durchgehen
        for i in range(1, 6):
            filename = f"Beispielaufgaben/hopsen{i}.txt"
            print(f"{i}. Beispielaufgabe")
            if os.path.exists(filename):
                main(filename, args.verbose)
            else:
                if args.verbose:
                    print(f"Datei {filename} nicht gefunden.")
