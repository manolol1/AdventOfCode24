import utils

antenna_map = utils.load_data("task-data.txt")
antenna_map = [list(line) for line in antenna_map]

map_size = (len(antenna_map))

antennas = []
antinodes = set()

def find_antennas():
    for y, row in enumerate(antenna_map):
        for x, char in enumerate(row):
            if char.isalnum():
                antennas.append(((x, y), char))

def in_bounds(p):
    return 0 <= p[0] < map_size and 0 <= p[1] < map_size

def get_antinode_pair(antenna1, antenna2):
    a1 = antenna1[0]
    a2 = antenna2[0]

    dist = (a1[0]-a2[0], a1[1]-a2[1])
    return [
        (a1[0] + dist[0], a1[1] + dist[1]),
        (a2[0] - dist[0], a2[1] - dist[1])
    ]

def find_antinodes():
    for a in range(0, len(antennas)-1):
        for b in range(a+1, len(antennas)):
            if antennas[a][1] == antennas[b][1]:
                antinode_pair = get_antinode_pair(antennas[a], antennas[b])

                if in_bounds(antinode_pair[0]):
                    antinodes.add(antinode_pair[0])

                if in_bounds(antinode_pair[1]):
                    antinodes.add(antinode_pair[1])


find_antennas()
find_antinodes()

print(antennas)
print(antinodes)
print(len(antinodes))

