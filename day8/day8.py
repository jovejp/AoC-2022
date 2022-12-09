def check_visible(my_list, idx, idy, lenx, leny, y):
    # print(idx, idy, lenx, leny, y)
    # check left
    tmpy = 0
    result = 1
    while tmpy < idy:
        if my_list[idx][tmpy] >= y:
            result = 0
            break
        else:
            tmpy += 1

    if result == 1:
        # print("left", idx, tmpy)
        return 1
    else:
        result = 1

    # check top
    tmp_x = 0
    while tmp_x < idx:
        if my_list[tmp_x][idy] >= y:
            result = 0
            break
        else:
            tmp_x += 1

    if result == 1:
        # print("top", tmp_x, idy)
        return 1
    else:
        result = 1

    # check right
    tmpy = idy + 1
    while tmpy < leny:
        if my_list[idx][tmpy] >= y:
            result = 0
            break
        else:
            tmpy += 1

    if result == 1:
        # print("right", idx, tmpy)
        return 1
    else:
        result = 1

    # check bottom
    tmp_x = idx + 1
    while tmp_x < lenx:
        if my_list[tmp_x][idy] >= y:
            result = 0
            break
        else:
            tmp_x += 1

    if result == 1:
        # print("bottom", tmp_x, idy)
        return 1
    return 0


def get_point(my_list, idx, idy, lenx, leny, y):
    if idx == 0 or idy == 0:
        return 1
    elif idx == (lenx - 1) or idy == (leny - 1):
        return 1
    else:
        return check_visible(my_list, idx, idy, lenx, leny, y)


def day8_1(my_list):
    # print("start")
    point_count = 0
    lenx = len(my_list)
    for idx, x in enumerate(my_list):
        leny = len(x)
        for idy, y in enumerate(x):
            # print(idx, idy, y)
            point_count += get_point(my_list, idx, idy, lenx, leny, y)
    return point_count


def check_visible_2(my_list, idx, idy, lenx, leny, y):
    # print(idx, idy, lenx, leny, y)
    # check left
    tmpy = idy - 1
    left_x = 0
    while tmpy >= 0:
        if my_list[idx][tmpy] >= y:
            left_x += 1
            break
        else:
            left_x += 1
            tmpy -= 1
    # print("left", idx, tmpy, left_x)

    # check top
    tmp_x = idx - 1
    top_x = 0
    while tmp_x >= 0:
        if my_list[tmp_x][idy] >= y:
            top_x += 1
            break
        else:
            top_x += 1
            tmp_x -= 1
    # print("top", tmp_x, top_x)

    # check right
    tmpy = idy + 1
    right_x = 0
    while tmpy < leny:
        if my_list[idx][tmpy] >= y:
            right_x += 1
            break
        else:
            right_x += 1
            tmpy += 1
    # print("right", idx, tmpy, right_x)

    # check bottom
    tmp_x = idx + 1
    bottom_x = 0
    while tmp_x < lenx:
        if my_list[tmp_x][idy] >= y:
            bottom_x += 1
            break
        else:
            bottom_x += 1
            tmp_x += 1
    # print("bottom", tmp_x, idy, bottom_x)

    return bottom_x * right_x * top_x * left_x


def get_point_2(my_list, idx, idy, lenx, leny, y):
    if idx == 0 or idy == 0:
        return 0
    elif idx == (lenx - 1) or idy == (leny - 1):
        return 0
    else:
        return check_visible_2(my_list, idx, idy, lenx, leny, y)


def day8_2(my_list):
    # print("start")
    point_count = []
    len_x = len(my_list)
    for idx, x in enumerate(my_list):
        len_y = len(x)
        for idy, y in enumerate(x):
            # print(idx, idy, y)
            point_count.append(get_point_2(my_list, idx, idy, len_x, len_y, y))
    point_count.sort(key=None, reverse=True)
    return point_count
