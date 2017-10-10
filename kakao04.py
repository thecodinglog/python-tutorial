test_cases = []
test_cases.append((2, 10, 2, ['09:10', '09:09', '08:00'], '09:09'))
test_cases.append((1, 1, 5, ['08:00', '08:01', '08:02', '08:03'], '09:00'))
test_cases.append((2, 10, 2, ['09:10', '09:09', '08:00'], '09:09'))
test_cases.append((2, 1, 2, ['09:00', '09:00', '09:00', '09:00'], '08:59'))
test_cases.append((1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01'], '00:00'))
test_cases.append((1, 1, 1, ['23:59'], '09:00'))
test_cases.append((10, 60, 45,
                   ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59',
                    '23:59', '23:59', '23:59', '23:59', '23:59'], '18:00'))


def lazy_con(n, t, m, table):
    regular_timetable = []
    for time in table:
        tmp = time.split(':')
        regular_timetable.append(int(tmp[0]) * 60 + int(tmp[1]))
    regular_timetable.sort()

    last_bus_arrival = 9 * 60 + (n - 1) * t

    on_board_crews = []
    for bus_round in range(0, n):
        on_board_crews.clear()
        for crew in regular_timetable:
            if bus_round * t + 540 >= crew and len(on_board_crews) < m:
                on_board_crews.append(crew)
            else:
                break

        if len(on_board_crews) > 0:
            del regular_timetable[0:len(on_board_crews)]

    if len(on_board_crews) > 0:
        last_on_board_crew = on_board_crews[len(on_board_crews) - 1]

        if len(regular_timetable) > 0:
            last_chance_time = last_on_board_crew - 1
        elif len(on_board_crews) == m:
            last_chance_time = last_on_board_crew - 1
        else:
            last_chance_time = last_bus_arrival
    else:
        last_chance_time = last_bus_arrival

    return '{:02d}:{:02d}'.format(last_chance_time // 60, last_chance_time % 60)


def parse_tuple(case):
    print('start case : ' + str(case))
    print(lazy_con(case[0], case[1], case[2], case[3]))


for case in test_cases:
    parse_tuple(case)
