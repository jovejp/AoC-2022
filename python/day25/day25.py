import time

from func_utils import read_file_array


def snafu_to_decimal(data_str):
    total = 0
    len_str = len(data_str)
    for idx, x in enumerate(data_str):
        if x.isnumeric():
            total = total + int(x) * pow(5, len_str - idx - 1)
        elif x == "=":
            total = total + -2 * pow(5, len_str - idx - 1)
        elif x == "-":
            total = total + -1 * pow(5, len_str - idx - 1)
        else:
            print(f"data error!!! {x}")
    return total


def decimal_to_snafu(int_data, return_value):
    if int_data < 5:
        return_value[0] = int_data
        return
    len_str = len(str(int_data)) * 2
    while True:
        if int_data > pow(5, len_str):
            return_value[len_str] = str(int_data // pow(5, len_str))
            decimal_to_snafu(int_data % pow(5, len_str), return_value)
            break
        else:
            len_str -= 1
    return return_value


def format_dict_snafu(snafu_data):
    max_bit = list(snafu_data.keys())[0]
    i = 0
    # fill blank
    while i <= max_bit:
        if i not in snafu_data:
            snafu_data[i] = 0
        i += 1
    i = 0
    # format number
    step_in = dict()
    while i <= max_bit + 1:
        if i in step_in:
            # print(step_in, snafu_data, i)
            snafu_data[i] = str(step_in[i] + int(snafu_data[i]))
        if i in snafu_data and snafu_data[i] == "3":
            snafu_data[i] = "="
            step_in[i + 1] = 1
        elif i in snafu_data and snafu_data[i] == "4":
            snafu_data[i] = "-"
            step_in[i + 1] = 1
        elif i in snafu_data and snafu_data[i] == "5":
            snafu_data[i] = "0"
            step_in[i + 1] = 1
        i += 1
    # get final value
    return_value = ""
    for i in sorted(snafu_data.keys(), reverse=True):
        return_value = return_value + str(snafu_data[i])
    return return_value


def run(input_data):
    sub_total = 0
    for x in input_data:
        sub_total += snafu_to_decimal(x)
    print("decimal:", sub_total)
    return_value = dict()
    decimal_to_snafu(sub_total, return_value)
    run_result = format_dict_snafu(return_value)
    print("snafu:", run_result)
    return run_result


if __name__ == '__main__':
    # P1
    start = time.perf_counter()
    print("p1 sample")
    tmp_list_1_s = read_file_array("day25_1_s.txt")
    p1_s = run(tmp_list_1_s)
    print("pass" if p1_s == '2=-1=0' else "failed")
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
    # p1
    print("p1")
    start = time.perf_counter()
    tmp_list_1 = read_file_array("day25.txt")
    p1 = run(tmp_list_1)
    end = time.perf_counter()
    print("run time:", round((end - start) * 1000), "milliseconds")
