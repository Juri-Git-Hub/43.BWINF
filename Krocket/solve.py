from shapely import LineString
from utility import linear_function, check_intersection


def bruteforce_alg(list_goals, ball_radius) -> tuple:
    checked_lines = set()

    def iterate_from_middle(list_goals):
        # generator function that returns the items of the list from the middle outwards
        if not list_goals:
            return

        middle = len(list_goals) // 2
        yield list_goals[middle]

        for shift in range(1, middle + 1):
            if middle - shift >= 0:
                yield list_goals[middle - shift]
            if middle + shift < len(list_goals):
                yield list_goals[middle + shift]

    # für jeden pfosten in jedem tor jeden anderen pfosten in jedem anderen tor überprüfen
    for goal in iterate_from_middle(list_goals):
        for post in goal:
            for second_goal in list_goals:
                for second_post in second_goal:
                    if post == second_post:
                        continue

                    # get the linear function of the line
                    m, b = linear_function(post, second_post)
                    if m is None and b is None:
                        continue
                    line_identifier = (m, b)

                    if line_identifier in checked_lines:
                        continue

                    checked_lines.add(line_identifier)
                    line_works = True

                    # Check if the line passes through all goals
                    for third_goal in list_goals:
                        is_intersection, _ = check_intersection(
                            (-1e6, m * (-1e6) + b),
                            (1e6, m * 1e6 + b),
                            third_goal[0],
                            third_goal[1]
                        )
                        if not is_intersection:
                            line_works = False
                            break

                    if line_works:
                        solution = check_path((post, second_post), ball_radius, list_goals)
                        if solution:
                            return solution  # Stop after finding the first solution

    return tuple()


def check_path(line, ball_radius, list_goals) -> tuple:

    def get_goal_intersection(line, goal):
        # this function returns the intersection point of a line and a goal
        m, b = linear_function(line[0], line[1])

        is_intersection, intersection_point = check_intersection(
            (-1e6, m * (-1e6) + b),
            (1e6, m * 1e6 + b),
            goal[0],
            goal[1]
        )
        return intersection_point

    def midpoint(point1, point2):
        # this function returns the midpoint of a line
        x1, y1 = point1
        x2, y2 = point2
        return (x1 + x2) / 2, (y1 + y2) / 2

    def get_shot_solution(line1, line2, first_goal, last_goal):
        # this function returns a shot given two lines
        # the shot is the line that runs parallel and in the middle of the two other lines
        line1_first_goal = get_goal_intersection(line1, first_goal)
        line1_last_goal = get_goal_intersection(line1, last_goal)
        line2_first_goal = get_goal_intersection(line2, first_goal)
        line2_last_goal = get_goal_intersection(line2, last_goal)

        start_point = midpoint(line1_first_goal, line2_first_goal)
        direction = midpoint(line1_last_goal, line2_last_goal)

        return start_point, direction

    # this function checks if it's possible to expand the line that was found to the ball diameter
    diameter = ball_radius * 2

    # list of all possible lines (4 cases)
    possible_lines = []
    # Case 1: parallel to the left
    parallel_left = LineString(line).offset_curve(diameter)
    possible_lines.append(parallel_left)

    # Case 2: parallel to the right
    parallel_right = LineString(line).offset_curve(-diameter)
    possible_lines.append(parallel_right)

    # Case 3:
    first_point = parallel_left.coords[0]
    last_point = parallel_right.coords[1]
    case3_line1 = LineString((first_point, line[1]))
    case3_line2 = LineString((line[0], last_point))
    possible_lines.append(case3_line1)
    possible_lines.append(case3_line2)

    # Case 4:
    first_point = parallel_right.coords[0]
    last_point = parallel_left.coords[1]
    case4_line1 = LineString((first_point, line[1]))
    case4_line2 = LineString((line[0], last_point))
    possible_lines.append(case4_line1)
    possible_lines.append(case4_line2)

    working_lines = []

    # loop through every possible line
    for possible_line in possible_lines:
        line_works = True

        # get the linear function of the possible line
        m, b = linear_function(possible_line.coords[0], possible_line.coords[1])

        # iterate over every goal to check if the possible line goes through the goal
        for goal in list_goals:
            is_intersection, _ = check_intersection(
                (-1e6, m * (-1e6) + b),
                (1e6, m * 1e6 + b),
                goal[0],
                goal[1]
            )
            if not is_intersection:
                line_works = False
                break

        # if the line intersects every goal, it works
        if line_works:
            working_lines.append(possible_line)

    first_goal = list_goals[0]
    last_goal = list_goals[-1]

    # return the right lines for every case
    if parallel_right in working_lines:
        return get_shot_solution(line, parallel_right.coords, first_goal, last_goal)

    elif parallel_left in working_lines:
        return get_shot_solution(line, parallel_left.coords, first_goal, last_goal)

    elif case3_line1 in working_lines and case3_line2 in working_lines:
        return get_shot_solution(case3_line1, case3_line2, first_goal, last_goal)

    elif case4_line1 in working_lines and case4_line2 in working_lines:
        return get_shot_solution(case4_line1, case4_line2, first_goal, last_goal)

    else:
        return tuple()
