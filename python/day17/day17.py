from func_utils import read_file_array

shapes = (((0, 0), (0, 1), (0, 2), (0, 3)),
          ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
          ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)),
          ((0, 0), (1, 0), (2, 0), (3, 0)),
          ((0, 0), (0, 1), (1, 0), (1, 1)))
move_action_steps = ""


def check_node(floor_shape, x, y):
    return x > 0 and 0 <= y < 7 and (x, y) not in floor_shape


def check_shape(floor_shape, current_shape, x, y):
    return all(check_node(floor_shape, x + x1, y + y1) for x1, y1 in shapes[current_shape])


def move_shape(floor_shape, idx_move_str, idx_shape, max_x):
    global move_action_steps
    current_x = max_x + 5
    current_y = 2
    while check_shape(floor_shape, idx_shape, current_x - 1, current_y):
        # move down
        current_x -= 1
        # move left
        if move_action_steps[idx_move_str] == '<' \
                and check_shape(floor_shape, idx_shape, current_x, current_y - 1):
            current_y -= 1
        # move right
        if move_action_steps[idx_move_str] == '>' \
                and check_shape(floor_shape, idx_shape, current_x, current_y + 1):
            current_y += 1
        # next action step, repeat when current step greater than string length
        idx_move_str = (idx_move_str + 1) % len(move_action_steps)

    fix_shape = [(current_x + sharp_x, current_y + sharp_y) for sharp_x, sharp_y in shapes[idx_shape]]
    floor_shape.update(fix_shape)
    return idx_move_str, (idx_shape + 1) % len(shapes), max(max_x, max(x for x, y in fix_shape))


def find_repeat_block(floor_shape, max_x):
    result_nodes = set()
    # block not filled node in 7*7 block
    for x in range(7):
        for y in range(7):
            if not check_node(floor_shape, max_x - x, y):
                result_nodes.add((x, y))
    return tuple(result_nodes)


def run(run_times, input_string):
    global move_action_steps
    move_action_steps = input_string
    floor_shape = set()
    idx_shape = 0
    idx_move_str = 0
    max_x = 0
    repeat_max_x = 0
    repeat_bocks = dict()
    repeat_processed_flag = False
    while run_times > 0:
        idx_move_str, idx_shape, max_x = move_shape(floor_shape, idx_move_str, idx_shape, max_x)
        run_times -= 1
        if not repeat_processed_flag:
            repeat_bock = find_repeat_block(floor_shape, max_x)
            if (idx_move_str, idx_shape, repeat_bock) in repeat_bocks:
                (old_max_x, old_run_times) = repeat_bocks[idx_move_str, idx_shape, repeat_bock]
                print("finding!!!", (run_times, old_run_times, max_x, old_max_x, idx_move_str, idx_shape))
                repeat_times = run_times // (old_run_times - run_times)
                remain_times = run_times % (old_run_times - run_times)
                repeat_height = max_x - old_max_x
                repeat_max_x += repeat_height * repeat_times
                run_times = remain_times
                repeat_processed_flag = True
            repeat_bocks[idx_move_str, idx_shape, repeat_bock] = (max_x, run_times)
    return max_x + repeat_max_x


if __name__ == '__main__':
    # P1
    print("p1 sample")
    tmp_list_1_s = read_file_array("day17_1_s.txt")
    p1_s = run(2022, tmp_list_1_s[0])
    print("pass" if p1_s == 3068 else "failed")

    print("p1")
    tmp_list_1 = read_file_array("day17.txt")
    p1 = run(2022, tmp_list_1[0])
    print(p1)

    # P2
    print("p2")
    tmp_list_1 = read_file_array("day17.txt")
    p2 = run(1000000000000, tmp_list_1[0])
    print(p2)
