import collections
import copy
import time
import numpy as np
from func_utils import read_file_array

global map_data, base_map, max_row, max_col


def check_node_status(node, move_steps):
    x, y = node
    flag = True
    # ">"
    tmp_next_y = y - move_steps % max_col if y - move_steps % max_col >= 0 \
        else max_col + y - move_steps % max_col
    if map_data[x][tmp_next_y] == ">":
        flag = False
    # "<"
    tmp_next_y = (y + move_steps) % max_col
    if flag and map_data[x][tmp_next_y] == "<":
        flag = False
    # "v"
    tmp_next_x = x - move_steps % max_row if x - move_steps % max_row >= 0 \
        else max_row + x - move_steps % max_row
    if flag and map_data[tmp_next_x][y] == "v":
        flag = False
    # "^"
    tmp_next_x = (x + move_steps) % max_row
    if flag and map_data[tmp_next_x][y] == "^":
        flag = False
    return flag


# def generate_one_snapshot(move_steps):
#     tmp_next_map = np.copy(base_map)
#     for x in range(max_row):
#         for y in range(max_col):
#             if map_data[x][y] == ".":
#                 continue
#             elif map_data[x][y] == ">":
#                 tmp_next_y = (y + move_steps) % max_col
#                 if tmp_next_map[x][tmp_next_y] == ".":
#                     tmp_next_map[x][tmp_next_y] = ">"
#                 else:
#                     tmp_next_map[x][tmp_next_y] = int(tmp_next_map[x][tmp_next_y]) + 1 \
#                         if tmp_next_map[x][tmp_next_y].isnumeric() else 2
#             elif map_data[x][y] == "<":
#                 tmp_next_y = y - move_steps % max_col if y - move_steps % max_col >= 0 \
#                     else max_col + y - move_steps % max_col
#                 if tmp_next_map[x][tmp_next_y] == ".":
#                     tmp_next_map[x][tmp_next_y] = "<"
#                 else:
#                     tmp_next_map[x][tmp_next_y] = int(tmp_next_map[x][tmp_next_y]) + 1 \
#                         if tmp_next_map[x][tmp_next_y].isnumeric() else 2
#
#             elif map_data[x][y] == "v":
#                 tmp_next_x = (x + move_steps) % max_row
#                 if tmp_next_map[tmp_next_x][y] == ".":
#                     tmp_next_map[tmp_next_x][y] = "v"
#                 else:
#                     tmp_next_map[tmp_next_x][y] = int(tmp_next_map[tmp_next_x][y]) + 1 \
#                         if tmp_next_map[tmp_next_x][y].isnumeric() else 2
#             elif map_data[x][y] == "^":
#                 tmp_next_x = x - move_steps % max_row if x - move_steps % max_row >= 0 \
#                     else max_row + x - move_steps % max_row
#                 if tmp_next_map[tmp_next_x][y] == ".":
#                     tmp_next_map[tmp_next_x][y] = "^"
#                 else:
#                     tmp_next_map[tmp_next_x][y] = int(tmp_next_map[tmp_next_x][y]) + 1 \
#                         if tmp_next_map[tmp_next_x][y].isnumeric() else 2
#             else:
#                 print(f"error!!!x={x}, y={y}, value={map_data[x][y]}")
#     return tmp_next_map


# def generate_all_snapshot():
#     all_maps = []
#     print(f"max_row={max_row}, max_col={max_col}")
#     for z in range(1, max_row * max_col + 1):
#         all_maps.append(generate_one_snapshot(z))
#     return all_maps


def covert_map(input_data):
    result_data = list()
    for x in input_data:
        x = x.replace("\n", "")
        tmp_line = np.array(list(x.replace("\n", "")))
        result_data.append(tmp_line)
    return result_data


def check_one_node(generated_nodes, node, run_times):
    if (run_times, node) not in generated_nodes:
        tmp_check_status = check_node_status(node, run_times)
        generated_nodes[(run_times, node)] = tmp_check_status
    else:
        tmp_check_status = generated_nodes[(run_times, node)]
    return tmp_check_status


def dfs(start_node, target_node, run_times):
    end_x, end_y = target_node
    generated_nodes = dict()
    final_path = dict()
    visited_node = set()
    while True:
        if check_one_node(generated_nodes, start_node, run_times):
            final_path[run_times] = start_node
            visited_node.add((run_times, start_node))
            break
        run_times += 1
    queue = collections.deque([(run_times + 1, start_node, final_path)])
    min_run_times = 0
    # times = set()

    while queue:
        run_times, from_node, final_path = queue.popleft()
        x, y = from_node

        # if run_times not in times:
        #     times.add(run_times)
        #     print(f' Time left: {run_times:2} | Queue size: {len(queue)}')

        tmp_visited_nodes = copy.copy(final_path)
        if x == end_x and y == end_y:
            # print(f"find!, min_run_time={run_times}")
            # print(f"find!, min_run_time={run_times}, visited_nodes={final_path}")
            min_run_times = run_times
            break

        nodes = [(x + i, y + j) for (i, j) in [(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0)]]

        for node in nodes:
            if (run_times, node) not in visited_node and 0 <= node[0] < max_row and 0 <= node[1] < max_col \
                    and check_one_node(generated_nodes, node, run_times):
                visited_node.add((run_times, node))
                tmp_visited_nodes[run_times] = node
                queue.append((run_times + 1, node, tmp_visited_nodes))
            else:
                if node == start_node:
                    queue.append((run_times + 1, node, tmp_visited_nodes))
                else:
                    continue
    return min_run_times


def run(input_data, p2_flag=False):
    global map_data, base_map, max_row, max_col
    new_input_data = covert_map(input_data)
    tmp_map_data = np.array(new_input_data)

    map_data = tmp_map_data[1:len(tmp_map_data) - 1, 1:len(tmp_map_data[0]) - 1]
    max_row = len(map_data)
    max_col = len(map_data[0])

    base_map = np.full((len(map_data), len(map_data[0])), ".")
    # start->end
    run_times = 0
    start_node = (0, 0)
    target_node = (max_row - 1, max_col - 1)
    return_value = dfs(start_node, target_node, run_times)
    print(f"1st Round: start->end={return_value}")
    if p2_flag:
        # end->start
        run_times = return_value + 1
        start_node = (max_row - 1, max_col - 1)
        target_node = (0, 0)
        return_value = dfs(start_node, target_node, run_times)
        print(f"1st Round: end->start={return_value}")
        # start->end
        run_times = return_value + 1
        start_node = (0, 0)
        target_node = (max_row - 1, max_col - 1)
        return_value = dfs(start_node, target_node, run_times)
        print(f"2nd Round: start->end={return_value}")
    return return_value


if __name__ == '__main__':
    # P1
    start = time.perf_counter()
    print("p1 sample")
    tmp_list_1_s = read_file_array("day24_1_s.txt")
    p1_s = run(tmp_list_1_s)
    print("pass" if p1_s == 18 else "failed")
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
    # p1
    print("p1")
    start = time.perf_counter()
    tmp_list_1 = read_file_array("day24.txt")
    p1 = run(tmp_list_1)
    print(p1)
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")

    # P2
    start = time.perf_counter()
    print("p2 sample")
    tmp_list_1_s = read_file_array("day24_1_s.txt")
    p1_s = run(tmp_list_1_s, True)
    print("pass" if p1_s == 54 else "failed")
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")

    print("p2")
    start = time.perf_counter()
    tmp_list_1 = read_file_array("day24.txt")
    p1 = run(tmp_list_1, True)
    print(p1)
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
