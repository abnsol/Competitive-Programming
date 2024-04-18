class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitBasket = Counter()
        startIdx = 0

        for fruit in fruits:
            fruitBasket[fruit] += 1

            if len(fruitBasket) > 2:
                startfruit = fruits[startIdx]
                fruitBasket[startfruit] -= 1

                if fruitBasket[startfruit] == 0:
                    del fruitBasket[startfruit]
                
                startIdx += 1
        
        return len(fruits) - startIdx