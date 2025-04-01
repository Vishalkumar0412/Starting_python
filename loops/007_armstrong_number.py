def arm_strong_number(num):
    orginal_num=num
   
    sum=0
    while num>0:
        digit=num%10
        sum+=digit**3
        num//=10
    if sum==orginal_num:
        return True
    else:
        return False

num=int(input("Enter Number: "))

print("yes the number is armstrong number.") if arm_strong_number(num) else print("No the number is not a armstrong number!")