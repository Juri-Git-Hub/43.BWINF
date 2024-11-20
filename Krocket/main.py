from solve import bruteforce_alg
from preprocess import read_goals, linear_ordering_test


def main(task):
    task = task.strip()
    if task == "all":
        exercises = range(1, 6)
    else:
        exercises = [int(task)]

    # für jede ausgewählte Beispielaufgabe das Programm durchführen
    for ex in exercises:
        num_goals, ball_radius, list_goals = read_goals(f"./Beispielaufgaben/krocket{ex}.txt")

        if not linear_ordering_test(list_goals):
            # Wenn False: unmöglich in die Kommandozeile schreiben und beenden
            print(f"\n\nThe Linear Ordering Test found misaligned goals. "
                  f"There doesn't exist a solution for exercise {ex}!")
            continue

        solution = bruteforce_alg(list_goals, ball_radius)
        if solution:
            print(f"\n\nThere exists a solution for exercise {ex}:")
            print(f"The startpoint is: {solution[0]}")
            print(f"And the direction is: {solution[1]}")
        else:
            print(f"\n\nThere doesn't exist a solution for exercise {ex}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="Task Krocket 43. BWINF",
        description="By HochgradigTalentiertWenigKrips"
    )

    parser.add_argument(
        "-i",
        "--input",
        default="all",
        help="Choose the example task by it's number or enter all"
    )
    args = parser.parse_args()

    if args.input not in ["all", "1", "2", "3", "4", "5"]:
        raise ValueError("Invalid Input! Please choose one of the following: 1, 2, 3, 4, 5, all")

    main(args.input)
