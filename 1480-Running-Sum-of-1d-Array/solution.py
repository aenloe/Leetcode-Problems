class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        output = [] 
        sum = 0
        for number in nums:
            sum += number
            output.append(sum)

        return output


