from solve import read_file, calculate_solution


# Hauptfunktion mit argparse
def main(task, verbose):
    task = task.strip()
    if task == "all":
        exercises = range(0, 6)
    else:
        exercises = [int(task)]

    for ex in exercises:
        people, length, width = read_file(ex, args.verbose)

        print(f"\n\nFür Beispielaufgabe {ex}:")
        calculate_solution(length, width, people, args.verbose)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Wählen Sie eine Beispielaufgabe mit ihrer Nummer "
                                                 "oder wählen Sie 'all'.")
    parser.add_argument("-i", "--input", default="all", help="Dateipfad zur Eingabedatei")
    parser.add_argument("-v", "--verbose", action="store_true", help="Ausführliche Ausgaben anzeigen")

    args = parser.parse_args()

    if args.input not in ["all", "0", "1", "2", "3", "4", "5"]:
        raise ValueError("Invalid Input! Please choose one of the following: 0, 1, 2, 3, 4, 5, all")

    main(args.input, args.verbose)
