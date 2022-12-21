from func_utils import read_file_array


def covert_list_data(input_data):
    data_list = [int(x) for x in input_data]
    return data_list


def decrypt(enum_data_list):
    len_list = len(enum_data_list)
    for i in range(len_list):
        for j in range(len_list):
            if i == enum_data_list[j][0]:
                col_index, col_value = node_j = enum_data_list[j]
                new_index = (j + col_value) % (len_list - 1)
                enum_data_list.remove(enum_data_list[j])
                enum_data_list.insert(new_index, node_j)
                break
    return enum_data_list


def get_sub_total(new_result_data):
    for x in new_result_data:
        if x[1] == 0:
            search_item = x
            break
    len_list = len(new_result_data)
    index_search_item = new_result_data.index(search_item)
    return sum(new_result_data[(index_search_item + x) % len_list][1] for x in (1000, 2000, 3000))


def run(input_data):
    new_input_data = covert_list_data(input_data)
    enum_data_list = list(enumerate(new_input_data))
    new_result_data = decrypt(enum_data_list)
    sub_total = get_sub_total(new_result_data)
    print("sub total =", sub_total)
    return sub_total


def run_2(input_data):
    new_input_data = covert_list_data(input_data)
    decrypt_key = 811589153
    enum_data_list = [(k, v*decrypt_key) for k, v in enumerate(new_input_data)]
    for i in range(10):
        enum_data_list = decrypt(enum_data_list)
    sub_total = get_sub_total(enum_data_list)
    print("sub total =", sub_total)
    return sub_total


if __name__ == '__main__':
    # P1
    print("p1 sample")
    tmp_list_1_s = read_file_array("day20_1_s.txt")
    p1_s = run(tmp_list_1_s)
    print("pass" if p1_s == 3 else "failed")
    # p1
    print("p1")
    tmp_list_1 = read_file_array("day20.txt")
    p1 = run(tmp_list_1)
    # print(p1)
    # p2

    print("p2 sample")
    tmp_list_1_s = read_file_array("day20_1_s.txt")
    p1_s = run_2(tmp_list_1_s)
    print("pass" if p1_s == 1623178306 else "failed")
    print("p2")
    tmp_list_1 = read_file_array("day20.txt")
    p2 = run_2(tmp_list_1)
    # print(p2)
