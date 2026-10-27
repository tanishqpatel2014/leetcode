"""
type x: int
:rtype: int
"""
class Solution(object):
    # x=int(input())
    def sumOfTheDigitsOfHarshadNumber(self, x):
        b=x
        total=0
        while x>0:
            a=x%10
            total+=a
            x=x//10
        if b%total==0:
            return total
        else:
            return -1
        

# x=int(input())
# b=x
# def sumOfTheDigitsOfHarshadNumber(x,b):
#     total=0
#     while x>0:
#         a=x%10
#         total+=a
#         x=x//10
#     if b%total==0:
#         return total
#     else:
#         return "-1"


# print(sumOfTheDigitsOfHarshadNumber(x,b))