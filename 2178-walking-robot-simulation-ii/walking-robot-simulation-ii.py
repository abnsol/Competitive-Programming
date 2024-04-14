class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        self.dirstr = ["East","North","West","South"]
        self.dirIdx = self.posX = self.posY = 0

    def step(self, num: int) -> None:
        num %= (self.width - 1 + self.height - 1) * 2
        if num == 0:
            num += (self.width - 1 + self.height - 1) * 2
        
        for _ in range(num):
            nx, ny = self.posX + self.dirs[self.dirIdx][0], self.posY + self.dirs[self.dirIdx][1]

            while not(0 <= nx < self.width and  0 <= ny < self.height):
                self.dirIdx = (self.dirIdx + 1) % 4
                nx, ny = self.posX + self.dirs[self.dirIdx][0], self.posY + self.dirs[self.dirIdx][1]

            self.posX, self.posY = nx, ny
        
        

    def getPos(self) -> List[int]:
        return [self.posX,self.posY]

    def getDir(self) -> str:
        return self.dirstr[self.dirIdx]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()