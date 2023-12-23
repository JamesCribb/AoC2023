class Grid:
    def __init__(self, lines):
        self.grid = []
        for row in lines:
            self.grid.append([])
            for cell in row:
                self.grid[-1].append(cell)
        self.width = len(self.grid[0])
        self.height = len(self.grid)
    
    def __str__(self):
        s = ''
        for row in self.grid:
            for cell in row:
                s += cell
            s += '\n'
        return s
    
    def Width(self):
        return self.width
    def Height(self):
        return self.height
    
    def North(self, x, y):
        if y > 0:
            return (x, y-1, self.grid[y-1][x])
    def NorthEast(self, x, y):
        if (x < (self.width - 1)) and (y > 0):
            return (x+1, y-1, self.grid[y-1][x+1])
    def East(self, x, y):
        if x < (self.width - 1):
            return (x+1, y, self.grid[y][x+1])
    def SouthEast(self, x, y):
        if (x < (self.width - 1)) and (y < (self.height - 1)):
            return (x+1, y+1, self.grid[y+1][x+1])
    def South(self, x, y):
        if y < (self.height - 1):
            return (x, y+1, self.grid[y+1][x])
    def SouthWest(self, x, y):
        if (x > 0) and (y < (self.height - 1)):
            return (x-1, y+1, self.grid[y+1][x-1])
    def West(self, x, y):
        if x > 0:
            return (x-1, y, self.grid[y][x-1])
    def NorthWest(self, x, y):
        if (x > 0) and (y > 0):
            return (x-1, y-1, self.grid[y-1][x-1])
    
    def Adjacent(self, x, y):
        adj = []
        fns = [
            self.North, self.NorthEast, self.East, self.SouthEast, 
            self.South, self.SouthWest, self.West, self.NorthWest
        ]
        for fn in fns:
            result = fn(x, y)
            if result:
                adj.append(result)
        return adj
    
    def NESW(self, x, y):
        adj = []
        fns = [self.North, self.East, self.South, self.West]
        for fn in fns:
            result = fn(x, y)
            if result:
                adj.append(result)
        return adj        

    # Return the first occurrence of the given character, starting from (0, 0)
    def Find(self, c):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == c:
                    return (x, y, c)