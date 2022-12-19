from func_utils import read_file_array
import numpy as np


def covert_list_data(input_data):
    lines = ((int(y) for y in x.split(",")) for x in input_data)
    tubes = set()
    for (x, y, z) in lines:
        tubes.add((x, y, z))
    return tubes


def draw_tubes(tubes):
    max_side = 0
    for (x, y, z) in tubes:
        max_side = max(max_side, x, y, z)
    print("max_sides", max_side)
    tubes_result = np.zeros((max_side + 1, max_side + 1, max_side + 1), np.int8)
    for x in tubes:
        tubes_result[x] = 1
    return tubes_result


def get_neighbor_cubes(tube):
    (x, y, z) = tube
    neighbor_cubes = set()
    neighbor_cubes.add((x - 1, y, z))
    neighbor_cubes.add((x + 1, y, z))
    neighbor_cubes.add((x, y - 1, z))
    neighbor_cubes.add((x, y + 1, z))
    neighbor_cubes.add((x, y, z - 1))
    neighbor_cubes.add((x, y, z + 1))
    return neighbor_cubes


def get_all_neighbor_cubes(cubes):
    neighbor_cubes = [tmp_neighbor_tube for tmp_cube in cubes for tmp_neighbor_tube in get_neighbor_cubes(tmp_cube)]
    return neighbor_cubes


def get_all_outside_nodes(cubes):
    min_x, max_x = min(x for x, _, _ in cubes), max(x for x, _, _ in cubes)
    min_y, max_y = min(y for _, y, _ in cubes), max(y for _, y, _ in cubes)
    min_z, max_z = min(z for _, _, z in cubes), max(z for _, _, z in cubes)
    # start point
    outside_cubes = {(min_x - 1, min_y - 1, min_z - 1)}
    cubes_for_check = list(outside_cubes)
    while cubes_for_check:
        for tmp_neighbor_cube in get_neighbor_cubes(cubes_for_check.pop()):
            x, y, z = tmp_neighbor_cube
            if min_x - 1 <= x <= max_x + 1 and \
                    min_y - 1 <= y <= max_y + 1 and \
                    min_z - 1 <= z <= max_z + 1 and \
                    tmp_neighbor_cube not in cubes and \
                    tmp_neighbor_cube not in outside_cubes:
                outside_cubes.add(tmp_neighbor_cube)
                cubes_for_check.append(tmp_neighbor_cube)
    return outside_cubes


def run(input_data):
    cubes = covert_list_data(input_data)
    # p1
    # tubes_result = draw_tubes(tubes)
    # remove neighbors when have, x , y, z
    # res1 = sum(np.count_nonzero(np.diff(tubes_result, 1, dim, 0, 0)) for dim in [0, 1, 2])
    # another p1
    neighbor_cubes = get_all_neighbor_cubes(cubes)
    res1 = sum(neighbor_cube not in cubes for neighbor_cube in neighbor_cubes)
    return res1


def run_p2(input_data):
    cubes = covert_list_data(input_data)
    neighbor_cubes = get_all_neighbor_cubes(cubes)
    outside_cubes = get_all_outside_nodes(cubes)
    res2 = sum(neighbor_cube in outside_cubes for neighbor_cube in neighbor_cubes)
    return res2


if __name__ == '__main__':
    # P1
    print("p1 sample")
    tmp_list_1_s = read_file_array("day18_1_s.txt")
    p1_s = run(tmp_list_1_s)
    print("pass" if p1_s == 64 else "failed")

    print("p1")
    tmp_list_1 = read_file_array("day18.txt")
    p1 = run(tmp_list_1)
    print(p1)

    # P2
    print("p2 sample")
    tmp_list_1_s = read_file_array("day18_1_s.txt")
    p2_s = run_p2(tmp_list_1_s)
    print("pass" if p2_s == 58 else "failed")

    print("p2")
    tmp_list_1 = read_file_array("day18.txt")
    p2 = run_p2(tmp_list_1)
    print(p2)
