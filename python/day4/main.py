from func_utils import read_file_array
from day4 import day4


if __name__ == '__main__':
    tmp_list4 = read_file_array("day4.txt")
    print("P1 Product")
    print(day4(tmp_list4, "P1"))
    print("P2 Product")
    print(day4(tmp_list4, "P2"))
