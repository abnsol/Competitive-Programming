class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        def reducer(num, count):
            if num == 0:
                return count
            
            if num % 2 == 0:
                count += 1
                return reducer(num/2,count)
            else:
                count += 1
                return reducer(num - 1,count)

        return reducer(num,count)