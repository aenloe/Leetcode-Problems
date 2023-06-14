class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0 

        for each_customer in accounts:
            summedwealth = 0
            for each_bank in each_customer:
                summedwealth += each_bank
            
            if summedwealth > maxwealth:
                maxwealth = summedwealth
        
        return maxwealth

