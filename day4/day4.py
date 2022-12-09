def check_data(data1, data2, condition_flag):
    data1_1 = data1.split("-")
    data1_2 = data2.split("-")
    lst1 = list(range(int(data1_1[0]), int(data1_1[1])+1))
    lst2 = list(range(int(data1_2[0]), int(data1_2[1])+1))
    if condition_flag == "P1":
        if set(lst1).issubset(lst2) or set(lst2).issubset(lst1):
            point = 1
        else:
            point = 0
    else:
        if lst1[0] > lst2[-1] or lst2[0] > lst1[-1]:
            point = 0
        else:
            point = 1
    # print(point)
    return point


# txt.split(", ")
def day4(my_list, condition_flag):
    sum_point = 0
    for x in my_list:
        data_list = x.split(",")
        # print(data_list)
        sum_point = sum_point + check_data(data_list[0], data_list[1], condition_flag)
    return sum_point




