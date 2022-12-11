from func_utils import read_file_array, read_file_step
from day3 import day_3_1, day_3_2


if __name__ == '__main__':
    print("P1 Product")
    tmp_list3 = read_file_array("day3.txt")
    print(day_3_1(tmp_list3))
    print("P2 Product")
    tmp_list3_2 = read_file_step("day3.txt", 3)
    print(day_3_2(tmp_list3_2))
