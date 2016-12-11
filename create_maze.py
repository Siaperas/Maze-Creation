import sys, random

def neighbours(start_x,start_y):
    exists=True
    while(exists==True):
        neighbouring_nodes= []
        if start_x-1 >= 0 :
             neighbouring_nodes.append((start_x-1,start_y))
        if start_y-1 >= 0 :
             neighbouring_nodes.append((start_x,start_y-1))
        if start_x+1 < n:
             neighbouring_nodes.append((start_x+1,start_y))
        if start_y+1 < n:
             neighbouring_nodes.append((start_x,start_y+1))
        random_neighbours = random.sample(neighbouring_nodes, len(neighbouring_nodes))
        exists=False
        for neighbour in random_neighbours:
            x, y =neighbour
            if drawn[x][y]==False:
                drawn[x][y]=True
                file.write("(%d, %d), (%d, %d)\n" %(start_x,start_y,x,y))
                start_x=x
                start_y=y
                exists=True
                break;
            else:
                exists=False
    checkdrawn=True
    for i in range(n):
        for j in range(n):
            if not(drawn[i][j]):
                checkdrawn=False
    
    

n=int(sys.argv[1])
start_x=int(sys.argv[2])
start_y=int(sys.argv[3])
input_seed=str(sys.argv[4])
output_file=str(sys.argv[5])

if (start_x>=n or start_x<0) or (start_y>=n or start_y<0) or len(sys.argv)!=6:
    print ("Please re-enter the parameters correctly.")
else:
    file = open(output_file, "w+")
    random.seed(input_seed)
    drawn= [[False for i in range(n)] for j in range(n)]
    drawn[start_x][start_y]=True
    checkdrawn = neighbours(start_x,start_y)
    while (checkdrawn==False):
        drawnareas =[]
        for i in range(n):
            for j in range(n):
                if drawn[i][j]==True:
                    drawnareas.append((i,j))
        random_drawn=random.sample(drawnareas,len(drawnareas))
        for drawn_node in random_drawn:
            start_x,start_y= drawn_node
            checkdrawn = neighbours(start_x,start_y)
    file.close()            
 
            


