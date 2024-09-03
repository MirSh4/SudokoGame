from random import sample
from copy import deepcopy


def create_line_coordinates(cell_size):
    points=[]
    for y in range(1,9):
        #Horizontal lines
        #Sabet el x change the y
        temp=[]
        temp.append((0,y*cell_size))
        temp.append((750,y*cell_size))
        points.append(temp)
    for x in range(1,10):
        temp=[]
        temp.append((x*cell_size,0))
        temp.append((x*cell_size,750))
        points.append(temp)

    return points


base  = 3 #SUB_GRID_SIZE
side  = base*base #GRID_SIZE

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s): return sample(s,len(s)) 
def create_grid(base):

    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
    return[ [nums[pattern(r,c)] for c in cols] for r in rows ]

    #for line in board: print(line)

# [6, 2, 5, 8, 4, 3, 7, 9, 1]
# [7, 9, 1, 2, 6, 5, 4, 8, 3]
# [4, 8, 3, 9, 7, 1, 6, 2, 5]
# [8, 1, 4, 5, 9, 7, 2, 3, 6]
# [2, 3, 6, 1, 8, 4, 9, 5, 7]
# [9, 5, 7, 3, 2, 6, 8, 1, 4]
# [5, 6, 9, 4, 3, 2, 1, 7, 8]
# [3, 4, 2, 7, 1, 8, 5, 6, 9]
# [1, 7, 8, 6, 5, 9, 3, 4, 2]


def remove_numbers(grid):
    numofCells= side*side
    #The more the fraction is closer to 100%,the more the cells are empty making the game harder
    empties=numofCells*1//13 #34-Lower the 7 for more difficulty
    for i in sample(range(numofCells),empties):
        grid[i//side][i%side]=0 #to select a cell in the sub squares to make empty




class Grid:
    def __init__(self,font):
        self.cell_size=80
        self.lines_coordinates=create_line_coordinates(self.cell_size)
        self.grid=create_grid(base)
        self.__testgrid= deepcopy(self.grid)
        self.font=font
        self.x_offset=35
        self.y_offset=12
        remove_numbers(self.grid)
        self.occupied_cells_co=self.pre_occupied_cells()
        self.last_clicked = None  # To store the last clicked cell
        self.win=False
    
    def pre_occupied_cells(self):
        occupied_cell_co=[]
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x,y)!=0:
                    occupied_cell_co.append((y,x))
        return occupied_cell_co 

   
    def __draw_lines(self,pg,surface):
        for index, line in enumerate(self.lines_coordinates):
            pg.draw.line(surface,(0,50,0),line[0],line[1])
            if index==2 or index==5 or index==10 or index==13: #from 0 to 7 vertical then horizontal indexes                 
                pg.draw.line(surface,(255,200,0),line[0],line[1])
            else:
                pg.draw.line(surface,(0,50,0),line[0],line[1])


    def __draw_nums(self,surface):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell(x,y)!=0:
                    if(y,x) in self.occupied_cells_co:
                        text=self.font.render(str(self.get_cell(x,y)),False,(0,200,255))
                    else:
                        text=self.font.render(str(self.get_cell(x,y)),False,(0,255,0))
                    if self.get_cell(x,y)!=self.__testgrid[y][x]:
                        text=self.font.render(str(self.get_cell(x,y)),False,(255,0,0))
                    surface.blit(text,(x*self.cell_size+ self.x_offset,y*self.cell_size+self.y_offset))
    
    
    def draw_all(self,pg,surface):
        self.__draw_lines(pg,surface)
        self.__draw_nums(surface)

    
    def get_cell(self,x,y):
        return self.grid[y][x]
    
    
    def set_cell(self,x,y,value):
        self.grid[y][x]=value

    def show(self):
        for cell in self.grid:
            print(cell)

    def get_mouse_click(self,x,y):
        if x<=730:
            grid_x,grid_y= x//80 , y//80
            print(grid_y,grid_x)
            if not self.is_cell_preocc(grid_x,grid_y):
                #self.set_cell(grid_x,grid_y,-1)
                self.last_clicked = (grid_x, grid_y)
        if self.check_grids(): self.win=True


    def is_cell_preocc(self,x,y):
        for cell in self.occupied_cells_co:
            if x==cell[1] and y==cell[0]:
                return True
        return False

    def check_grids(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x]!=self.__testgrid[y][x]:
                    return False
        return True

if __name__=="__main__":
    grid = Grid()
    grid.show()