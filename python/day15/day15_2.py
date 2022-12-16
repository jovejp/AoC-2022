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
        self.result_list = []
        self.max_number = 0
        self.target_line = 0

    def covert_list_data(self):
        for x in self.data_list:
            self.new_data_list.append(convert_line(x))
        for x in self.new_data_list:
            for y in x:
                # if y[0] < self.start_y_position:
                #     self.start_y_position = y[0]
                if y[0] > self.end_y_position:
                    self.end_y_position = y[0]
                # if y[1] < self.start_x_position:
                #     self.start_x_position = y[1]
                if y[1] > self.end_x_position:
                    self.end_x_position = y[1]

        if self.end_x_position > self.max_number:
            self.end_x_position = self.max_number + 1
        else:
            self.end_x_position += 1
        if self.end_y_position > self.max_number:
            self.end_y_position = self.max_number + 1
        else:
            self.end_y_position += 1
        print(self.start_x_position, self.end_x_position, self.start_y_position, self.end_y_position)
        print("init tables")

    def draw_one_node(self, node, data):
        idx_x = node[1]
        idx_y = node[0]
        if idx_x == self.target_line and 0 <= idx_y <= self.max_number:
            self.result_list.append((idx_y, idx_y, data))

    def draw_sensor_beacon(self):
        for x in self.new_data_list:
            self.draw_one_node(x[0], 1)
            self.draw_one_node(x[1], 2)

    def draw_closest(self, node, data=3):
        idx_x, idx_y, idx_length = get_range(node)
        if idx_x - idx_length <= self.target_line <= idx_x + idx_length:
            gap_x = abs(idx_x - self.target_line)
            gap_y = idx_length - gap_x
            start_y = idx_y - gap_y if idx_y - gap_y >= 0 else 0
            end_y = idx_y + gap_y if idx_y + gap_y < self.end_y_position else self.end_y_position
            self.result_list.append((start_y, end_y, data))

    def get_possible_position(self):
        start_y = self.result_list[0][0]
        end_y = self.result_list[1][0]
        poss_posi = -1

        for idx, x in enumerate(self.result_list):
            if start_y <= x[0] <= end_y + 1:
                if x[1] > end_y:
                    end_y = x[1]
            elif x[0] > end_y + 1:
                print("find", start_y, x[0])
                poss_posi = end_y + 1
                break
            else:
                print("error")
                print(self.result_list)
        # print(start_y, end_y)
        return poss_posi

    def run_2(self, line_number):
        self.max_number = line_number
        self.covert_list_data()
        temp_line = 0
        while temp_line <= line_number:
            self.target_line = temp_line
            self.result_list = []
            self.draw_sensor_beacon()
            for x in self.new_data_list:
                self.draw_closest(x)
            self.result_list = sorted(self.result_list)
            result_y = self.get_possible_position()
            if result_y != -1:
                break
            temp_line += 1
        print(temp_line, result_y)
        sub_total = result_y * 4000000 + temp_line
        print(sub_total)


if __name__ == '__main__':
    # P2
    # print("p2 sample")
    # tmp_list_1_s = read_file_array("day15_1_s.txt")
    # p2_s = Day15(tmp_list_1_s)
    # p2_s.run_2(20)

    print("p2 production")
    tmp_list = read_file_array("day15.txt")
    p2 = Day15(tmp_list)
    p2.run_2(4000000)
