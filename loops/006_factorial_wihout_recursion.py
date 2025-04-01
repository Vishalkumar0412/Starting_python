#method wihout recursion
def factorial_without_recursion(num):
    if num<0:
        return None   
    elif num==0:
        return 1
                    
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

num=int(input("Enter the number: "))
factrial_of_num=factorial_without_recursion(num)
if factrial_of_num is not None: 
    print("Factorial of The number is : ",factrial_of_num)
else:
    print("Factorial is not defined for negative numbers.")
