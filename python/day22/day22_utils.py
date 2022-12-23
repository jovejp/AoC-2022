import numpy as np
import re


def covert_map(input_data):
    result_data = list()
    result_data_index = list()
    for x in input_data:
        x = x.replace("\n", "")
        start_col = len(x) - len(x.lstrip())
        end_col = len(x.rstrip())
        tmp_line = np.array(list(x.replace("\n", "")))
        tmp_line_index = [start_col, end_col]
        result_data.append(tmp_line)
        result_data_index.append(tmp_line_index)
    return result_data, result_data_index


def convert_command(input_data):
    return [int(x) if x.isnumeric() else x for x in re.findall(r"([0-9]+|L|R)", input_data)]