data_lists = []


def process_move(move_command, move_flag):
    global data_lists
    output_list = move_command.split(" ")
    step = int(output_list[1])
    fromW = int(output_list[3])
    toW = int(output_list[5])
    sub_list = data_lists[fromW-1][len(data_lists[fromW-1])-step:len(data_lists[fromW-1])]
    new_from_list = data_lists[fromW-1][0:len(data_lists[fromW-1])-step]
    data_lists[fromW - 1] = new_from_list
    if move_flag == "Reverse":
        sub_list.reverse()
    new_to_list = data_lists[toW-1] + sub_list
    data_lists[toW - 1] = new_to_list


def day5_1(my_list, move_flag):
    global data_lists
    # init data
    data_lists = [['Q', 'M', 'G', 'C', 'L'], ['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'],
                  ['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'], ['J', 'F', 'D', 'V', 'Q', 'P'],
                  ['N', 'F', 'M', 'S', 'L', 'B', 'T'], ['R', 'N', 'V', 'H', 'C', 'D', 'P'],
                  ['H', 'C', 'T'], ['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'], ['Z', 'F', 'H', 'G']]

    sum_point = ""
    for x in my_list:
        process_move(x, move_flag)
    for y in data_lists:
        # print(y)
        sum_point += y[-1]
    return sum_point
