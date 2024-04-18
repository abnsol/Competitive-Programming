class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitBasket = Counter()
        startIdx = 0

        for fruit in fruits:
            fruitBasket[fruit] += 1

            if len(fruitBasket) > 2:
                startfruit = fruits[startIdx]  # like the left pointer in SW
                fruitBasket[startfruit] -= 1

                if fruitBasket[startfruit] == 0: # delete the fruit from the dictionary
                    del fruitBasket[startfruit]
                
                startIdx += 1   # everytime left is increased while fruitBasket > 2 
        
        return len(fruits) - startIdx  # think of it as  