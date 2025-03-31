# conditionals


# A=int(input("A: "))
# G=input("M/F: ")
# if((A==1 or A==2)and G=="M"):
#     print("fee is 100")
# elif(A==3 or A==4 or G=="F"):
#     print("fee is 200")
# else:
#     print("no fee")

#ternary 

# food=input("food:'")
# eat="Yes" if food=="cake" else "No"
# print(eat)
# print("Yes") if food=="cake" else print("no")

age=int(input("age: "))
vote=("Yes","No") [age<18]
print(vote)