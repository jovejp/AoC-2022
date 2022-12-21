import copy
import time

from func_utils import read_file_array


def covert_list_data(input_data):
    # data_list = [(x.split(":")[0].strip(), x.split(":")[1].strip()) for x in input_data]
    monkey_data = dict()
    for x in input_data:
        y = x.split(":")
        tmp_name = y[0].strip()
        tmp_value = y[1].strip()
        if tmp_value.isnumeric():
            monkey_data[tmp_name] = int(tmp_value)
        else:
            tmp_value_list = tmp_value.split(" ")
            if tmp_value_list[0].strip().isnumeric():
                tmp_value_list[0] = int(tmp_value_list[0].strip())
            else:
                tmp_value_list[0] = tmp_value_list[0].strip()
            tmp_value_list[1] = tmp_value_list[1].strip()
            if tmp_value_list[2].strip().isnumeric():
                tmp_value_list[2] = int(tmp_value_list[2].strip())
            else:
                tmp_value_list[2] = tmp_value_list[2].strip()
            monkey_data[tmp_name] = tmp_value_list
    return monkey_data


def get_monkey_value(monkey_list, monkey_name):
    monkey_value = monkey_list[monkey_name]
    if isinstance(monkey_value, int):
        return monkey_value
    else:
        # print(monkey_name, monkey_value)
        monkey_l = monkey_value[0] if isinstance(monkey_value[0], int) \
            else get_monkey_value(monkey_list, monkey_value[0])
        monkey_r = monkey_value[2] if isinstance(monkey_value[2], int) \
            else get_monkey_value(monkey_list, monkey_value[2])
        # print(monkey_l, monkey_r)
        if monkey_value[1] == "+":
            new_monkey_value = monkey_l + monkey_r
        elif monkey_value[1] == "-":
            new_monkey_value = monkey_l - monkey_r
        elif monkey_value[1] == "*":
            new_monkey_value = monkey_l * monkey_r
        elif monkey_value[1] == "/":
            new_monkey_value = monkey_l / monkey_r
        else:
            print("operation error")
        # print(new_monkey_value)
        return new_monkey_value
        # monkey_list[monkey_name] = new_monkey_value


def check_human_node(monkey_list, monkey_name):
    # print(monkey_name)
    monkey_value = monkey_list[monkey_name]
    if isinstance(monkey_value, int):
        return False
    else:
        # print(monkey_name, monkey_value)
        if "humn" in monkey_value:
            return True
        else:
            monkey_l = False if isinstance(monkey_value[0], int) \
                else check_human_node(monkey_list, monkey_value[0])
            monkey_r = False if isinstance(monkey_value[2], int) \
                else check_human_node(monkey_list, monkey_value[2])
            return monkey_l or monkey_r
    return False


def run(input_data):
    new_input_data = covert_list_data(input_data)
    root_number = int(get_monkey_value(new_input_data, "root"))
    print(root_number)
    return root_number


def run_2(input_data, l, r, reverse=False):
    new_input_data = covert_list_data(input_data)
    # print(new_input_data)
    tmp_new_data = copy.copy(new_input_data)
    for x, y in tmp_new_data.items():
        if not check_human_node(tmp_new_data, x):
            new_input_data[x] = int(get_monkey_value(tmp_new_data, x))
    # print(new_input_data)

    x = [0, 1e13]
    while True:
        mid_data = int(sum(x) // 2)
        new_input_data["humn"] = mid_data
        left_data = get_monkey_value(new_input_data, l)
        right_data = get_monkey_value(new_input_data, r)
        # print("left", left_data)
        # print("right", right_data)
        if left_data > right_data:
            if reverse:
                x[0] = mid_data
            else:
                x[1] = mid_data
        elif left_data < right_data:
            if reverse:
                x[1] = mid_data
            else:
                x[0] = mid_data
        else:
            print(mid_data)
            break
    return mid_data


if __name__ == '__main__':
    # P1
    print("p1 sample")
    tmp_list_1_s = read_file_array("day21_1_s.txt")
    p1_s = run(tmp_list_1_s)
    print("pass" if p1_s == 152 else "failed")
    # p1
    print("p1")
    start = time.perf_counter()
    tmp_list_1 = read_file_array("day21.txt")
    p1 = run(tmp_list_1)
    end = time.perf_counter()
    print("run time:", (end - start) * 1000, "milliseconds")
    # print(p1)
    # p2

    print("p2 sample")
    tmp_list_1_s = read_file_array("day21_1_s.txt")
    p1_s = run_2(tmp_list_1_s, "pppw", "sjmn")
    print("pass" if p1_s == 301 else "failed")
    print("p2")
    start = time.perf_counter()
    tmp_list_1 = read_file_array("day21.txt")
    p2 = run_2(tmp_list_1, "qntq", "qgth", reverse=True)
    end = time.perf_counter()
    print("run time:", (end - start) * 1000, "milliseconds")
    # print(p2)

# debug for forward and reverse and get roughly max values.
# new_input_data["humn"] = 0
# left_data = get_monkey_value(new_input_data, l)
# right_data = get_monkey_value(new_input_data, r)
# print("left_data", left_data)
# print("right_data", right_data)
# new_input_data["humn"] = int(1e13)
# left_data = get_monkey_value(new_input_data, l)
# right_data = get_monkey_value(new_input_data, r)
# print("left_data", left_data)
# print("right_data", right_data)
