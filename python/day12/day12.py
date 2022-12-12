from func_utils import read_file_array
from numpy import *
import time, threading


class Day12:
    path_list = []
    success_path_list = []
    success_step = 0
    moved_position = []

    def __init__(self, data_list):
        self.data_list = data_list
        self.start_position = []
        self.target_position = []
        self.new_path_list = []

    def init_start_end(self):
        search_condition = 0
        for idx, x in enumerate(self.data_list):
            for idy, y in enumerate(x):
                if y == 'S':
                    self.start_position = [idx, idy]
                    search_condition += 1
                elif y == 'E':
                    self.target_position = [idx, idy]
                    search_condition += 1
                if search_condition == 2:
                    return

    def init_search(self):
        self.data_list[self.start_position[0]] = self.data_list[self.start_position[0]].replace('S', 'a')
        self.data_list[self.target_position[0]] = self.data_list[self.target_position[0]].replace('E', 'z')
        Day12.moved_position = []
        Day12.moved_position.append(self.start_position)
        path_list = []
        tmp_path = [self.start_position]
        Day12.path_list.append(tmp_path)
        Day12.success_path_list = []
        Day12.success_step = 0

    def move_up(self, x, current_position, pre_position):
        tmp_idx = current_position[0]
        tmp_idy = current_position[1]
        if tmp_idx - 1 >= 0 and (tmp_idx - 1 != pre_position[0] or tmp_idy != pre_position[1]) \
                and [tmp_idx - 1, tmp_idy] not in Day12.moved_position \
                and compare(self.data_list[tmp_idx][tmp_idy], self.data_list[tmp_idx - 1][tmp_idy]):
            Day12.moved_position.append([tmp_idx - 1, tmp_idy])
            tmp_up_path = x.copy()
            tmp_up_path.append([tmp_idx - 1, tmp_idy])
            if [tmp_idx - 1, tmp_idy] == self.target_position:
                Day12.success_path_list.append(tmp_up_path)
                Day12.success_step = len(tmp_up_path)
            else:
                self.new_path_list.append(tmp_up_path)
            return True
        else:
            return False

    def move_down(self, x, current_position, pre_position):
        tmp_idx = current_position[0]
        tmp_idy = current_position[1]
        if tmp_idx + 1 < len(self.data_list) and (tmp_idx + 1 != pre_position[0] or tmp_idy != pre_position[1]) \
                and [tmp_idx + 1, tmp_idy] not in Day12.moved_position and \
                compare(self.data_list[tmp_idx][tmp_idy], self.data_list[tmp_idx + 1][tmp_idy]):
            tmp_down_path = x.copy()
            tmp_down_path.append([tmp_idx + 1, tmp_idy])
            Day12.moved_position.append([tmp_idx + 1, tmp_idy])
            if [tmp_idx + 1, tmp_idy] == self.target_position:
                Day12.success_path_list.append(tmp_down_path)
                Day12.success_step = len(tmp_down_path)
            else:
                self.new_path_list.append(tmp_down_path)
            return True
        else:
            return False

    def move_left(self, x, current_position, pre_position):
        tmp_idx = current_position[0]
        tmp_idy = current_position[1]
        if tmp_idy - 1 >= 0 and (tmp_idx != pre_position[0] or tmp_idy - 1 != pre_position[1]) \
                and [tmp_idx, tmp_idy - 1] not in Day12.moved_position \
                and compare(self.data_list[tmp_idx][tmp_idy], self.data_list[tmp_idx][tmp_idy - 1]):
            # print("left", self.data_list[tmp_idx][tmp_idy], self.data_list[tmp_idx][tmp_idy - 1])
            tmp_left_path = x.copy()
            tmp_left_path.append([tmp_idx, tmp_idy - 1])
            Day12.moved_position.append([tmp_idx, tmp_idy - 1])
            if [tmp_idx, tmp_idy - 1] == self.target_position:
                Day12.success_path_list.append(tmp_left_path)
                Day12.success_step = len(tmp_left_path)
            else:
                self.new_path_list.append(tmp_left_path)
            return True
        else:
            return False

    def move_right(self, x, current_position, pre_position):
        tmp_idx = current_position[0]
        tmp_idy = current_position[1]
        if tmp_idy + 1 < len(self.data_list[tmp_idx]) and (tmp_idx != pre_position[0] or tmp_idy + 1 != pre_position[1]) \
                and [tmp_idx, tmp_idy + 1] not in Day12.moved_position \
                and compare(self.data_list[tmp_idx][tmp_idy], self.data_list[tmp_idx][tmp_idy + 1]):
            tmp_right_path = x.copy()
            tmp_right_path.append([tmp_idx, tmp_idy + 1])
            Day12.moved_position.append([tmp_idx, tmp_idy + 1])
            if [tmp_idx, tmp_idy + 1] == self.target_position:
                Day12.success_path_list.append(tmp_right_path)
                Day12.success_step = len(tmp_right_path)
            else:
                self.new_path_list.append(tmp_right_path)
            return True
        else:
            return False

    def move_one_step(self):
        self.new_path_list = []
        for x in Day12.path_list:
            current_position = x[-1]
            if len(x) > 2:
                pre_position = x[-2]
            else:
                pre_position = current_position
            self.move_up(x, current_position, pre_position)
            self.move_down(x, current_position, pre_position)
            self.move_left(x, current_position, pre_position)
            self.move_right(x, current_position, pre_position)
        Day12.path_list = self.new_path_list

    def print_result(self):
        for x in self.data_list:
            print(x)
        for y in Day12.path_list:
            print(y)

    def run(self):
        self.init_start_end()
        self.init_search()
        index = 1
        while Day12.success_step == 0 and len(Day12.path_list) > 0:
            # print(index, len(Day12.path_list), "start")
            self.move_one_step()
            index += 1
        if Day12.success_step == 0:
            print("not find,something wrong")
        else:
            print("find!!!", Day12.success_step - 1)

    def p2_run(self):
        self.init_start_end()
        self.init_search()
        result_list = []
        for idx, x in enumerate(self.data_list):
            for idy, y in enumerate(x):
                if y == 'a':
                    Day12.success_path_list = []
                    Day12.moved_position = []
                    Day12.success_step = 0
                    self.start_position = [idx, idy]
                    # print(self.start_position, y)
                    Day12.moved_position.append(self.start_position)
                    Day12.path_list = []
                    tmp_path = [self.start_position]
                    Day12.path_list.append(tmp_path)
                    while Day12.success_step == 0 and len(Day12.path_list) > 0:
                        self.move_one_step()
                    if Day12.success_step != 0:
                        # print("find!!!", Day12.success_step - 1)
                        success_step = Day12.success_step - 1
                        result_list.append(success_step)
                        # print(self.start_position, success_step)
                    # else:
                        # print(self.start_position, "not find,something wrong")
        result_list.sort()
        print(result_list[0])


def compare(char_1, char_2):
    if char_1 >= char_2:
        return True
    elif ord(char_2) - ord(char_1) == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    # P1
    print("p1 sample")
    tmp_list_1_s = read_file_array("day12_1_s.txt")
    p1_s = Day12(tmp_list_1_s)
    p1_s.run()

    print("p1 production")
    tmp_list = read_file_array("day12.txt")
    p1 = Day12(tmp_list)
    p1.run()

    # # P2
    print("p2 sample")
    tmp_list_2_s = read_file_array("day12_1_s.txt")
    p2_s = Day12(tmp_list_2_s)
    p2_s.p2_run()
    #
    print("p2 production")
    tmp_list = read_file_array("day12.txt")
    p2 = Day12(tmp_list)
    p2.p2_run()
