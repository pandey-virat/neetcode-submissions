class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        binary_str = bin(n)[2:]
        binary_dig = [int(digits) for digits in binary_str]
        for binn in binary_dig:
            if binn == 1:
                count += 1

        return count
        
        