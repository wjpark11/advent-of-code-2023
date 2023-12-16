RACE = (54817088, 446129210351007)


def get_win_number(time: int, record: int) -> int:
    win_number = 0
    for hold_time in range(time + 1):
        distance = (time - hold_time) * hold_time
        if distance > record:
            win_number += 1
    return win_number


print(get_win_number(*RACE))
