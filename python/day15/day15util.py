def convert_position(str_line):
    str_list = str_line.split(",")
    return [int(str_list[0].strip().strip("x=").strip()), int(str_list[1].strip().strip("y=").strip())]


def convert_line(str_line):
    tmp_out_list = str_line.split(":")
    return [convert_position(tmp_out_list[0].strip().strip("Sensor at ").strip()),
            convert_position(tmp_out_list[1].strip().strip("closest beacon is at").strip())]


def get_range(node):
    idx_x = node[0][1]
    idx_y = node[0][0]
    idx_length = abs(node[1][0] - node[0][0]) + abs(node[1][1] - node[0][1])
    return idx_x, idx_y, idx_length
