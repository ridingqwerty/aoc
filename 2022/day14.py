#!/usr/bin/env python
import numpy as np

lines=[line.strip() for line in open("day14.input")]

class Cave:
    ticks = 0
    bottomless = True
    def __init__(self, width, depth):
        self.width = width
        self.depth = depth
        self.layout = np.full((width,depth), ".", dtype=str)
        self.source = (0,500)
        self.readout = lines

    def __len__(self):
        return self.depth

    def draw(self, a, b):
        x = min(a[0],b[0]); y = min(a[1],b[1])
        dx = abs(a[0]-b[0]); dy = abs(a[1] - b[1])
        c = max(dx,dy)
        while c >= 0:
            if (a[0] == b[0]): self.layout[y+c][x] = '#'
            else: self.layout[y][x+c] = '#'
            c = c - 1

    def scan_rocks(self):
        points = []
        for line in self.readout:
            points.append ( [tuple(map(int,_.split(","))) for _ in line.split(" -> ")] )
        self.bottom = self.find_bottom()
        return points

    def find_bottom(self):
        bottom = 0
        for line in self.readout:
            bottom = max(bottom, max([int(c.split(',')[1]) for c in line.split(' -> ')]))
        if not self.bottomless:
            bottom += 2
            for i in range(len(self.layout[bottom])):
               self.layout[bottom][i] = '#'
        return bottom

    def plot(self):
        points = self.scan_rocks()
        for sweep in points:
            for i in range(len(sweep)-1):
                self.draw(sweep[i], sweep[i+1])
        self.bottom = self.find_bottom()

        return

    def display(self):
        for line in self.layout[0:13]:
            print(line[490:504])

    def drop_sand(self):
        x,y = self.source
        forever = False
        blockers='#o'

        #self.bottom = self.find_bottom(False)
        self.bottom = self.find_bottom()

        while x < self.bottom:
            for move in [(x+1, y), (x+1,y-1), (x+1,y+1)]:
                if self.layout[move] not in blockers:
                    x,y = move
                    break
            else:
                return True, (x,y)
        return False, (x,y)

    def place_sand(self):
        while True:
            stopped, pos = self.drop_sand()
            if self.bottomless and not stopped:
                break
            self.layout[pos[0]][pos[1]]='o'
            self.ticks = self.ticks + 1
            if not self.bottomless and pos == self.source:
                break


## part 1
cave1 = Cave(5000, 5000)
cave1.plot()
while(cave1.place_sand()): pass

# part 2
cave2 = Cave(5000,5000)
cave2.plot()
cave2.bottomless=False
while(cave2.place_sand()): pass

print(f'Part 1: {cave1.ticks}')
print(f'Part 2: {cave2.ticks}')


