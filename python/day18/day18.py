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

def remove_air(tubes):
    # tobedo
    pass


def run(input_data):
    tubes = covert_list_data(input_data)
    tubes_result = draw_tubes(tubes)
    # remove neighbors when have, x , y, z
    res1 = sum(np.count_nonzero(np.diff(tubes_result, 1, dim, 0, 0)) for dim in [0, 1, 2])
    return res1


if __name__ == '__main__':
    # P1
    print("p1 sample")
    tmp_list_1_s = read_file_array("day18_1_s.txt")
    p1_s = run(tmp_list_1_s)
    print("pass" if p1_s == 64 else "failed")

    print("p1")
    tmp_list_1 = read_file_array("day18.txt")
    p2 = run(tmp_list_1)
    print(p2)

