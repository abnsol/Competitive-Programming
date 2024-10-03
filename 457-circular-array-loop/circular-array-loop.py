class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_pos(idx):
            return (idx + nums[idx]) % n
        
        for i in range(n):
            if nums[i] == 0: continue

            slow, fast = i, i
            direction = nums[i]

            while True:
                fast = next_pos(fast)
                slow = next_pos(slow)

                if nums[slow] * direction < 0 or nums[fast] * direction < 0:
                    break
                
                fast = next_pos(fast)
                if slow == fast:
                    if slow == next_pos(slow):
                        break
                    return True
                
            slow = i
            while nums[slow] * direction > 0:
                temp = next_pos(slow)
                nums[slow] = 0
                slow = temp
        
        return False



        

          
