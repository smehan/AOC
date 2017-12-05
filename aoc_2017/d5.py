
class Soln(object):
    def __init__(self):
        self.grid = []
        self.end = 0
        self.run = True
        self.position = 0
        self.steps = 0

    def make_grid(self):
        with open('d5.txt', 'r') as fh:
            self.grid = [int(e.strip('\n')) for e in fh.readlines()]
            self.end = len(self.grid)

    def make_test(self):
        self.grid = [0, 3, 0, 1, -3]
        self.end = len(self.grid)

    def jump(self, part=1):
        last_pos = self.position
        try:
            next_position = last_pos + self.grid[last_pos]
            self.steps += 1
            if part==2 and self.grid[last_pos] > 2:
                self.grid[last_pos] -= 1
            else:
                self.grid[last_pos] += 1
            self.position = next_position
        except:
            self.run = False

"""Now, the jumps are even stranger: after each jump, if the offset was three or more, 
instead decrease it by 1. Otherwise, increase it by 1 as before."""

if __name__ == '__main__':
    soln = Soln()
    soln.make_grid()
    while soln.run:
        soln.jump(part=2)
    print(soln.steps)

