from utility import calculate_angle


def read_goals(file_path):
    with open(file_path, "r") as file:
        num_goals, ball_radius = file.readline().strip().split()

        list_goals = []
        for line in file:
            coords_goal = tuple(int(num) for num in line.strip().split(" "))
            coords_posts = ((coords_goal[0], coords_goal[1]), (coords_goal[2], coords_goal[3]))
            list_goals.append(coords_posts)
    return int(num_goals), float(ball_radius), list_goals


def linear_ordering_test(list_goals: list[tuple[(float, float), (float, float)]]) -> bool:
    richtung = None

    for i, goal in enumerate(list_goals):
        if i == len(list_goals) - 1:
            break

        # für ein Tor berechne ich den Winkel an dem ersten Pfosten von dem Tor und dem zweiten Pfosten von dem Tor
        # und irgendeinem Pfosten vom nächsten Tor und den Winkel an dem zweiten Pfosten von dem Tor
        # und dem ersten Pfosten von dem Tor und dem anderen Pfosten von dem nächsten Tor.
        a1 = goal[1]
        x1 = goal[0]
        b1 = list_goals[i + 1][0]

        a2 = goal[0]
        x2 = goal[1]
        b2 = list_goals[i + 1][1]

        # Zur Berechnung der Winkel muss der Winkel gegen den Uhrzeigersinn beschrieben werden.
        # Wenn der erste Punkt auf der y-Achse höher ist als der zweite Punkt desselben Tors müssen die Winkel so
        # beschrieben werden, dass
        if x1[1] > x2[1]:
            angle1 = calculate_angle(b1, x1, a1)
            angle2 = calculate_angle(a2, x2, b2)
        else:
            angle1 = calculate_angle(a1, x1, b1)
            angle2 = calculate_angle(b2, x2, a2)

        # wir erhalten zwei Winkel, die zwei Tore verbinden. Wenn diese beiden Innenwinkel größer als 180° sind, wird
        # beim ersten Mal die Richtung festgelegt, und bei jedem weiteren Tor überprüft, ob die Richtung sich geändert
        # hat. Wenn die beiden Innenwinkel in jeweils andere Richtungen zeigen, bleibt die Richtung None.
        # Ab der ersten Richtungsübereinstimmung beider Innenwinkel muss jede weitere Richtungsübereinstimmung
        # der beiden Innenwinkel dieselbe Richtung vorgeben. Ansonsten ist der Pfad unmöglich. Zeigen beide Innenwinkel
        # in jeweils unterschiedliche Richtungen ist unklar, ob der Schusspfad existiert und deswegen kann er hier nicht
        # verworfen werden.
        if angle1 > 180 and angle2 > 180:
            if richtung is None:
                richtung = "backwards"

            if richtung == "forwards":
                return False

        elif angle1 < 180 and angle2 < 180:
            if richtung is None:
                richtung = "forwards"

            if richtung == "backwards":
                return False

    return True
