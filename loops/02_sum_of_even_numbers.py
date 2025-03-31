# nums=[4,7,3,6,8,9,5]
# sum=0
# for num in nums:
#     if num%2==0:
#         sum+=num
# print(sum)


#for n numbers
def sum_of_even(n):
    sum=0
    for num in range(n+1):
        if num%2==0:
            sum+=num
    return sum

print(sum_of_even(10))