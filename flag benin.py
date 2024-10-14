GREEN = '\033[42m'
YELLOW = '\033[43m'
RED = '\033[41m'
RST = '\033[0m'

height = 15       
width = 60         
green_width = width // 3  
for i in range(height):
    line = ""
    for j in range(width):
        if j < green_width:
            line += GREEN + " "  
        elif height // 2 > i:
            line += YELLOW + " "  
        else:
            line += RED + " "     
    line += RST
    print(line)
