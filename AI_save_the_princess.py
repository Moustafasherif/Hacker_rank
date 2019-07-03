#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    moves = []
    for i in range(0,n):
        for j in range(0,n):
            if grid[i][j] == 'm':
                bot = [i,j]
            if grid[i][j] == 'p':
                princess  = [i,j]
    while(bot[0]!=princess[0]):
        if bot[0] > princess[0]:
            moves.append('UP')
            bot = [bot[0]-1,bot[1]]
        elif  bot[0] < princess[0]:
            moves.append('DOWN')
            bot = [bot[0]+1,bot[1]]
    while(bot[1]!=princess[1]):
        if bot[1] > princess[1]:
            moves.append('LEFT')
            bot = [bot[0],bot[1]-1]
        elif  bot[1] < princess[1]:
            moves.append('RIGHT')
            bot = [bot[0],bot[1]+1]
    for p in moves:
        print(p)
    
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
