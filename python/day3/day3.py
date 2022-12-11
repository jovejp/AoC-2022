def get_value_1(key):
    half_len = int(len(key)/2)
    tmp_str_1 = key[:half_len]
    tmp_str_2 = key[-half_len:]
    for x in tmp_str_1:
        if x in tmp_str_2:
            return x


def get_point_1(key):
    if ord(key) >= 97:
        return ord(key) - 96
    else:
        return ord(key) - 38


def day_3_1(main_list):
    sum_point_1 = 0
    for key in main_list:
        value = get_value_1(key)
        sum_point_1 = sum_point_1 + get_point_1(value)
    return sum_point_1


def get_value_2(key):
    for x in key[0]:
        if x in key[1] and x in key[2]:
            return x


def day_3_2(main_list):
    sum_point_1 = 0
    for key in main_list:
        if len(key) == 3:
            value = get_value_2(key)
            sum_point_1 = sum_point_1 + get_point_1(value)
    return sum_point_1
