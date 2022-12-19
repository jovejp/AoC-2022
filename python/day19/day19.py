import collections

from func_utils import read_file_array
import re


def covert_list_data(input_data):
    data_list = [[eval(y) for y in re.findall(r"([0-9]+)", x)] for x in input_data]
    return data_list


def get_best_geodes(robot_data, run_times, curr_ore, curr_clay, curr_obsidian, curr_geode,
                    ore_robot, clay_robot, obsidian_robot, geode_robot):
    max_o_cost = max(robot_data[1], robot_data[2], robot_data[3], robot_data[5])
    queue = collections.deque([(run_times, curr_ore, curr_clay, curr_obsidian, curr_geode,
                                ore_robot, clay_robot, obsidian_robot, geode_robot)])
    visited = set()
    times = set()
    max_geodes = 0
    while queue:
        run_times, curr_ore, curr_clay, curr_obsidian, curr_geode, \
            ore_robot, clay_robot, obsidian_robot, geode_robot = queue.popleft()

        if run_times not in times:
            times.add(run_times)
            print(f'[{robot_data[0]}] Time left: {run_times:2} | Queue size: {len(queue)}')

        max_geodes = max(max_geodes, curr_geode)

        if run_times == 0:
            continue

        # remove low geodes branch

        # phase 2 very slow....need to reduce queue numbers
        key = (run_times, curr_ore, curr_clay, curr_obsidian, curr_geode,
               ore_robot, clay_robot, obsidian_robot, geode_robot)
        if key in visited:
            continue
        visited.add(key)

        # build geode_robot if can build geode, then only build geode
        if curr_obsidian >= robot_data[6] and curr_ore >= robot_data[5]:
            queue.append((run_times - 1, curr_ore - robot_data[5] + ore_robot, curr_clay + clay_robot,
                          curr_obsidian - robot_data[6] + obsidian_robot, curr_geode + geode_robot,
                          ore_robot, clay_robot, obsidian_robot, geode_robot + 1))
            continue

        # build nothing
        queue.append((run_times - 1, curr_ore + ore_robot, curr_clay + clay_robot, curr_obsidian + obsidian_robot,
                      curr_geode + geode_robot, ore_robot, clay_robot, obsidian_robot, geode_robot))

        # if last minutes even build nothing
        if run_times <= 2:
            continue

        # build ore robot
        if curr_ore >= robot_data[1] and ore_robot < max_o_cost:
            queue.append((run_times - 1, curr_ore - robot_data[1] + ore_robot, curr_clay + clay_robot,
                          curr_obsidian + obsidian_robot, curr_geode + geode_robot,
                          ore_robot + 1, clay_robot, obsidian_robot, geode_robot))

        # build clay robot
        if curr_ore >= robot_data[2] and clay_robot < robot_data[4]:
            queue.append((run_times - 1, curr_ore - robot_data[2] + ore_robot, curr_clay + clay_robot,
                          curr_obsidian + obsidian_robot, curr_geode + geode_robot,
                          ore_robot, clay_robot + 1, obsidian_robot, geode_robot))

        # build obsidian bobot
        # if last minutes even build nothing
        if (curr_obsidian + obsidian_robot < robot_data[6] and run_times == 3) or run_times <= 2:
            continue
        if curr_clay >= robot_data[4] and curr_ore >= robot_data[3] and obsidian_robot < robot_data[6]:
            queue.append((run_times - 1, curr_ore - robot_data[3] + ore_robot, curr_clay - robot_data[4] + clay_robot,
                          curr_obsidian + obsidian_robot, curr_geode + geode_robot,
                          ore_robot, clay_robot, obsidian_robot + 1, geode_robot))

    return max_geodes


def run(input_data):
    new_input_data = covert_list_data(input_data)
    total_point = 0
    for x in new_input_data:
        print("Blueprint:", x, "start")
        # blueprint, run times
        # curr_ore, curr_clay, curr_obsidian, curr_geode,
        # ore_robot, clay_robot, obsidian_robot, geode_robot
        total_point += x[0] * get_best_geodes(x, 24, 0, 0, 0, 0, 1, 0, 0, 0)
    return total_point


def run_p2(input_data):
    new_input_data = covert_list_data(input_data)
    total_point = 1
    for x in new_input_data[:3]:
        print("Blueprint:", x, "start")
        # blueprint, run times
        # curr_ore, curr_clay, curr_obsidian, curr_geode,
        # ore_robot, clay_robot, obsidian_robot, geode_robot
        total_point *= get_best_geodes(x, 32, 0, 0, 0, 0, 1, 0, 0, 0)
    return total_point


if __name__ == '__main__':
    # P1
    # print("p1 sample")
    # tmp_list_1_s = read_file_array("day19_1_s.txt")
    # p1_s = run(tmp_list_1_s)
    # print("pass" if p1_s == 33 else "failed")
    # p1
    # print("p1")
    # tmp_list_1 = read_file_array("day19.txt")
    # p1 = run(tmp_list_1)
    # print(p1)
    # p2
    print("p2")
    tmp_list_1 = read_file_array("day19.txt")
    p2 = run_p2(tmp_list_1)
    print(p2)
