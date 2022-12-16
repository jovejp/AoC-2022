from func_utils import read_file_array
from day15util import convert_line, get_range


class Day15:
    # class variables
    def __init__(self, data_list):
        # instance variables
        self.data_list = data_list
        self.new_data_list = []
        self.start_x_position = 0
        self.end_x_position = 0
        self.start_y_position = 0
        self.end_y_position = 0
        self.base_x_position = 0
        self.base_y_position = 0
        self.result_list = []
        self.add_max_y_left = 0
        self.add_max_y_right = 1000000
        self.target_line = 0

    def covert_list_data(self):
        for x in self.data_list:
            self.new_data_list.append(convert_line(x))
        for x in self.new_data_list:
            for y in x:
                if y[0] < self.start_y_position:
                    self.start_y_position = y[0]
                if y[0] > self.end_y_position:
                    self.end_y_position = y[0]
                if y[1] < self.start_x_position:
                    self.start_x_position = y[1]
                if y[1] > self.end_x_position:
                    self.end_x_position = y[1]
        self.end_x_position += 1
        self.end_y_position += 1

        self.base_x_position = -1 * self.start_x_position
        self.start_x_position += self.base_x_position
        self.end_x_position += self.base_x_position
        self.target_line += self.base_x_position

        self.base_y_position = -1 * self.start_y_position
        self.start_y_position = self.start_y_position + self.base_y_position
        self.end_y_position = self.end_y_position + self.base_y_position + self.add_max_y_left + self.add_max_y_right
        print("position ready")
        print(self.start_x_position, self.end_x_position, self.start_y_position, self.end_y_position)
        print("init tables")
        # self.result_list = [[0 for col in range(self.start_y_position, self.end_y_position)] for row in
        #                     range(self.end_x_position)]
        self.result_list = [0 for col in range(self.start_y_position, self.end_y_position)]
        # self.result_list[-1] = [2 for col in range(self.start_y_position, self.end_y_position)]
        # for x in self.result_list:
        #     print(x)

    def draw_one_node(self, node, data):
        idx_x = node[1]
        idx_y = node[0]
        if idx_x + self.base_x_position == self.target_line:
            self.result_list[idx_y + self.base_y_position + self.add_max_y_left] = data

    def draw_sensor_beacon(self):
        for x in self.new_data_list:
            self.draw_one_node(x[0], 1)
            self.draw_one_node(x[1], 2)

    def draw_closest(self, node, data=3):
        idx_x, idx_y, idx_length = get_range(node)
        if idx_x + self.base_x_position - idx_length <= self.target_line <= idx_x + self.base_x_position + idx_length:
            for i in range(-1 * idx_length, 1 * idx_length + 1):
                if idx_x + self.base_x_position + i == self.target_line:
                    idx_cols = idx_length + i if i < 0 else idx_length - i
                    for j in range(0, idx_cols + 1):
                        if j == 0:
                            if self.result_list[idx_y + self.base_y_position + self.add_max_y_left] == 0:
                                self.result_list[idx_y + self.base_y_position + self.add_max_y_left] = data
                            elif self.result_list[idx_y + self.base_y_position + self.add_max_y_left] == data:
                                self.result_list[idx_y + self.base_y_position + self.add_max_y_left] = data + 1
                        else:

                            if self.result_list[idx_y + self.base_y_position + self.add_max_y_left - j] == 0:
                                self.result_list[idx_y + self.base_y_position + self.add_max_y_left - j] = data
                            elif self.result_list[idx_y + self.base_y_position + self.add_max_y_left - j] == data:
                                self.result_list[idx_y + self.base_y_position + self.add_max_y_left - j] = data + 1

                            if self.result_list[idx_y + self.base_y_position + self.add_max_y_left + j] == 0:
                                self.result_list[idx_y + self.base_y_position + self.add_max_y_left + j] = data
                            elif self.result_list[idx_y + self.base_y_position + self.add_max_y_left + j] == data:
                                self.result_list[idx_y + self.base_y_position + self.add_max_y_left + j] = data + 1
                    break

    def run(self, line_number=10):
        self.target_line = line_number
        self.covert_list_data()
        self.draw_sensor_beacon()
        for x in self.new_data_list:
            self.draw_closest(x)
        count_num = 0
        print(self.result_list[0], self.result_list[-1])
        for x in self.result_list:
            if x >= 3:
                count_num += 1
        print(count_num)


if __name__ == '__main__':
    # P2
    print("p2 sample")
    tmp_list_1_s = read_file_array("day15_1_s.txt")
    p2_s = Day15(tmp_list_1_s)
    p2_s.run(10)
    # # #
    print("p2 production")
    tmp_list = read_file_array("day15.txt")
    p2 = Day15(tmp_list)
    p2.run(2000000)
