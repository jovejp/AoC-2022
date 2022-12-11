# import time
monkey_data = []
sub_common_data = 1


class Monkey:
    monkey_index = 0
    data_list = []
    throw_times = 0
    operation = ""
    operation_value = 0
    div_num = 0
    true_monkey = 0
    false_monkey = 0


def process_org_operation(str_command):
    command_list = str_command.split(" ")
    if command_list[4].isnumeric():
        second_value = int(command_list[4])
    else:
        second_value = 0
    return command_list[3], second_value


def process_operation(command_list, old_data, second_value):
    if command_list == "+":
        return old_data + second_value
    elif command_list == "-":
        return old_data - second_value
    elif command_list == "*":
        return old_data * second_value
    else:
        print("operation command error")


def process_throw_action(worry_level):
    global monkey_data, sub_common_data
    for x in monkey_data:
        # print(x)
        tmp_data_list = x.data_list
        for data in tmp_data_list:
            x.throw_times += 1
            if x.operation_value == 0:
                second_data = data
            else:
                second_data = x.operation_value
            new_data = process_operation(x.operation, data, second_data)
            # print("new_data,", new_data, x.monkey_index, data, second_data)
            if worry_level == 1:
                new_risk_data = new_data
            else:
                new_risk_data = new_data // worry_level
            if new_risk_data >= sub_common_data:
                new_risk_data = new_risk_data % sub_common_data
            if new_risk_data % x.div_num == 0:
                monkey_data[x.true_monkey].data_list.append(new_risk_data)
            else:
                monkey_data[x.false_monkey].data_list.append(new_risk_data)
        monkey_data[x.monkey_index].data_list = []


def process_org_data(step_list):
    global monkey_data
    tmp_monkey = Monkey()
    for x in step_list:
        if x.startswith("Monkey"):
            monkey_index = int(x.split(" ")[1].strip(":").strip())
            tmp_monkey.monkey_index = monkey_index
        elif x.startswith("Starting items:"):
            start_item = x.strip("Starting items:").strip().split(",")
            if len(start_item) > 0:
                tmp_monkey.data_list = [int(x) for x in start_item]

        elif x.startswith("Operation:"):
            operation = x.strip("Operation:").strip()
            tmp_monkey.operation, tmp_monkey.operation_value = process_org_operation(operation)
        elif x.startswith("Test:"):
            tmp_monkey.div_num = int(x.strip("Test: divisible by ").strip())
        elif x.startswith("If true:"):
            tmp_monkey.true_monkey = int(x.strip("If true: throw to monkey").strip())
        elif x.startswith("If false:"):
            tmp_monkey.false_monkey = int(x.strip("If false: throw to monkey").strip())
    monkey_data.append(tmp_monkey)


def day11_1(data_list, run_round=20, worry_level=1):
    global monkey_data, sub_common_data
    monkey_data = []
    sub_common_data = 1

    for x in data_list:
        process_org_data(x)
    for x in monkey_data:
        sub_common_data = sub_common_data * x.div_num

    for round_index in range(0, run_round):
        process_throw_action(worry_level)
        round_index += 1
    monkey_inspect_index = []
    for x in monkey_data:
        monkey_inspect_index.append(x.throw_times)

    monkey_inspect_index.sort(reverse=True)
    return monkey_inspect_index[0] * monkey_inspect_index[1]
