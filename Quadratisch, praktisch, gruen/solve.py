import math


def calculate_solution(length, width, people, verbose=False):
    # Berechne die maximale Anzahl von Parzellen
    max_plots = math.ceil(1.1 * people)

    best_rows = best_columns = 0
    best_ratio = float('inf')  # Startwert für das Seitenverhältnis

    # Schleife über die Anzahl der Reihen (von 1 bis max_people)
    for rows in range(1, people + 1):
        # Berechne die Anzahl der Spalten
        columns = math.ceil(people / rows)
        total_plots = rows * columns  # Gesamtzahl der Parzellen

        # Überspringe ungültige Aufteilungen
        if total_plots < people or total_plots > max_plots:
            continue

        # Berechne die Dimensionen jeder Parzelle
        cell_length = length / rows
        cell_width = width / columns
        ratio = abs(cell_length - cell_width)  # Differenz der Seitenlängen als Maß für das Verhältnis

        # Überprüfe, ob das Seitenverhältnis besser ist
        if ratio < best_ratio:
            best_ratio = ratio
            best_rows = rows
            best_columns = columns

    # Überprüfen, ob eine gültige Aufteilung gefunden wurde
    total_plots = best_rows * best_columns
    if total_plots < people or total_plots > max_plots:
        print("[Fehler] Keine gültige Aufteilung gefunden.")
        return None

    # Berechne die endgültigen Dimensionen der Parzellen
    cell_length = length / best_rows
    cell_width = width / best_columns

    # Ausgabe der besten Aufteilung
    print(f"Beste Aufteilung: {best_rows} Reihen und {best_columns} Spalten")
    print(f"Jede Parzelle ist {cell_length:.2f} m lang und {cell_width:.2f} m breit.")
    print(f"Gesamtzahl der Parzellen: {total_plots}")


# Funktion zum Einlesen der Datei
def read_file(task, verbose=False):
    try:
        with open(f"./Beispielaufgaben/garten{task}.txt", 'r') as file:
            people = int(file.readline().strip())
            length = float(file.readline().strip())
            width = float(file.readline().strip())

        if verbose:
            print(f"Datei {task} erfolgreich gelesen mit folgenden Werten: ")
            print(f"Höhe: " + str(length))
            print(f"Breite: " + str(width))
            print(f"Personen: " + str(people))

        return people, length, width
    except Exception as e:
        print(f"Fehler beim Lesen der Datei {task}: {e}")
        return None, None, None
