from curses.textpad import rectangle
from math import sqrt

#Q1
class Book():
    def __init__(self, title, author, pages, current_page):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = current_page
        self.book_mark = 1
    
    def bookmark_page(self):
        mark = input(F"We are now in page {self.current_page} please enter Y if you would like to mark the current page.\nOr enter the page no. you wish to marked.\n:")
        if mark == "Y":
            self.book_mark=self.current_page
        else:
            if int(mark) <= self.pages:
                self.book_mark = int(mark)
            else:
                print(f"This book only have {self.pages} pages.")
        print(f"The book is marked at page {self.book_mark}.")
            
    def turn_page(self):
        direction = input(F"We are now in page {self.current_page} please enter :\nF if you want to go foward\nB if you want to go back\nOr the page no. you wish to turn to\n: ")
        if direction == "F":
            if self.current_page < self.pages:
                self.current_page  += 1
            else:
                self.current_page = 1
        elif direction == "B":
            self.current_page  -= 1
        else :
            if int(direction) <= self.pages:
                self.current_page = int(direction)
            else:
                print(f"This book only have {self.pages} pages.")
      
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"
    

my_book = Book("A grate book", "me", 198, 1)
print(my_book)
my_book.turn_page()
my_book.turn_page()
my_book.bookmark_page()

#Q2
class Rectangle():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def cal_area(self):
        self.area = self.width*self.height
       

    def cal_perimeter(self):
        self.perimeter = self.width*2+self.height*2
        
    
    def cal_diagonal(self):
        self.diagonal = sqrt(self.width**2+self.height**2)
    
    def if_square(self):
        if self.width == self.height:
            print("This rectangle is a square.")
        else:
            print("This rectangle is not a square.")

my_rectangle = Rectangle(int(input("Please enter the width of the rectangle : ")), int(input("Please enter the height of the rectangle : ")))
my_rectangle.cal_area()
print(f"The area of this rectangle is : {my_rectangle.area}")
my_rectangle.cal_perimeter()
print(f"The perimeter of this rectangle is : {my_rectangle.perimeter}")
my_rectangle.cal_diagonal()
print(f"The length of the diagonal of this rectangle is : {my_rectangle.diagonal}")
my_rectangle.if_square()

#Q3 and Q4
class Vehicle():
    def __init__(self, make_and_model, colour, seating_capacity, maximum_speed,max_fuel,fuel_per_km):
        self.make_and_model = make_and_model
        self.colour = colour
        self.seating_capacity = seating_capacity
        self.maximum_speed = maximum_speed
        self.max_fuel = int(max_fuel)
        self.fuel_per_km = int(fuel_per_km)
        self.fuel = 0

    def rev_engine (self):
        print("VARROOOOOOOOOMMMMM!!!BRMMMMMMMMMM!!!!") 

    def fuel_refuel(self):
        print(f"There are {self.fuel} L fuel in the tank, the maximum capacity of the fuel tank is {self.max_fuel}.")
        self.fuel += int(input("Please enter how many liter to refuel : "))
        if self.fuel > self.max_fuel:
            print(f"Exceed maximum capacity of the fuel tank! Refueled to maximum capacity of {self.max_fuel}L.")
            self.fuel = self.max_fuel
        
    def drive_and_fuel_check(self):
        self.fuel_use = int(input("How many km to drive?"))*self.fuel_per_km
        if self.fuel_use < self.fuel:
            self.fuel -= self.fuel_use
            self.rev_engine()
            if self.fuel< self.max_fuel/10:
                print("There is less than 10% fuel in the tank, please refuel.")
                self.fuel_refuel()
        else:
            if self.fuel_use > self.max_fuel:
                print("The fuel usage of this distance is larger than the the maximum capacity of the fuel tank.")
            elif self.fuel_use == self.fuel:
                print("You will use all of fuel if you drive this distance.\nPlease refuel first, or shorten your drive if the tank already full.")
                self.fuel_refuel()
            else:
                print("There will be not enough fuel to drive this distance, please refuel first.")
                self.fuel_refuel()

    def __str__(self) -> str:
        return f"Make and model : {self.make_and_model}, Colour : {self.colour}, Seating capacity : {self.seating_capacity}, Maximum speed : {self.maximum_speed}"


my_car = Vehicle(input("Please enter the Make and model of the vehicle : "), input("Please enter the colour of the vehicle : "),input("Please enter the seating capacity of the vehicle : "),input("Please enter the maximum speed of the vehicle : "),input("Please enter the maximum capacity of the fuel tank :"), input("Please enter the fuel usage per km of the vehicle : "))
print(my_car)
my_car.fuel_refuel()
my_car.drive_and_fuel_check()
my_car.drive_and_fuel_check()




