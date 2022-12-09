from treelib import Tree, Node


def sum_data(tree, node_name):
    node_tmp = tree.get_node(node_name)
    node_sum_value = 0
    if node_tmp.is_leaf():
        return node_tmp.data
    else:
        node_list = tree.is_branch(node_name)
        for x in node_list:
            node_sum_value = node_sum_value + sum_data(tree, x)
    return node_sum_value


def day7_1(my_list):
    cur_id = 0
    next_id = 0
    leaf_id = 0
    parent_id = 0
    node_list = []
    node_str_list = []
    tree = Tree()
    for x in my_list:
        tmpA = x.split(" ")
        if len(tmpA) == 3:
            if tmpA[1] == 'cd':
                if tmpA[2] == "..":
                    node_tmp = tree.parent(str(cur_id) + "-" + node_str_list[cur_id])
                    parent_id = int(node_tmp.tag.split("-")[0])
                    cur_id = parent_id
                else:
                    if next_id == 0:  # root
                        node_list.append(next_id)
                        node_str_list.append(tmpA[2])
                        tree.create_node(tag=str(next_id) + "-" + node_str_list[next_id],
                                         identifier=str(next_id) + "-" + node_str_list[next_id], data=0)
                        next_id += 1
                    elif next_id > 0:
                        node_list.append(next_id)
                        node_str_list.append(tmpA[2])
                        tree.create_node(tag=str(next_id) + "-" + node_str_list[next_id],
                                         identifier=str(next_id) + "-" + node_str_list[next_id],
                                         parent=str(parent_id) + "-" + node_str_list[parent_id],
                                         data=0)
                        cur_id = next_id
                        parent_id = cur_id
                        next_id += 1

        elif len(tmpA) == 2:
            # if tmpA[0] == 'dir':
            # elif tmpA[1] == 'ls':
            if tmpA[0].isnumeric():
                tree.create_node(tag=str(leaf_id) + "-" + tmpA[1],
                                 identifier=str(leaf_id) + "-" + tmpA[1],
                                 parent=str(cur_id) + "-" + node_str_list[cur_id],
                                 data=int(tmpA[0]))
                leaf_id += 1

    # tree.show()
    data_list = []
    for x in node_list:
        node_name_list = str(x) + "-" + node_str_list[x]
        data_list.append(sum_data(tree, node_name_list))

    data_list.sort()
    # print(data_list)

    # P1
    sum_total = 0
    print("P1 production")
    for y in data_list:
        if y <= 100000:
            sum_total += y
        else:
            break
    print(sum_total)
    # P2
    print("P2 production")
    i = 0
    for y in data_list:
        if y <= 8748071:
            i += 1
        else:
            break
    print(data_list[i])
