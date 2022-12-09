def day6_1(my_list, check_lenth):
    i = 0
    check_flag = 0
    while i < len(my_list)-3:
        suba = my_list[i:i+check_lenth]
        for x in suba:
            check_flag = check_flag + suba.count(x)
        if check_flag == check_lenth:
            # print(suba)
            # print(check_flag)
            return i+check_lenth
        else:
            # print(suba)
            # print(check_flag)
            check_flag = 0
        i += 1
    return i



