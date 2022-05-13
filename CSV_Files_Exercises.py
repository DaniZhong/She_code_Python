import csv
import os
import sys
from typing import Counter

#Q1
with open(os.path.join(sys.path[0], "colours_20_simple.csv")) as csv_file:
    reader=csv.reader(csv_file)
    for colour_name in reader:
        print(f"{colour_name[0]} {colour_name[1]} {colour_name[2]}")

#Q2
with open(os.path.join(sys.path[0], "colours_20_simple.csv")) as csv_file:
    reader=csv.reader(csv_file)
    colour_data = []
    for row in reader:
        colour_data.append(row)
    for item in range (1,len(colour_data)):
        print (f"{colour_data[item][2]}, {colour_data[0][1]}: {colour_data[item][1]}, {colour_data[0][0]}: {colour_data[item][0]} ")

#Q3
with open(os.path.join(sys.path[0], "colours_20.csv")) as csv_file:
    reader=csv.reader(csv_file)
    colour_data = []
    for row in reader:
        colour_data.append(row)
    for item in range (1,len(colour_data)):
        print (f"{colour_data[item][4]}, {colour_data[0][2]}: {colour_data[item][2]}, {colour_data[0][1]}: {colour_data[item][1]} ")
           
#4
with open(os.path.join(sys.path[0], "colours_20.csv")) as csv_file:
    reader=csv.reader(csv_file)
    counter_red=0
    counter_green=0
    counter_blue=0
    counter_yellow=0
    for row in reader:
        if "red" in row[4]:
           counter_red+=1
        elif "green" in row[4]:
            counter_green+=1
        elif "blue" in row[4]:
            counter_blue+=1
        elif "yellow" in row[4]:
            counter_yellow+=1
    print(f"Red: {counter_red}")
    print(f"Green: {counter_green}")
    print(f"Blue: {counter_blue}")
    print(f"Yellow: {counter_yellow}")

with open(os.path.join(sys.path[0], "colours_213.csv")) as csv_file:
    reader=csv.reader(csv_file)
    counter_red=0
    counter_green=0
    counter_blue=0
    counter_yellow=0
    for row in reader:
        if "red" in row[4]:
           counter_red+=1
        elif "green" in row[4]:
            counter_green+=1
        elif "blue" in row[4]:
            counter_blue+=1
        elif "yellow" in row[4]:
            counter_yellow+=1
    print(f"Red: {counter_red}")
    print(f"Green: {counter_green}")  
    print(f"Blue: {counter_blue}")
    print(f"Yellow: {counter_yellow}")

#5
with open(os.path.join(sys.path[0], "galaxies.csv")) as csv_file:
    reader=csv.reader(csv_file)
    counter = 0

    for row in reader:
        
        if counter<1:
            counter+=1
        elif counter==1:
            name_min = row[0]
            velocities_min = int(row[1])
            name_max = row[0]
            velocities_max = int(row[1])
            counter+=1
            
        else :
            if int(row[1]) < velocities_min:
                name_min = row[0]
                velocities_min = int(row[1])
                
            elif int(row[1]) > velocities_max:
                name_max = row[0]
                velocities_max = int(row[1])
                
    print(f"Galaxy {name_min} has the min velocity of {velocities_min}km/sec.")
    print(f"Galaxy {name_max} has the max velocity of {velocities_max}km/sec.")