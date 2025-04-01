class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg(self):
        sum=0
        for val in self.marks:
            sum=sum+val
        print("avg : ",sum//3)  

s1=Student("vishal",[98,65,76])
s1.avg()

        