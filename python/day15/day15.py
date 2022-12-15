from func_utils import read_file_array


class Day15:
    # class variables
    def __init__(self, data_list):
        # instance variables
        self.data_list = data_list
        self.start_x_position = 0
        self.end_x_position = 0
        self.start_y_position = 0
        self.end_y_position = 0
        self.new_data_list = []
        # self.result_list = []
        # self.fall_start = [500, 0]
        # self.stop_flag = False
        self.add_max_y_left = 300
        # self.add_max_y_right = 300

    def convert_line(str_line):
        tmp_out_list = str_line.split(":")
        # Sensor at x=2, y=18: closest beacon is at x=-2, y=15
        tmp_sensor = tmp_out_list[0].strip().strip("Sensor at ").strip()
        tmp_beacon = tmp_out_list[1].strip().strip("closest beacon ").strip()

    def convert_position(str_line):
        

    def covert_list_data(self):
        for x in self.data_list:
            print("line data", x)

            # tmp_line = list(map(lambda y: list(map(int, y.strip().split(","))), x.split("->")))
            # self.new_data_list.append(tmp_line)
        # for x in self.new_data_list:
        #     for y in x:
        #         if y[0] < self.start_y_position:
        #             self.start_y_position = y[0]
        #         if y[0] > self.end_y_position:
        #             self.end_y_position = y[0]
        #         if y[1] > self.end_x_position:
        #             self.end_x_position = y[1]
        # self.end_y_position = self.end_y_position + 1 + self.add_max_y + self.add_max_y_right
        # self.end_x_position = self.end_x_position + 1 + 2
        # self.result_list = [[0 for col in range(self.start_y_position, self.end_y_position)] for row in
        #                     range(self.end_x_position)]
        # self.result_list[-1] = [2 for col in range(self.start_y_position, self.end_y_position)]
        # for x in self.result_list:
        #     print(x)

    # def draw_one_step(self, node_s, node_e):
    #     if node_s[0] == node_e[0]:
    #         # draw x
    #         start_x = min(node_s[1], node_e[1])
    #         end_x = max(node_s[1], node_e[1]) + 1
    #         for idx in range(start_x, end_x):
    #             self.result_list[idx][node_s[0] - self.start_y_position + self.add_max_y] = 2
    #     else:
    #         # draw y
    #         start_y = min(node_s[0], node_e[0])
    #         end_y = max(node_s[0], node_e[0]) + 1
    #         for idy in range(start_y, end_y):
    #             self.result_list[node_s[1]][idy - self.start_y_position + self.add_max_y] = 2
    #
    # def draw_path(self):
    #     for x in self.new_data_list:
    #         # print("lenx", len(x))
    #         for idy, y in enumerate(x):
    #             # print("idy", idy)
    #             if idy + 1 < len(x):
    #                 self.draw_one_step(x[idy], x[idy + 1])
    #     # for x in self.result_list:
    #     #     print(x)



    # def get_fall_node(self):
    #     return self.check_status(self.fall_start[1], self.fall_start[0])

    def run(self):
        self.covert_list_data()
        # self.draw_path()
        # # for x in self.result_list:
        # #     print(x)
        # i = 1
        # while not self.stop_flag and self.result_list[self.fall_start[1]][
        #     self.fall_start[0] - self.start_y_position + self.add_max_y] == 0:
        #     tmp_node = self.get_fall_node()
        #     self.result_list[tmp_node[1]][tmp_node[0] - self.start_y_position + self.add_max_y] = 1
        #     i += 1
        # # for x in self.result_list:
        # #     print(x)
        # print("i", i - 1)


if __name__ == '__main__':
    # P2
    print("p2 sample")
    tmp_list_1_s = read_file_array("day15_1_s.txt")
    p2_s = Day15(tmp_list_1_s)
    p2_s.run()
    # # #
    # print("p2 production")
    # tmp_list = read_file_array("day15.txt")
    # p2 = Day15(tmp_list)
    # p2.run()
