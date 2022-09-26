# Creating the first class
class Phone:
    def make_call(self):
        print("I am making a call")
    def play_game(self):
        print("I am playing a game")

p1=Phone()

p1.make_call()
p1.play_game()

# Adding parameters to the class
class Phone:
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
    def make_call(self):
        print ("Making phone call")
    def play_game(self):
        print ("Playing game")

p2 = Phone()

p2.set_color("Blue")
p2.set_cost(50000)
p2.show_color()              ##
p2.show_cost()               ##
p2.make_call()
p2.play_game()


# Creating a class with constructor
class Employee:
    def __init__(self, name, age, salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def show_Employee_details(self):
        print('Name of the enployee is',self.name)
        print('Age of the empoyee is',self.age)
        print('Salary of the empoyee is',self.salary)
        print('Gender of the empoyee is',self.gender)

e1=Employee("Ram",29, 90000, 'Male')

e1.show_Employee_details()

# Inheritance in Python

## Creating the base class (Superclass)
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost
    def show_Vehicle_details(self):
        print("This is a vehicle")
        print("Mileage is", self.mileage)
        print("Cost is", self.cost)

## Instatiating the object for base class
v1=Vehicle(500,75000)
v1.show_Vehicle_details()

## Creating the child class (Subclass)
class car(Vehicle):
    def show_car_details(self):
        print("I am a car")

## Instatiating the object for child class
c1=car(500,15000)
c1.show_Vehicle_details()

## Invoking the child class method
c1.show_car_details()

# Over-riding init method

## Overriding init method
class car(Vehicle):
    def __init__(self, mileage, cost,tyres,hp):
        super(). __init__(mileage,cost)
        self.tyres=tyres
        self.hp=hp
    def show_car_details(self):
        print("I am a car")
        print("No. of tyres are",self.tyres)
        print("Value of horse power is", self.hp)

## Invoking show_vehicle_details() method from parent class
c1=car(20,15000,4,800)
c1.show_Vehicle_details()

## Invoking show_car_details() method from child class
c1.show_car_details()


## TYPES OF INHERITANCE
class Shape:
    def __init__ (self, c, b):
        self.color=c
        self.borderwidth=b
    def area(self):
        return-1
    def setcolor(self,c):
        self.color=c
    def getcolor(self):
        return self.color

 ## Circle class
 class Circle(Shape):
     Pi=3.14
     # c &  b are optional
     def __init__(self,r,c="", b=0):
         self.radius=r
         super(Circle,self).__init__(c,b)
         def area(self): # override method
             return self.radius*self.radius*Circle.Pi
Create instance
c1=Circle(2,'Red',5)
c2=Circle(3,'Blue')
c3=Circle(4)
print(cl.area())

## Rectangle class


