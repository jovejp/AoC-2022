# read file to array of array, split by blank line
def read_file_arrays(file_name):
    f = open(file_name)
    my_main_list = []
    my_sub_list = []
    line = f.readline()
    while line:
        if line.strip() == "":
            my_main_list.append(my_sub_list)
            my_sub_list = []
        else:
            my_sub_list.append(line)
        line = f.readline()
    my_main_list.append(my_sub_list)
    f.close()
    return my_main_list


# read file to array of array, split by step of lines
def read_file_step(file_name, step):
    f = open(file_name)
    my_main_list = []
    my_sub_list = []
    i = 1
    line = f.readline()
    while line:
        if i % step == 0:
            my_sub_list.append(line.strip())
            my_main_list.append(my_sub_list)
            my_sub_list = []
        else:
            my_sub_list.append(line.strip())
        i = i + 1
        line = f.readline()
    my_main_list.append(my_sub_list)
    f.close()
    return my_main_list


# read file to array
def read_file_array(file_name):
    f = open(file_name)
    my_main_list = []
    line = f.readline()
    while line:
        my_main_list.append(line.strip())
        line = f.readline()
    f.close()
    return my_main_list


# read file to a int array of array, split by 1 character number
def read_file_array_of_array(file_name):
    f = open(file_name)
    my_main_list = []
    line = f.readline()
    while line:
        tmp_line = line.strip()
        tmp_list = []
        for x in tmp_line:
            tmp_list.append(int(x))
        my_main_list.append(tmp_list)
        line = f.readline()
    f.close()
    return my_main_list










