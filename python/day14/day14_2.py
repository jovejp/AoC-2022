from func_utils import read_file_array


class Day14:
    # class variables
    def __init__(self, data_list):
        # instance variables
        self.data_list = data_list
        self.start_x_position = 0
        self.end_x_position = 0
        self.start_y_position = 600
        self.end_y_position = 0
        self.new_data_list = []
        self.result_list = []
        self.fall_start = [500, 0]
        self.stop_flag = False
        self.add_max_y = 300
        self.add_max_y_right = 300

    def covert_list_data(self):
        for x in self.data_list:
            tmp_line = list(map(lambda y: list(map(int, y.strip().split(","))), x.split("->")))
            self.new_data_list.append(tmp_line)
        for x in self.new_data_list:
            for y in x:
                if y[0] < self.start_y_position:
                    self.start_y_position = y[0]
                if y[0] > self.end_y_position:
                    self.end_y_position = y[0]
                if y[1] > self.end_x_position:
                    self.end_x_position = y[1]
        self.end_y_position = self.end_y_position + 1 + self.add_max_y + self.add_max_y_right
        self.end_x_position = self.end_x_position + 1 + 2
        self.result_list = [[0 for col in range(self.start_y_position, self.end_y_position)] for row in
                            range(self.end_x_position)]
        self.result_list[-1] = [2 for col in range(self.start_y_position, self.end_y_position)]
        # for x in self.result_list:
        #     print(x)

    def draw_one_step(self, node_s, node_e):
        if node_s[0] == node_e[0]:
            # draw x
            start_x = min(node_s[1], node_e[1])
            end_x = max(node_s[1], node_e[1]) + 1
            for idx in range(start_x, end_x):
                self.result_list[idx][node_s[0] - self.start_y_position + self.add_max_y] = 2
        else:
            # draw y
            start_y = min(node_s[0], node_e[0])
            end_y = max(node_s[0], node_e[0]) + 1
            for idy in range(start_y, end_y):
                self.result_list[node_s[1]][idy - self.start_y_position + self.add_max_y] = 2

    def draw_path(self):
        for x in self.new_data_list:
            # print("lenx", len(x))
            for idy, y in enumerate(x):
                # print("idy", idy)
                if idy + 1 < len(x):
                    self.draw_one_step(x[idy], x[idy + 1])
        # for x in self.result_list:
        #     print(x)

    def check_down_status(self, idx, idy):
        if idx + 1 >= self.end_x_position:
            print("down idx", idx, "idy", idy, "max x", self.end_x_position, "max y", self.end_y_position, "actual x ",
                  idx + 1, "actual y", idy - self.start_y_position + self.add_max_y)
            self.stop_flag = True
            return False
        if self.result_list[idx + 1][idy - self.start_y_position + self.add_max_y] == 0:
            return True
        else:
            return False

    def check_left_status(self, idx, idy):
        if idy + self.add_max_y - self.start_y_position - 1 < 0 or idx + 1 >= self.end_x_position:
            print("left idx", idx, "idy", idy, "max x", self.end_x_position, "max y", self.end_y_position, "actual x ",
                  idx + 1, "actual y", idy - self.start_y_position - 1 + self.add_max_y)
            self.stop_flag = True
            return False
        if self.result_list[idx + 1][idy - self.start_y_position - 1 + self.add_max_y] == 0:
            return True
        else:
            return False

    def check_right_status(self, idx, idy):
        if idy + self.add_max_y + 1 >= self.end_y_position or idx + 1 >= self.end_x_position:
            print("right left idx", idx, "idy", idy, "max x", self.end_x_position, "max y", self.end_y_position,
                  "actual x ", idx + 1, "actual y", idy - self.start_y_position + 1 + self.add_max_y)
            self.stop_flag = True
            return False
        if self.result_list[idx + 1][idy - self.start_y_position + 1 + self.add_max_y] == 0:
            return True
        else:
            return False

    def check_status(self, idx, idy):
        if self.check_down_status(idx, idy):
            result = self.check_status(idx + 1, idy)
        elif self.check_left_status(idx, idy):
            result = self.check_status(idx + 1, idy - 1)
        elif self.check_right_status(idx, idy):
            result = self.check_status(idx + 1, idy + 1)
        else:
            result = [idy, idx]
        return result

    def get_fall_node(self):
        return self.check_status(self.fall_start[1], self.fall_start[0])

    def run_p2(self):
        self.covert_list_data()
        self.draw_path()
        # for x in self.result_list:
        #     print(x)
        i = 1
        while not self.stop_flag and self.result_list[self.fall_start[1]][
            self.fall_start[0] - self.start_y_position + self.add_max_y] == 0:
            tmp_node = self.get_fall_node()
            self.result_list[tmp_node[1]][tmp_node[0] - self.start_y_position + self.add_max_y] = 1
            i += 1
        # for x in self.result_list:
        #     print(x)
        print("i", i - 1)


if __name__ == '__main__':
    # P2
    print("p2 sample")
    tmp_list_2_s = read_file_array("day14_1_s.txt")
    p2_s = Day14(tmp_list_2_s)
    p2_s.run_p2()
    # # #
    print("p2 production")
    tmp_list = read_file_array("day14.txt")
    p2 = Day14(tmp_list)
    p2.run_p2()
