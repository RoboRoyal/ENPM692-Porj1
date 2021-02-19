
import copy

path_doc = 'my_nodePath.txt'
nodes_doc = 'my_Nodes.txt'
info_doc = 'my_NodesInfo.txt'

size = 2
target = []

target_found = None
path = []

node_count = 1
current_node = 0

nodes_to_check = []
scanned_nodes = []

class node:
    node_number = 0
    parent_node = 0
    node = None
    def __init__(self, node):
        global node_count
        self.node_number = node_count
        node_count = node_count + 1
        self.parent_node = current_node
        self.node = node

def getInit():
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
            print(num,'|', end = '')
        print('\n--------')

def find_hole(state):
    for x,i in enumerate(state):
        for y,j in enumerate(i):
            if j == 0:
                return [y,x]

def generate_new(state):
    hole = find_hole(state)
    #print(hole)
    new_states = []
    if hole[0] != size: #move left
        #print('left')
        new = copy.deepcopy(state)
        new[hole[1]][hole[0]] = state[hole[1]][hole[0] + 1]
        new[hole[1]][hole[0] + 1] = 0
        new_states.append(new)
    if hole[1] != 0: #move up
        #print('up')
        new = copy.deepcopy(state)
        new[hole[1]][hole[0]] = state[hole[1] - 1][hole[0]]
        new[hole[1] - 1][hole[0]] = 0
        new_states.append(new)
    if hole[0] != 0:#move right
        #print('right')
        new = copy.deepcopy(state)
        new[hole[1]][hole[0]] = state[hole[1]][hole[0] - 1]
        new[hole[1]][hole[0] - 1] = 0
        new_states.append(new)
    if hole[1] != size:
        #print('down')
        new = copy.deepcopy(state)
        new[hole[1]][hole[0]] = state[hole[1] + 1][hole[0]]
        new[hole[1] + 1][hole[0]] = 0
        new_states.append(new)
    #print(new_states)
    return new_states

def node_to_string(node):
    ret = ''
    for row in node:
        for num in row:
            ret = ret + str(num) + ' '
    return ret[:-1]  # return all but last space

def add_node(new_node):
    new_node = node(new_node)
    nodes_to_check.append(new_node)
    scanned_nodes.append(new_node)

def write_files():
    with open(nodes_doc, 'a') as f:
        for node in scanned_nodes:
            f.write(node_to_string(node.node) + '\n')
    with open(info_doc, 'a') as f:
        for node in scanned_nodes:
            f.write(str(node.node_number) + ' ' + str(node.parent_node) + ' ' + str(0) + '\n')
    with open(path_doc, 'w') as f:
        for node in path:
            f.write(node_to_string(node.node)+ '\n')

def seen_before(pot):
    for node in scanned_nodes:
        if node.node == pot:
            return True
    return False

def validate_states(new_nodes):
    global target_found
    for new_node in new_nodes:
        if not seen_before(new_node): # new node
            add_node(new_node)
        else:
            #print('got that one')
            pass
        if new_node == target:
            print('Found!')
            target_found = node(new_node)
            return True
    return False

def make_target():
    x = 0
    for i in range(size+1):
        row = []
        for j in range(size+1):
            x = x + 1
            row.append(x)
        target.append(row)
    target[size][size] = 0

def trace_back():
    global path
    path.append(scanned_nodes[0])
    prop = target_found
    while prop.node_number != 1:
        path.insert(1, prop)
        prop = scanned_nodes[prop.parent_node - 1]
        print(prop.node_number)
    # path.append(node(target))
    print('Len: ', len(path))

def clear_files():
    open(path_doc, 'w').close()
    open(nodes_doc, 'w').close()
    open(info_doc, 'w').close()

if __name__ == '__main__':
    clear_files()
    make_target()
    print_matrix(target)
    initial = getInit()
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
            next = nodes_to_check.pop(0)
            current_node = next.node_number
            new_states = generate_new(next.node)
    #recunstruct path
    trace_back()
    print(itt)
    write_files()

#  1 2 3 0 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9 10 11 0 13 14 15 12
# 1 2 3 4 5 6 0 7 8

# 1 2 3 4 5 6 7 8 9 10 11 12 0 13 14 15
