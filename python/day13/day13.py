from func_utils import read_file_arrays
from functools import cmp_to_key


def covert_list(input_data):
    output_data = list(map(lambda y: y.strip("[+]+"), input_data.split(",")))
    output_data = list(map(lambda y: '-1' if y == '' else y, output_data))
    output_data = list(map(lambda y: eval(y), output_data))
    return output_data


def compare_data(left, right):
    # print("compare_data left", left, "right", right)
    if isinstance(left, list) and isinstance(right, list):
        result_value = compare_list(left, right)
    elif isinstance(left, list) or isinstance(right, list):
        if isinstance(left, list):
            right = [right]
        else:
            left = [left]
        result_value = compare_list(left, right)
    else:
        if left < right:
            result_value = 1
        elif left > right:
            result_value = -1
        else:
            result_value = 0
    return result_value


def compare_list(left, right):
    result_value = 0
    # print("compare_list left", left, "right", right)
    if isinstance(left, list) and isinstance(right, list) and result_value == 0:
        idx = 0
        while idx < len(left) and idx < len(right) and result_value == 0:
            result_value = compare_data(left[idx], right[idx])
            idx += 1
        if result_value == 0:
            if len(left) < len(right):
                result_value = 1
            elif len(left) > len(right):
                result_value = -1
    else:
        result_value = compare_data(left, right)
    return result_value


def customer_compare(a, b):
    if compare_list(a, b) == 1:
        return -1
    else:
        return 1


cmp_items_py3 = cmp_to_key(customer_compare)


class Day13:
    # class variables
    def __init__(self, data_list):
        # instance variables
        self.data_list = data_list
        self.new_data_list = []
        self.result_list = []
        self.new_p2_data_list = []
        self.new_ordered_p2_data_list = []

    def covert_list_data(self):
        for x in self.data_list:
            # print(x)
            self.new_data_list.append([eval(x[0]), eval(x[1])])
            # self.new_data_list.append([covert_list(x[0]), covert_list(x[1])])

    def run_p1(self):
        self.covert_list_data()
        for x in self.new_data_list:
            self.result_list.append(compare_list(x[0], x[1]))
        sub_total = 0
        idx = 1
        for y in self.result_list:
            if y == 1:
                sub_total += idx
            idx += 1
        print(self.result_list)
        print(sub_total)

    def run_p2(self):
        self.covert_list_data()
        self.new_p2_data_list = [[[2]], [[6]]]
        for x in self.new_data_list:
            self.new_p2_data_list.append(x[0])
            self.new_p2_data_list.append(x[1])
        self.new_p2_data_list.sort(key=cmp_items_py3)
        sub_total = 1
        idx = 1
        for y in self.new_p2_data_list:
            if y == [[2]]:
                sub_total *= idx
            elif y == [[6]]:
                sub_total *= idx
                break
            idx += 1
            # print(y)
        print(sub_total)

if __name__ == '__main__':
    # P1
    # print("p1 sample")
    # tmp_list_1_s = read_file_arrays("day13_1_s.txt")
    # p1_s = Day13(tmp_list_1_s)
    # # p1_s.print_data()
    # p1_s.run_p1()
    #
    # print("p1 production")
    # tmp_list = read_file_arrays("day13.txt")
    # p1 = Day13(tmp_list)
    # p1.run_p1()
    #
    # P2
    print("p2 sample")
    tmp_list_2_s = read_file_arrays("day13_1_s.txt")
    p2_s = Day13(tmp_list_2_s)
    p2_s.run_p2()
    # #
    print("p2 production")
    tmp_list = read_file_arrays("day13.txt")
    p2 = Day13(tmp_list)
    p2.run_p2()
