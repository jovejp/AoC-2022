from func_utils import read_file_array
from day5 import day5_1


if __name__ == '__main__':
    tmp_list5 = read_file_array("day5.txt")
    print("P1 Product")
    print(day5_1(tmp_list5, "Reverse"))
    print("P2 Product")
    print(day5_1(tmp_list5, "Normal"))
