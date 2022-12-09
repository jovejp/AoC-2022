def day_1(main_list):
    my_sum_list = []
    for sub_list in main_list:
        my_sum_list.append(sum(map(int, sub_list)))
    my_sum_list.sort(key=None, reverse=True)
    return my_sum_list

