class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = (0,1,0,-1,0)
        maxDistance = directionsIndex = 0 
        posX = posY = 0
        obs = {(x,y) for x,y in obstacles}

        for command in commands:
            if command == -2:
                directionsIndex = (directionsIndex + 3) % 4
            elif command == -1:
                directionsIndex = (directionsIndex + 1) % 4
            else:
                for _ in range(command):
                    nx , ny = posX + directions[directionsIndex], posY + directions[directionsIndex + 1]

                    if (nx,ny) in obs:
                        break
                    
                    posX , posY = nx , ny
                    maxDistance = max(maxDistance, posX * posX + posY * posY)
            
        return maxDistance