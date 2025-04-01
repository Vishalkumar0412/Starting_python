def rev_the_number(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev

num=int(input("num: "))
print("reverse of number is : ",rev_the_number(num))
