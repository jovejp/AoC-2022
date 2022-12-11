# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won


point_list_1 = {"A X": 1 + 3, "A Y": 2 + 6, "A Z": 3 + 0, "B X": 1 + 0, "B Y": 2 + 3, "B Z": 3 + 6, "C X": 1 + 6, "C Y": 2 + 0, "C Z": 3 + 3 }

# A for Rock, B for Paper, and C for Scissors.
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
# 0 if you lost, 3 if the round was a draw, and 6 if you won
point_list_2 = {"A X": 0 + 3, "A Y": 3 + 1, "A Z": 6 + 2, "B X": 0 + 1, "B Y": 3 + 2, "B Z": 6 + 3, "C X": 0 + 2, "C Y": 3 + 3, "C Z": 6 + 1 }


def get_point_1(key):
    if key in point_list_1:
        return point_list_1[key]


def get_point_2(key):
    if key in point_list_2:
        return point_list_2[key]


def day_2(main_list):
    sum_point_1 = 0
    sum_point_2 = 0
    for key in main_list:
        # print(key)
        sum_point_1 = sum_point_1 + get_point_1(key)
        sum_point_2 = sum_point_2 + get_point_2(key)
    return sum_point_1, sum_point_2
