#For Loops: Exercises

#Q1
times=input("Enter a number: ")
for num in range(1,int(times)+1):
    result=int(times) * int(num)
    print(f"{times} * {num} = {result}")


#Q2
num_total = input ("Enter a number: ")
result_total=0
for num_add in range (0,int(num_total)+1):
    result_total=result_total+num_add
print(result_total)

#Q3
random_numbers = []
list_len = int(input("How many numbers are there in your list ? "))
item_numbers = 1
sum = 0

for list_numbers in range (list_len):
    list_numbers = int(input(f"Please enter item {item_numbers} in your list : "))
    random_numbers.append(list_numbers)
    item_numbers = item_numbers + 1

print(F"You entered the following list of numbers to be sumed up : {random_numbers}")

for list_numbers in random_numbers:
    sum = sum + list_numbers

print(f"The results is: {sum}")

#Q4
mailing_list = [
      ["Chilli", "chilli@thechihuahua.com"],
      ["Roary", "roary@moth.catchers"],
      ["Remus", "remus@kapers.dog"],
      ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
      ["Ivy", "noreply@goldendreamers.xyz"],
]
for item in mailing_list:
    print(f"{item[0]} : {item[1]}")

# While Loops: Exercises

#Q1
sum=0
number_entered = input("Enter a number : ")
while len(number_entered)!=0:
    sum = sum+int(number_entered)
    number_entered = input("Enter a number : ")
print (sum)

#Q2
number_entered = input("Enter a number : ")
number_print = 1
while int(number_entered)-number_print >=0:
    print(number_print)
    number_print=number_print+2

#Q3
number_selected = 25
number_entered = int(input("Guess the number : "))

while number_entered != number_selected:
    while number_entered < number_selected :
        print ("Too low!")
        number_entered = int(input("Guess the number : "))
    while number_entered > number_selected :
        print ("Too high!")
        number_entered = int(input("Guess the number : "))

print("Correct!")

#Extension

#Q1
groceries = [
      ["Baby Spinach", 2.78],
      ["Hot Chocolate", 3.70],
      ["Crackers", 2.10],
      ["Bacon", 9.00],
      ["Carrots", 0.56],
      ["Oranges", 3.08]
]
receipt = []
total = 0
x=" "
for item in groceries:
    units = int(input(f"How many {item[0]} do you bought? "))
    amount = item[1]*units
    format_amount = "{:.2f}".format(amount)
    space = 18-len(item[0])
    receipt.append ([item[0], x*space, format_amount])
    total = total+amount 
print("====Izzy's Food Emporium====") 
for item in receipt :   
    print(f"{item[0]}{item[1]}${item[2]}")
print("============================")
format_total = "{:.2f}".format(total)
print(f"{x*18}${format_total}")

#Q2
string_input = input("Please enter a string: ")
list_input = list(string_input.strip())
position = 0
for character in list_input:
    print(f"{position} {character}")
    position = position+1

#Q3
size = int(input("Pyramid size: "))
star ="*"
for level in range(size) :
    print (f"{star*(level+1)}") 

#Q4
size = int(input("Pyramid size: "))
star ="*"
space = " "
for level in range(size) :
    star_num = 1+level*2
    space_num =size-level-1
    print (f"{space*space_num}{star*star_num}{space*space_num}")


