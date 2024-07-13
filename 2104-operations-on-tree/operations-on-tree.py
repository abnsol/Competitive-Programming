class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = {}
        self.g = defaultdict(list)
        for i in range(len(parent)):
            if parent[i] != -1:
                self.g[parent[i]].append(i)

    def lock(self, num, user):
        if num not in self.locked:
            self.locked[num] = user
            return True
        return False        

    def unlock(self, num, user):
        if num in self.locked and self.locked[num] == user:
            del self.locked[num]
            return True
        return False
    
    def ancestor(self, node):
        while node != -1:
            if node in self.locked:
                return True
            node = self.parent[node]
        return False

    def descendant(self, node):
        if node in self.locked:
            return True
        for child in self.g[node]:
            if self.descendant(child):
                return True
        return False
    
    def unlockall(self, node):
        for child in self.g[node]:
            self.unlockall(child)
            if child in self.locked:
                del self.locked[child]

    def upgrade(self,num, user): 
        if num not in self.locked and not self.ancestor(num) and self.descendant(num):
            self.unlockall(num)
            self.lock(num, user)
            return True
        return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num, user)
# param_2 = obj.unlock(num, user)
# param_3 = obj.upgrade(num, user)
