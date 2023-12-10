RACES = [(54, 446), (81, 1292), (70, 1035), (88, 1007)]

def get_win_number(time: int, record: int) -> int:
    win_number = 0
    for hold_time in range(time+1):
        distance = (time - hold_time) * hold_time
        if distance > record:
            win_number += 1
    return win_number

ans = 1
for race in RACES:
    ans *= get_win_number(race[0], race[1])

print(ans)