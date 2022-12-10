result_list = []
cycle_index = 0
image_list = []


def process(send_command):
    global result_list, cycle_index
    if send_command.startswith("addx"):
        command_list = send_command.split(" ")
        command_key = command_list[0]
        command_value = int(command_list[1])
        pre_value = result_list[-1]
        next_value = pre_value + command_value
        result_list.append(pre_value)
        result_list.append(next_value)
        cycle_index += 2
    else:
        result_list.append(result_list[-1])
        cycle_index += 1


def day10_1(data_list):
    global result_list, cycle_index
    result_list = [1]
    cycle_index = 1
    for x in data_list:
        process(x)
        if cycle_index > 220:
            break
    # print(cycle_index, len(result_list))
    sub_total = 0
    for i in range(20, len(result_list), 40):
        sub_total += i * result_list[i - 1]
    return sub_total


def draw_image(step=40):
    current_index = cycle_index // step
    if current_index >= len(image_list):
        tmp_list = []
        image_list.append(tmp_list)
    current_position = cycle_index % step

    if len(result_list) == 0:
        range_start = 1
    else:
        range_start = result_list[-1]
    if current_position in range(range_start - 1, range_start + 2):
        image_list[current_index].append("#")
    else:
        image_list[current_index].append(".")


def process_2(send_command):
    global result_list, cycle_index, image_list
    if send_command.startswith("addx"):
        command_list = send_command.split(" ")
        command_value = int(command_list[1])
        # Cycle 1
        draw_image()
        if len(result_list) == 0:
            result_list.append(1)
        else:
            result_list.append(result_list[-1])
        cycle_index += 1
        # cycle 2
        draw_image()
        result_list.append(result_list[-1] + command_value)
        cycle_index += 1
    else:
        draw_image()
        if len(result_list) == 0:
            result_list.append(1)
        else:
            result_list.append(result_list[-1])
        cycle_index += 1


def day10_2(data_list):
    global result_list, cycle_index, image_list
    result_list = []
    cycle_index = 0
    image_list = []
    for x in data_list:
        process_2(x)
        if cycle_index > 240:
            break
    # print(cycle_index, len(result_list))
    # sub_total = 0
    # for i in range(20, len(result_list), 40):
    #     sub_total += i * result_list[i-1]
    # return sub_total
    for x in image_list:
        # print(len(x))
        print(x)
