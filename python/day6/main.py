from func_utils import read_file_array
from day6 import day6_1


if __name__ == '__main__':
    tmp_list6 = read_file_array("day6.txt")
    print("P1 Product")
    print(day6_1(tmp_list6[0], 4))
    print("P2 Product")
    print(day6_1(tmp_list6[0], 14))

