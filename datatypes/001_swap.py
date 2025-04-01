# swap 
def swap(num1,num2):
    temp=num1
    num1=num2
    num2=temp
    return num1,num2
   
num1=int(input("num1: "))
num2=int(input("num2: "))

print("Before swaping")
print("num1",num1)
print("num1",num2)
print("After swaping")
num1,num2=swap(num1,num2)
print("num1",num1)
print("num1",num2)