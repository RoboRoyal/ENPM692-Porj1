
import copy  # used for deep copy

path_doc = 'my_nodePath.txt'
nodes_doc = 'my_Nodes.txt'
info_doc = 'my_NodesInfo.txt'

size = 2
target = []  # target array, aka finished puzzle

target_found = None
path = []  # path from input to target

node_count = 1
current_node = 0

nodes_to_check = []  # nodes left to be checked
scanned_nodes = []  # nodes already seen, avoid duplicates


# Class to hold info about a node
class Node:
    node_number = 0  # ID of node
    parent_node = 0  # ID of parent node
    board = None     # matrix

    def __init__(self, board):
        global node_count
        self.node_number = node_count
        node_count = node_count + 1
        self.parent_node = current_node
        self.board = board


def get_init():  # gets input from user
    s_node = input("Enter start node: ")
    node = s_node.split()
    for x,i in enumerate(node):
        node[x] = int(i)
    if len(node) != pow(size+1, 2):
        raise Exception("Invalid node")
    if size == 2:
        node = [node[0:3], node[3:6], node[6:9]]
    if size == 3:
        node = [node[0:4], node[4:8], node[8:12], node[12:16]]
    return node


def print_matrix(state):
    for row in state:
        for num in row:
            print(num,'|', end='')
        print('\n--------')


def find_hole(state):  # find the hole ('0')
    for x,i in enumerate(state):
        for y,j in enumerate(i):
            if j == 0:
                return [y,x]


def generate_new(state):  # generates all new possible board from the given board state
    hole = find_hole(state)
    new_states = []

    if hole[0] != size:  # move left
        new = copy.deepcopy(state)
        new[hole[1]][hole[0]] = state[hole[1]][hole[0] + 1]
        new[hole[1]][hole[0] + 1] = 0
        new_states.append(new)

    if hole[1] != 0:  # move up
        new = copy.deepcopy(state)
        new[hole[1]][hole[0]] = state[hole[1] - 1][hole[0]]
        new[hole[1] - 1][hole[0]] = 0
        new_states.append(new)

    if hole[0] != 0:  # move right
        new = copy.deepcopy(state)
        new[hole[1]][hole[0]] = state[hole[1]][hole[0] - 1]
        new[hole[1]][hole[0] - 1] = 0
        new_states.append(new)

    if hole[1] != size:  # mode down
        new = copy.deepcopy(state)
        new[hole[1]][hole[0]] = state[hole[1] + 1][hole[0]]
        new[hole[1] + 1][hole[0]] = 0
        new_states.append(new)

    return new_states


def node_to_string(node):
    ret = ''
    for row in node:
        for num in row:
            ret = ret + str(num) + ' '
    return ret[:-1]  # return all but last space


def add_node(board):  # turns board into a node, adds it to lists
    new_node = Node(board)
    nodes_to_check.append(new_node)
    scanned_nodes.append(new_node)


def write_files():  # writes all data to the three given files
    with open(nodes_doc, 'a') as f:
        for node in scanned_nodes:
            f.write(node_to_string(node.board) + '\n')
    with open(info_doc, 'a') as f:
        for node in scanned_nodes:
            f.write(str(node.node_number) + ' ' + str(node.parent_node) + ' ' + str(0) + '\n')
    with open(path_doc, 'w') as f:
        for node in path:
            f.write(node_to_string(node.board) + '\n')


def seen_before(pot):  # checks if a given board state has been seen before
    for node in scanned_nodes:
        if node.board == pot:
            return True
    return False


def validate_states(new_nodes):  # checks if new nodes(boards) are seen before or if they are the target board state
    global target_found
    for new_node in new_nodes:
        if not seen_before(new_node):  # new node
            add_node(new_node)
        else:
            pass
        if new_node == target:
            print('Found!')
            target_found = Node(new_node)
            return True
    return False


def make_target():  # makes a representation for the target board
    x = 0
    for i in range(size+1):
        row = []
        for j in range(size+1):
            x = x + 1
            row.append(x)
        target.append(row)
    target[size][size] = 0


def trace_back():  # look back through scanned_nodes to find path taken to final board state
    global path
    path.append(scanned_nodes[0])
    prop = target_found
    while prop.node_number != 1:
        path.insert(1, prop)
        prop = scanned_nodes[prop.parent_node - 1]
        print(prop.node_number)
    print('Len: ', len(path))


def clear_files():  # delete all data in files
    open(path_doc, 'w').close()
    open(nodes_doc, 'w').close()
    open(info_doc, 'w').close()


if __name__ == '__main__':
    # initial set up
    clear_files()
    make_target()
    print_matrix(target)
    initial = get_init()
    add_node(initial)

    print_matrix(initial)
    found = False
    new_states = generate_new(initial)
    print_matrix(new_states[0])
    itt = 0
    current_node = 1
    while not found and itt < 20000:
        print(itt)
        itt = itt + 1
        found = validate_states(new_states)
        if not found:
            next_node = nodes_to_check.pop(0)
            current_node = next_node.node_number
            new_states = generate_new(next_node.board)
    trace_back()
    print(itt)
    write_files()

#  1 2 3 0 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9 10 11 0 13 14 15 12
# 1 2 3 4 5 6 0 7 8

# 1 2 3 4 5 6 7 8 9 10 11 12 0 13 14 15
