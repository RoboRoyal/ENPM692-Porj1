# ENPM692-Porj1
Project 1 for ENPM692, Spring 2021


This program solves a 4x4 sliding puzzle, also know as a 15-puzzle, using a brute-force, breath first search.
The program then writes out infor about the nodes, as well as the path, to text files.
To solve a puzzle, run the program. This can be doen from an IDE or from the command line.
In either case it should be noted this is only tested for python3.
The program will then prompt you for the puzzle. Enter the puzzle in matrix notation.
The hole, or the empty space, is notated by a '0'.


Matrix notation, in target configuration:
[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]

Would be the equivilant as the puzzle:

----------
1 |2 |3 |4
----------
5 |6 |7 |8
----------
9 |10|11|12
----------
13|14|14|0
----------

The rules for a sliding puzzle can be found here:https://en.wikipedia.org/wiki/15_puzzle

Sample program output for test case 1
```
Enter start node: [[1, 2, 3, 4],[ 5, 6,0, 8], [9, 10, 7, 12] , [13, 14, 11, 15]]
Found!
Number of nodes searched:  16
Length of path:  4
```

The first file it writes to is 'Nodes.txt'. 
It writes ever node searched by the algorithm, one per line, in the order they were encountered.
Theya re writin in matrix order, with all commas and brackets removed.

The next file it writes to is 'NodesInfo.txt'.
In this file, every node number is listed with the parent node number listed next to it.

The last file it writes to is 'nodePath.txt'.
This writes out each board configuration in the order to get to the end state.
Each node is writen out as in 'Nodes.txt'

This program imports the copy library to use the function 'deepcopy' to make deep copies of matrixs.

This project can be found on GitHub at: https://github.com/RoboRoyal/ENPM692-Porj1
