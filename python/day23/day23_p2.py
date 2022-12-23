import operator
import time
import numpy as np
from func_utils import read_file_array

global new_input_data, map_height, map_width

# N, NE, or NW
# S, SE, or SW
# W, NW, or SW
# E, NE, or SE
position_check_list = [
    [(-1, -1), (-1, 0), (-1, 1)],
    [(1, -1), (1, 0), (1, 1)],
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (0, 1), (1, 1)]]

position_all_check_list = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]


def covert_map(input_data):
    result_data = list()
    for x in input_data:
        x = x.replace("\n", "")
        tmp_line = np.array(list(x.replace("\n", "")))
        result_data.append(tmp_line)
    return result_data


def check_position(idx, idy, x, y):
    if idx + x < 0 or idx + x == map_height or idy + y < 0 or idy + y == map_width:
        print(f"error, idx+x={idx + x}, idy+y={idy + y}, map_height={map_height}, map_width={map_width}")
    if new_input_data[idx + x][idy + y] == ".":
        return True
    else:
        return False


def get_next_position(idx, idy, run_times):
    start_order = run_times % 4
    result_position = (idx, idy)
    for x in range(4):
        tmp_check_list = position_check_list[(x + start_order) % 4]
        if all(check_position(idx, idy, x, y) for x, y in tmp_check_list):
            result_position = (idx + tmp_check_list[1][0], idy + tmp_check_list[1][1])
            break
        # print(result_position)
    return result_position


def next_position(run_times):
    new_positions_dict = dict()
    not_move_list = dict()
    for idx, x in enumerate(new_input_data):
        for idy, y in enumerate(x):
            if y == "#":
                # if (idx, idy) in not_move_list:
                #     tmp_position = (idx, idy)
                # else:
                if all(check_position(idx, idy, x, y) for x, y in position_all_check_list):
                    not_move_list[(idx, idy)] = (idx, idy)
                    tmp_position = (idx, idy)
                else:
                    tmp_position = get_next_position(idx, idy, run_times)
                new_positions_dict[(idx, idy)] = tmp_position
    return new_positions_dict, not_move_list


def update_position(new_positions_dict):
    new_positions_values = new_positions_dict.values()
    for x, y in new_positions_dict.items():
        # print(x, y)
        if operator.countOf(new_positions_values, y) == 1:
            new_input_data[x[0]][x[1]] = "."
            new_input_data[y[0]][y[1]] = "#"


def run(input_data):
    global new_input_data, map_height, map_width
    tmp_input_data = covert_map(input_data)
    new_input_data = np.pad(tmp_input_data, ((100, 100), (100, 100)), 'constant', constant_values=".")
    map_height, map_width = len(new_input_data), len(new_input_data[0])
    # print(map_height, map_width)
    i = 0
    while True:
        new_positions_dict, not_move_list = next_position(i)
        print(len(new_positions_dict), len(not_move_list))
        if len(new_positions_dict) == len(not_move_list):
            print(f"completed, i={i + 1}")
            break
        update_position(new_positions_dict)
        i += 1
    return i + 1


if __name__ == '__main__':
    # P2
    start = time.perf_counter()
    print("p2 sample")
    tmp_list_1_s = read_file_array("day23_1_s.txt")
    p1_s = run(tmp_list_1_s)
    print("pass" if p1_s == 20 else "failed")
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
    # p2
    print("p2")
    start = time.perf_counter()
    tmp_list_1 = read_file_array("day23.txt")
    p1 = run(tmp_list_1)
    end = time.perf_counter()
    # print("run time:", round((end - start) * 1000), "milliseconds")
