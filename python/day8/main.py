from func_utils import read_file_array_of_array
from day8 import day8_1, day8_2


if __name__ == '__main__':
    # Sample
    tmp_list8_d = read_file_array_of_array("day8_1.txt")
    print("P1 sample")
    print(day8_1(tmp_list8_d))

    print("P2 sample")
    print(day8_2(tmp_list8_d)[0])

    # Product
    tmp_list8 = read_file_array_of_array("day8.txt")
    print("P1 Product")
    print(day8_1(tmp_list8))

    print("P2 Product")
    print(day8_2(tmp_list8)[0])
