from func_utils import read_file_array
from day2 import day_2


if __name__ == '__main__':
    tmp_list2 = read_file_array("day2.txt")
    sum_point_1, sum_point_2 = day_2(tmp_list2)
    print("P1 Product")
    print(sum_point_1)
    print("P2 Product")
    print(sum_point_2)



