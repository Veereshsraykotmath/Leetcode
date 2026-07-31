class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for e in digits:
            num=num*10+e
        num +=1
        digits=[]
        while num>0:
            ld=num%10
            num//=10
            digits.insert(0,ld)
        return digits