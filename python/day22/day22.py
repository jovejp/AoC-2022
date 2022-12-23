import time
from func_utils import read_file_arrays
from day22_utils import *
global new_input_data, input_data_index, cube_size


def move_one_step(start_point, face, steps):
    global new_input_data, input_data_index
    start_row, start_col = start_point
    if face == 0:  # 0 for right (>)
        end_row = start_row
        end_col = input_data_index[start_row][0] if input_data_index[start_row][0] > start_col else start_col
        while steps > 0:
            steps -= 1
            # print("start_row=", end_col+1, input_data_index[start_row][1])
            if end_col + 1 == input_data_index[start_row][1]:
                if new_input_data[end_row][input_data_index[start_row][0]] == ".":
                    end_col = input_data_index[start_row][0]
                elif new_input_data[end_row][input_data_index[start_row][0]] == "#":
                    break
                else:
                    print("face==0 error!")
            else:
                if new_input_data[end_row][end_col + 1] == ".":
                    end_col += 1
                elif new_input_data[end_row][end_col + 1] == "#":
                    break
                else:
                    print("face==0 error!")
    elif face == 2:  # 2 for left (<)
        end_row = start_row
        end_col = input_data_index[start_row][0] if input_data_index[start_row][0] > start_col else start_col
        while steps > 0:
            steps -= 1
            if end_col - 1 < input_data_index[start_row][0]:
                if new_input_data[end_row][input_data_index[start_row][1] - 1] == ".":
                    end_col = input_data_index[start_row][1] - 1
                elif new_input_data[end_row][input_data_index[start_row][1] - 1] == "#":
                    break
                else:
                    print("face==2 error!")
            else:
                if new_input_data[end_row][end_col - 1] == ".":
                    end_col -= 1
                elif new_input_data[end_row][end_col - 1] == "#":
                    break
                else:
                    print("face==2 error!")
    elif face == 1:  # 1 for down (v)
        end_row = start_row
        end_col = start_col
        while steps > 0:
            steps -= 1
            if end_row + 1 < len(new_input_data) and input_data_index[end_row + 1][0] <= end_col < \
                    input_data_index[end_row + 1][1]:
                if new_input_data[end_row + 1][end_col] == ".":
                    end_row += 1
                elif new_input_data[end_row + 1][end_col] == "#":
                    break
                else:
                    print("face==1, end_row error!!!")
            else:
                tmp_row = 0
                while True:
                    if input_data_index[tmp_row][0] <= end_col < input_data_index[tmp_row][1]:
                        break
                    tmp_row += 1
                if new_input_data[tmp_row][end_col] == ".":
                    end_row = tmp_row
                elif new_input_data[tmp_row][end_col] == "#":
                    break
                else:
                    print("face==1, end_row error!!!")
    elif face == 3:  # 3 for up (^)
        end_row = start_row
        end_col = start_col
        while steps > 0:
            steps -= 1
            if end_row - 1 >= 0 and input_data_index[end_row - 1][0] <= end_col < input_data_index[end_row - 1][1]:
                if new_input_data[end_row - 1][end_col] == ".":
                    end_row -= 1
                elif new_input_data[end_row - 1][end_col] == "#":
                    break
                else:
                    print("face==3, end_row error!!!")
            else:
                tmp_row = len(new_input_data) - 1
                while True:
                    if input_data_index[tmp_row][0] <= end_col < input_data_index[tmp_row][1]:
                        break
                    tmp_row -= 1
                if new_input_data[tmp_row][end_col] == ".":
                    end_row = tmp_row
                elif new_input_data[tmp_row][end_col] == "#":
                    break
                else:
                    print("face==3, end_row error!!!")
    else:
        print(f"face=={face} error!!!")
    return end_row, end_col


def run(input_data, px):
    global new_input_data, input_data_index, cube_size
    new_input_data, input_data_index = covert_map(input_data[0])
    # for x in new_input_data:
    #     print(x)
    command_list = convert_command(input_data[1][0])
    cube_size = int(len(new_input_data) / 4) + 1
    face = 0  # 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
    start_point = [0, 0]
    # new_start_point = move_one_step(start_point, face, 10)
    # print(new_start_point, face)
    for x in command_list:
        if isinstance(x, str):
            if x == 'R':
                face = (face + 1) % 4
            elif x == 'L':
                face = face - 1 if face - 1 >= 0 else face - 1 + 4
            else:
                print("data error!")
        else:
            start_point = move_one_step(start_point, face, x)
    print(start_point, face)
    x, y = start_point
    subtotal = 1000 * (x + 1) + 4 * (y + 1) + face
    print(subtotal)
    return subtotal


if __name__ == '__main__':
    # P1
    start = time.perf_counter()
    print("p1 sample")
    tmp_list_1_s = read_file_arrays("day22_1_s.txt")
    p1_s = run(tmp_list_1_s, "p1")
    print("pass" if p1_s == 6032 else "failed")
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
    # p1
    print("p1")
    start = time.perf_counter()
    tmp_list_1 = read_file_arrays("day22.txt")
    p1 = run(tmp_list_1, "p1")
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
