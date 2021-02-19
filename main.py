
import copy

path_doc = 'my_nodePath.txt'
nodes_doc = 'my_Nodes.txt'
info_doc = 'my_NodesInfo.txt'
node_count = 1
current_node = 0
target = []
size = 2
nodes_to_scan = []
scanned_nodes = []

def getInit():
    s_node = input("Enter start node: ")
    node = s_node.split()
    for x,i in enumerate(node):
        node[x] = int(i)
    if len(node) != 9:
        raise Exception("Invalid node")
    node = [node[0:3], node[3:6], node[6:9]]
    return node

def print_matrix(state):  # from plot_path.py
    counter = 0
    for row in range(0, len(state), size+1):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(state), size+1):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")

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

def print_state(state):
    for row, i in enumerate(state):
        print(str(i[0])+'|'+str(i[1])+'|'+str(i[2]))
        if row != 2:
            print('-----')

def node_to_string(node):
    ret = ''
    for row in node:
        for num in row:
            ret = ret + str(num) + ' '
    return ret[:-1]  # return all but last space

def add_node(node):
    global node_count
    #write to Nodes
    with open(nodes_doc, 'a') as f:
        f.write(node_to_string(node) + '\n')
    #write to NodesInfo
    with open(info_doc, 'a') as f:
        f.write(str(node_count) + ' ' + str(current_node) + ' ' + str(0) + '\n')
    nodes_to_scan.append(node)
    node_count = node_count + 1

def validate_states(new_nodes):
    nodes = []
    with open(nodes_doc) as f:
        lines = f.read().splitlines()
    #print(lines)
    for new_node in new_nodes:
        if node_to_string(new_node) not in lines: # new node
            add_node(new_node)
        else:
            #print('got that one')
            pass
        if new_node == target:
            print('Found!')
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

if __name__ == '__main__':
    make_target()
    print_state(target)
    initial = getInit()

    print_state(initial)
    found = False
    new_states = generate_new(initial)
    print_state(new_states[0])
    itt = 0
    while not found and itt < 20000:
        print(itt)
        itt = itt + 1
        found = validate_states(new_states)
        if not found:
            #current_node = parent_node.pop()
            new_states = generate_new(nodes_to_scan.pop(0))
    #recunstruct path

    print(itt)

#  1 2 3 0 4 5 6 7 8

