from func_utils import read_file_array


class Day13:
    # class variables
    def __init__(self, data_list):
        # instance variables
        self.data_list = data_list

    def print_data(self):
        for x in self.data_list:
            print(x)

    def run_p1(self):
        print("run")

    def run_p2(self):
        print("run")


if __name__ == '__main__':
    # P1
    print("p1 sample")
    tmp_list_1_s = read_file_array("day13_1_s.txt")
    p1_s = Day13(tmp_list_1_s)
    p1_s.run_p1()

    print("p1 production")
    tmp_list = read_file_array("day13.txt")
    p1 = Day13(tmp_list)
    p1.run_p1()

    # # P2
    print("p2 sample")
    tmp_list_2_s = read_file_array("day13_1_s.txt")
    p2_s = Day13(tmp_list_2_s)
    p2_s.run_p2()
    #
    print("p2 production")
    tmp_list = read_file_array("day13.txt")
    p2 = Day13(tmp_list)
    p2.run_p2()
