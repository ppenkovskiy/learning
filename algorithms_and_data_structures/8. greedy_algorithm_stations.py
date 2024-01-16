states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az', ])

stations = {}
stations['k_one'] = set(['id', 'nv', 'ut'])
stations['k_two'] = set(['wa', 'id', 'mt'])
stations['k_three'] = set(['or', 'nv', 'ca'])
stations['k_four'] = set(['nv', 'ut'])
stations['k_five'] = set(['ca', 'az'])

final_stations = set()
i = 1

while states_needed:
    best_station = None
    states_covered = set()

    print(f"Iteration {i}")
    print(f'Final stations: {final_stations}.')
    i += 1

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # sets intersection
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(f"Iteration {i}")
print(f'Final stations: {final_stations}.')
