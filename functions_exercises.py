#Q1
def convert_fahrenheit_to_celsiu(temperature):
    return (temperature-32)*5/9

temp_in_f = int(input("please enter the fahrenheit temperature you need to convert to celsiu : "))

print(f"{temp_in_f}°F = {convert_fahrenheit_to_celsiu(temp_in_f)}°C")

#Q2
def odd_number(number):
    if number%2 == 0: 
        print("False")
    else :
        print("True")

number = int(input("Please enter a number to check if it's odd : ")) 
odd_number(number)

#Q3
def mean_calculator(num_list):
    counter=0
    total=0
    for number in num_list:
        total+= number
        counter+=1
    return total/counter

num_list=[]

number= input("Please enter the first number of the numbers you want to calculate the mean, press enter to continue and # to stop : ")
while number!="#" :
    num_list.append(float(number))
    number=input("Please enter the next number or press # to stop : ")

print(f"The mean of {num_list} is {mean_calculator(num_list)}")

#Q4
def total_cost(price_per_unit, num_unit):
    return f"${price_per_unit*num_unit}"

price_per_unit = float(input("Please enter the unit price : "))
num_list = float(input("Please enter how many units were purchased : "))

print(total_cost(price_per_unit,num_list))





