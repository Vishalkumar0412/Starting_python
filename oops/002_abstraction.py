class Car:
    def __init__(self):
        self.cluch=False
        self.brk=False
        self.acc=False
    def start(self):
        self.cluch=True
        self.acc=True
        print("Car is started...")
car=Car()
car.start()