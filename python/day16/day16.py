import collections
import copy
import numpy as np
import time
from func_utils import read_file_array

global tree_nodes, valid_rate_nodes, valid_path_nodes


def convert_line(str_line):
    tmp_out_list = str_line.split(";")
    tmp_node = tmp_out_list[0].strip()[6:8]
    tmp_rate = int(tmp_out_list[0].split("=")[1].strip())
    if "," in tmp_out_list[1]:
        tmp_nodes = [x.strip() for x in tmp_out_list[1].strip()[22:].split(",")]
    else:
        tmp_nodes = [tmp_out_list[1].strip()[22:].strip()]
    return {"name": tmp_node, "rate": tmp_rate, "nodes": tmp_nodes}


def covert_list_data(input_data):
    global tree_nodes, valid_rate_nodes, valid_path_nodes
    initial_data_list = [convert_line(x) for x in input_data]
    tree_nodes = {x["name"]: set(x["nodes"]) for x in initial_data_list}
    valid_rate_nodes = {x["name"]: x["rate"] for x in initial_data_list if x["rate"] != 0}
    valid_path_nodes = {x: {y: 1 if y in tree_nodes[x] else np.inf for y in tree_nodes} for x in
                        tree_nodes}


def shortest_move_steps(path_nodes):
    for k in path_nodes:
        for i in path_nodes:
            for j in path_nodes:
                path_nodes[i][j] = min(path_nodes[i][j], path_nodes[i][k] + path_nodes[k][j])
    return path_nodes


def dfs(run_times, start_node):
    tmp_node_path = [x for x in valid_rate_nodes]
    # print(tmp_node_path)
    visited = list()
    queue = collections.deque([(run_times, start_node, 0, visited)])
    # result_list = dict()
    max_score = 0
    while queue:
        run_times, from_node, curr_score, visited = queue.popleft()
        max_score = max(max_score, curr_score)
        # result_list.update({curr_score: visited})
        # result_list[tuple(visited)] = max(curr_score, result_list.get(tuple(visited), 0))

        if run_times <= 0:
            continue

        for x in tmp_node_path:
            # print(start_node, x, visited)
            if x in visited:
                continue
            new_run_times = run_times - valid_path_nodes[from_node][x] - 1
            if new_run_times <= 0:
                continue
            new_visited = copy.copy(visited)
            new_visited.append(x)
            new_score = curr_score + valid_rate_nodes[x] * new_run_times
            # print(new_run_times, x, new_score, new_visited)
            queue.append((new_run_times, x, new_score, new_visited))
    return max_score


def run(input_data):
    global tree_nodes, valid_rate_nodes, valid_path_nodes
    covert_list_data(input_data)
    # print(valid_rate_nodes)
    valid_path_nodes = shortest_move_steps(valid_path_nodes)
    max_score = dfs(30, "AA")
    return max_score


def dfs_refactory(run_times, start_node):
    tmp_node_path = [x for x in valid_rate_nodes]
    valid_state_nodes = {x: 1 << i for i, x in enumerate(valid_rate_nodes)}
    # print(tmp_node_path)
    queue = collections.deque([(run_times, start_node, 0, 0)])
    result_list = dict()

    while queue:
        run_times, from_node, curr_score, state = queue.popleft()
        result_list[state] = max(curr_score, result_list.get(state, 0))
        if run_times <= 0:
            continue
        for x in tmp_node_path:
            new_run_times = run_times - valid_path_nodes[from_node][x] - 1
            if valid_state_nodes[x] & state or new_run_times <= 0:
                continue
            new_score = curr_score + valid_rate_nodes[x] * new_run_times
            queue.append((new_run_times, x, new_score, valid_state_nodes[x] | state))
    return result_list


def run_2(input_data):
    global tree_nodes, valid_rate_nodes, valid_path_nodes
    covert_list_data(input_data)
    valid_path_nodes = shortest_move_steps(valid_path_nodes)
    result_list = dfs_refactory(26, "AA")
    print("result_list size:", len(result_list))
    max_score = max(y1 + y2 for x1, y1 in result_list.items()
                    for x2, y2 in result_list.items() if not x1 & x2)
    print(max_score)
    return max_score


if __name__ == '__main__':
    # P1
    print("p1 sample")
    start = time.perf_counter()
    tmp_list_1_s = read_file_array("day16_1_s.txt")
    p1_s = run(tmp_list_1_s)
    print("pass" if p1_s == 1651 else "failed")
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
    #
    print("p1")
    start = time.perf_counter()
    tmp_list_1 = read_file_array("day16.txt")
    p1 = run(tmp_list_1)
    print(p1)
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
    # # P2
    #
    print("p2 sample")
    start = time.perf_counter()
    tmp_list_2_s = read_file_array("day16_1_s.txt")
    p2_s = run_2(tmp_list_2_s)
    print("pass" if p2_s == 1707 else "failed")
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")

    print("p2")
    start = time.perf_counter()
    tmp_list_1 = read_file_array("day16.txt")
    p2 = run_2(tmp_list_1)
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
