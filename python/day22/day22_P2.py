import time
from func_utils import read_file_arrays
from day22_utils import *

global new_input_data, input_data_index, cube_size


def get_cube_side(row_no, col_no):
    # print(f"row_no={row_no}, cube_size={cube_size}, row_no // cube_size = {row_no // cube_size},"
    #       f"col_no // cube_size ={col_no // cube_size}")
    if row_no // cube_size == 0:
        return col_no // cube_size
    elif row_no // cube_size == 1:
        return 3
    elif row_no // cube_size == 2:
        return row_no // cube_size + 2 + col_no // cube_size
    elif row_no // cube_size == 3:
        return 6
    else:
        print(f"cube side error, row_no={row_no}, col_no={col_no}")
        return -1


def move_in_cube(start_point, face, steps):
    global new_input_data, input_data_index
    start_row, start_col = start_point
    end_row = start_row
    end_col = start_col
    while steps > 0:
        steps -= 1
        if face == 0:
            if end_col + 1 == input_data_index[start_row][1]:
                cube_side = get_cube_side(end_row, end_col)
                if cube_side == 2:
                    tmp_start_row = 3 * cube_size - 1 - end_row
                    tmp_start_col = 2 * cube_size - 1
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 2  # << left
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 3:
                    tmp_start_row = cube_size - 1
                    tmp_start_col = end_row + cube_size
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 3  # << up
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 5:
                    tmp_start_row = 3 * cube_size - 1 - end_row
                    tmp_start_col = 3 * cube_size - 1
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 2  # << left
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 6:
                    tmp_start_row = 3 * cube_size - 1
                    tmp_start_col = end_row - 2 * cube_size
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 3  # << up
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                else:
                    print(f"moving right error!!! cube_side={cube_side}, row={end_row}, col={end_col}")
            else:
                if new_input_data[end_row][end_col + 1] == ".":
                    end_col += 1
                elif new_input_data[end_row][end_col + 1] == "#":
                    break
                else:
                    print(f"face={face} error!, data={new_input_data[end_row][end_col + 1]}, "
                          f"row={end_row}, col={end_col + 1}")
        elif face == 2:  # 2 for left (<)
            if end_col - 1 < input_data_index[start_row][0]:
                cube_side = get_cube_side(end_row, end_col)
                if cube_side == 1:
                    tmp_start_row = 3 * cube_size - 1 - end_row
                    tmp_start_col = 0
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 0  # << right
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 3:
                    tmp_start_row = 2 * cube_size
                    tmp_start_col = end_row - cube_size
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 1  # << down
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 4:
                    tmp_start_row = 3 * cube_size - 1 - end_row
                    tmp_start_col = cube_size
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 0  # << right
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 6:
                    tmp_start_row = 0
                    tmp_start_col = end_row - 2 * cube_size
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 1  # << down
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                else:
                    print(f"moving left error!!! cube_side={cube_side}, row={end_row}, col={end_col}")
            else:
                if new_input_data[end_row][end_col - 1] == ".":
                    end_col -= 1
                elif new_input_data[end_row][end_col - 1] == "#":
                    break
                else:
                    print(f"face={face} error!, data={new_input_data[end_row][end_col - 1]}, "
                          f"row={end_row}, col={end_col - 1}")
        elif face == 1:  # 1 for down (v)
            if end_row + 1 < len(new_input_data) and input_data_index[end_row + 1][0] <= end_col < \
                    input_data_index[end_row + 1][1]:
                if new_input_data[end_row + 1][end_col] == ".":
                    end_row += 1
                elif new_input_data[end_row + 1][end_col] == "#":
                    break
                else:
                    print(f"face={face} error!, data={new_input_data[end_row + 1][end_col]}, "
                          f"row={end_row + 1}, col={end_col}")
            else:
                cube_side = get_cube_side(end_row, end_col)

                if cube_side == 2:
                    tmp_start_row = end_col - cube_size
                    tmp_start_col = 2 * cube_size - 1
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 2  # << left
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 5:
                    tmp_start_row = 2 * cube_size + end_col
                    tmp_start_col = cube_size - 1
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 2  # << left
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 6:
                    tmp_start_row = 0
                    tmp_start_col = 2 * cube_size + end_col
                    # print(f"error!, face=={face}, cube_side={cube_side},  "
                    #       f"end_row={end_row}, end_col={end_col},"
                    #       f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 1  # << down
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                else:
                    print(input_data_index[end_row + 1][0],end_col,input_data_index[end_row + 1][1])
                    print(f"moving down error!!! cube_side={cube_side}, row={end_row}, col={end_col}")
        elif face == 3:  # 3 for up (^)
            if end_row - 1 >= 0 and input_data_index[end_row - 1][0] <= end_col < input_data_index[end_row - 1][1]:
                if new_input_data[end_row - 1][end_col] == ".":
                    end_row -= 1
                elif new_input_data[end_row - 1][end_col] == "#":
                    break
                else:
                    print(f"face={face} error!, data={new_input_data[end_row - 1][end_col]}, "
                          f"row={end_row - 1}, col={end_col}")
            else:
                cube_side = get_cube_side(end_row, end_col)
                if cube_side == 1:
                    tmp_start_row = end_col + 2 * cube_size
                    tmp_start_col = 0
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 0  # << right
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 2:
                    tmp_start_row = 4 * cube_size - 1
                    tmp_start_col = end_col - 2 * cube_size
                    # print(f"error!, face=={face}, cube_side={cube_side},  "
                    #       f"end_row={end_row}, end_col={end_col},"
                    #       f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 3  # << up
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                elif cube_side == 4:
                    tmp_start_row = end_col + cube_size
                    tmp_start_col = cube_size
                    if new_input_data[tmp_start_row][tmp_start_col] == ".":
                        end_row = tmp_start_row
                        end_col = tmp_start_col
                        face = 0  # << right
                    elif new_input_data[tmp_start_row][tmp_start_col] == "#":
                        break
                    else:
                        # print(tmp_start_row, tmp_start_col, end_row, end_col,
                        #       new_input_data[tmp_start_row][tmp_start_col])
                        print(f"error!, face=={face}, cube_side={cube_side},  "
                              f"tmp_start_row={tmp_start_row}, tmp_start_col={tmp_start_col} ")
                else:
                    print(f"moving up error!!! cube_side={cube_side}, row={end_row}, col={end_col}")
        else:
            print(f"face={face} error!!!, not in 0,1,2,3")
    return (end_row, end_col), face


def run(input_data):
    global new_input_data, input_data_index, cube_size
    new_input_data, input_data_index = covert_map(input_data[0])
    command_list = convert_command(input_data[1][0])
    cube_size = int(len(new_input_data) / 4)
    face = 0  # 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
    start_point = [0, input_data_index[0][0]]
    for x in command_list:
        if isinstance(x, str):
            if x == 'R':
                face = (face + 1) % 4
            elif x == 'L':
                face = face - 1 if face - 1 >= 0 else face - 1 + 4
            else:
                print("data error!")
        else:
            start_point, face = move_in_cube(start_point, face, x)

    print(start_point, face)
    x, y = start_point
    subtotal = 1000 * (x + 1) + 4 * (y + 1) + face
    print(subtotal)
    return subtotal


if __name__ == '__main__':
    # p2
    print("p2")
    start = time.perf_counter()
    tmp_list_1 = read_file_arrays("day22.txt")
    p2 = run(tmp_list_1)
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")

