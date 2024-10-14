height = 24  
width = 40   
maxx = 36
maxy = 40    

grid = [[' ' for _ in range(width)] for _ in range(height)]

y_scale = (height - 2) / maxy
x_scale = (width - 2) / maxx

for i in range(height -1):
    grid[i][0] = '|' 
for j in range(width):

    grid[height -1][j] = '-'  
    grid[height -1][0] = '+'  

for x in range(0, maxx + 1):
    y = x + 1
    grid_x = int(1 + x * x_scale)
    grid_y = int(height -1 - y * y_scale)
    if 0 <= grid_x < width and 0 <= grid_y < height:
        grid[grid_y][grid_x] = '*'

for row in grid:
    print(''.join(row))
