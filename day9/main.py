from func_utils import read_file_array
from day9 import day9


if __name__ == '__main__':
    print("p1 sample")
    tmp_list9_1_s = read_file_array("day9_1_s.txt")
    # print(tmp_list9_1_s)
    print(day9(tmp_list9_1_s, 1, 5, 0, 11))
    # P1
    print("p2 production")
    tmp_list9 = read_file_array("day9.txt")
    # print(tmp_list9)
    print(day9(tmp_list9, 1, 21, 30, 300))

    # P2
    print("p2 sample")
    tmp_list9_2_s = read_file_array("day9_2_s.txt")
    # print(tmp_list9_2_s)
    print(day9(tmp_list9_2_s, 9, 15, 12, 40))

    print("p2 production")
    tmp_list9_2 = read_file_array("day9.txt")
    # print(tmp_list9_2)
    print(day9(tmp_list9_2, 9, 21, 30, 300))
