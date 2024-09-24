# Python Program to Calculate the Average of Numbers in a Given List [1,11,21,31,41,51,61,71,81,91]
n=[1,11,21,31,41,51,61,71,81,91]
p=len(n)
sum=0
for i in n:
    sum += i
    result = sum/p
print("Average of Numbers is :",result)