from func_utils import read_file_arrays
from day1 import day_1


if __name__ == '__main__':
    tmp_list = read_file_arrays("day1.txt")
    result_list = day_1(tmp_list)
    # p1
    print("P1 Product")
    print(result_list[0])
    # p2
    sum_top_3 = 0
    for x in result_list[:3]:
        sum_top_3 += x
    print("P2 Product")
    print(sum_top_3)


