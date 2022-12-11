result_array = []
node_list = []
node_size = 0


def change_head_position(move_direction):
    if move_direction == "R":
        node_list[0].start_y += 1
    elif move_direction == "L":
        node_list[0].start_y -= 1
    elif move_direction == "U":
        node_list[0].start_x -= 1
    elif move_direction == "D":
        node_list[0].start_x += 1


def change_next_node_position(node_index):
    if node_list[node_index].start_x > node_list[node_index + 1].start_x:
        node_list[node_index + 1].start_x += 1
    elif node_list[node_index].start_x < node_list[node_index + 1].start_x:
        node_list[node_index + 1].start_x -= 1
    if node_list[node_index].start_y > node_list[node_index + 1].start_y:
        node_list[node_index + 1].start_y += 1
    elif node_list[node_index].start_y < node_list[node_index + 1].start_y:
        node_list[node_index + 1].start_y -= 1

    if node_list[node_index + 1].my_index == node_size - 2:
        result_array[node_list[node_index + 1].start_x][node_list[node_index + 1].start_y] = 1


def move_one_step(move_direction):
    global node_list
    node_index = 0
    # move head
    change_head_position(move_direction)

    # move others
    while node_index < node_size - 2:
        # print(node_index)
        # print(move_direction, node_index, node_list[node_index].start_x, node_list[node_index].start_y,
        #       node_list[node_index + 1].start_x, node_list[node_index + 1].start_y)
        if abs(node_list[node_index].start_x - node_list[node_index + 1].start_x) == 2 or abs(
                node_list[node_index].start_y - node_list[node_index + 1].start_y) == 2:
            change_next_node_position(node_index)
        elif abs(node_list[node_index].start_x - node_list[node_index + 1].start_x) > 2 or abs(
                node_list[node_index].start_y - node_list[node_index + 1].start_y) > 2:
            print("error!!!")
            print(move_direction, node_index, node_list[node_index].start_x, node_list[node_index].start_y,
                  node_list[node_index + 1].start_x, node_list[node_index + 1].start_y)
        if node_list[node_index].start_x < 0 or node_list[node_index].start_y < 0 or node_list[
            node_index + 1].start_x < 0 or node_list[node_index + 1].start_y < 0:
            print("error!!!")
            print(move_direction, node_index, node_list[node_index].start_x, node_list[node_index].start_y,
                  node_list[node_index + 1].start_x, node_list[node_index + 1].start_y)
        # else:
        #     print("no action needed")
        node_index += 1


def move_2(move_str):
    move_action = move_str.split(" ")
    move_direction = move_action[0]
    move_step = int(move_action[1])
    i = 0
    while i < move_step:
        move_one_step(move_direction)
        i += 1


class Node:
    def __init__(self, start_x, start_y, my_index):
        self.start_x = start_x
        self.start_y = start_y
        self.my_index = my_index


def day9(my_list, knot_size, base_start_x, base_start_y, step):
    global result_array, node_list, node_size
    result_array = []
    node_list = []
    node_size = knot_size + 2

    # init map
    x = 0
    while x < step:
        list_line = [0] * step
        result_array.append(list_line)
        x += 1

    result_array[base_start_x][base_start_y] = 1
    i = 0
    # init node list
    while i < node_size:
        node_tmp = Node(base_start_x, base_start_y, i)
        node_list.append(node_tmp)
        i += 1

    for move_str in my_list:
        # print(move_str)
        move_2(move_str)

    # for x in result_array:
    #     print(x)

    sum_result_array = []
    for sum_x in result_array:
        # print(sum_x)
        sum_result_array.append(sum(sum_x))
    # print(result_array)
    # print(sum_result_array)
    return sum(sum_result_array)
