class ThroneInheritance:
    def __init__(self, kingName: str):
        self.g = defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str):
        self.g[parentName].append(childName)

    def death(self, name: str):
        self.dead.add(name)

    def getInheritanceOrder(self):
        def dfs(node,order):
            if not self.g[node]:
                return []

            for succ in self.g[node]:
                if succ not in self.dead:
                    order.append(succ)
                dfs(succ,order)
            return order

        if not self.g[self.king]:
            return [self.king]

        curOrder = dfs(self.king,[self.king])
        if self.king in self.dead:
            curOrder.pop(0)   
        return curOrder


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()