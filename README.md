# Maze Creation
We have a n x n graph, meaning that we have n rows and n columns. Each and every node represents a room in the maze. To start with, we think that the maze is fully connected. The nodes in the corners have two neighbours, the node in the outer lines have 3 neighbours and the nodes in the inside have four neighbours. We will use python for this project.

## How does the program work
We start from a node in the graph. We note that we have visited that node. We take the neighbours in a random order. If the neighbour has not been visited, we move that node and we save the edge between the two nodes. We actually do an in depth search where we ranomly check on the of the neighbouring nodes. 
When we cannot visit any neibouring node, the procedured is finished and through the edges we now have we have created a maze.

## How to run
In order to run this file from the terminal we have to give the following order

```
python make_maze.py [-n] [height] [-w] [width] [-s] [seed] [-o]
```
Depending on the system where the program is run, you may need to write python3.

We can observe that the program receives five parameters:
* The parameter n represents the height our graph will have
* The parameter w represents the width our graph will have
* The seed is a number or a string that it is given to generate a random seed for our program.
* The -o is set so that the walls of the maze can be stored in a txt file.
