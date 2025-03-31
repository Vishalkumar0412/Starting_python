# check the entered number is even or odd

# num=int(input("num: "))
# if(num%2==0):
#     print("even")

# else:
#     print('odd')

# find the greatest of 3 number entered by user

num1=int(input('num1 :'))
num2=int(input('num2 :'))
num3=int(input('num3 :'))

if(num1>num2 and num1 > num3):
    print("num1: "+num1)
elif(num2>num1 and num2>num3):
    print("num2: ",num2)
else:
    print("num3 ",num3)