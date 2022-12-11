from func_utils import read_file_step
from day11 import day11_1


if __name__ == '__main__':
    print("p1 sample")
    tmp_list_1_s = read_file_step("day11_1_s.txt", 7)
    print(day11_1(tmp_list_1_s, 20, 3))
    # P1
    print("p1 production")
    tmp_list = read_file_step("day11.txt", 7)
    print(day11_1(tmp_list, 20, 3))

    # P2
    print("p2 sample")
    tmp_list_1_s = read_file_step("day11_1_s.txt", 7)
    print(day11_1(tmp_list_1_s, 10000))

    print("p2 production")
    tmp_list = read_file_step("day11.txt", 7)
    print(day11_1(tmp_list, 10000))
