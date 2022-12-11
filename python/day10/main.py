from func_utils import read_file_array
from day10 import day10_1, day10_2


if __name__ == '__main__':
    # print("p1 sample")
    # tmp_list_1_s = read_file_array("day10_1_s.txt")
    # print(day10_1(tmp_list_1_s))
    # # P1
    # print("p1 production")
    # tmp_list = read_file_array("day10.txt")
    # print(day10_1(tmp_list))

    # P2
    # print("p2 sample")
    # tmp_list_2_s = read_file_array("day10_1_s.txt")
    # day10_2(tmp_list_2_s)
    #
    # print("p2 production")
    tmp_list = read_file_array("day10.txt")
    day10_2(tmp_list)
