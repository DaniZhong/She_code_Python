import csv
import os
import sys
#Q1
groceries = {"Baby Spinach": 2.78,"Hot Chocolate": 3.70,"Crackers": 2.10,"Bacon": 9.00,"Carrots": 0.56,"Oranges": 3.08}

quantity1 = {"Baby Spinach": 1,"Hot Chocolate": 3,"Crackers": 2,"Bacon": 1,"Carrots": 4,"Oranges": 2}
for item_name, item_price in groceries.items():
    total = "{:.2f}".format(item_price*quantity1[item_name])                            
    print(f"{quantity1[item_name]} {item_name} @ ${groceries[item_name]} = ${total}")

quantity2 = {"Baby Spinach": 2,"Hot Chocolate": 1,"Crackers": 4,"Bacon": 0,"Carrots": 8,"Oranges": 5}
for item_name, item_price in groceries.items(): 
    total = "{:.2f}".format(item_price*quantity2[item_name])
    print(f"{quantity2[item_name]} {item_name} @ ${groceries[item_name]} = ${total}")

#Q2
colour_counts = {"blue": 0,"green": 0,"yellow": 0,"red": 0,"purple": 0,"orange": 0,}

colours1 = ["purple","red","yellow","blue","purple","orange","blue","purple","orange","green"]

for item in colours1:
    colour_counts[item]+=1

for item_name, item_no in colour_counts.items():
    print(f"{item_name}: {item_no}")

colour_counts = {"blue": 0,"green": 0,"yellow": 0,"red": 0,"purple": 0,"orange": 0,}

colours2 = ["orange","purple","blue","yellow","green","green","purple","purple","green","blue","green","orange","purple","blue","green","orange","orange","red","yellow","yellow"]
for item in colours2:
    colour_counts[item]+=1

for item_name, item_no in colour_counts.items():
    print(f"{item_name}: {item_no}")

# #Q3
names1 = ["Maddy", "Bel", "Elnaz", "Gia", "Izzy","Joy", "Katie", "Maddie", "Tash", "Nic","Rachael", "Bec", "Bec", "Tabitha", "Teagen","Viv", "Anna", "Catherine", "Catherine", "Debby","Gab", "Megan", "Michelle", "Nic", "Roxy","Samara", "Sasha", "Sophie", "Teagen", "Viv"]
name_counts = {}
for key in names1:
    name_counts[key]=0
for key in names1:
    name_counts[key]+=1
for item_key, item_no in name_counts.items():
    print(f"{item_key} {item_no}")

names2 = ["Miranda", "Sophie", "Emily", "Taylor", "Anne","Djuarli", "Anika", "Rosie", "Miranda", "Taylor","Abby", "Sarah", "Teagen", "Abby", "Abby","Maddie", "Miranda", "Rosie"]
name_counts = {}
for key in names2:
    name_counts[key]=0
for key in names2:
    name_counts[key]+=1
for item_key, item_no in name_counts.items():
    print(f"{item_key} {item_no}")

#Q4
import csv
import os
import sys
colors_name = {}
with open(os.path.join(sys.path[0], "colours_20_simple.csv")) as csv_file:
    reader=csv.reader(csv_file)
    for row in reader:
        colors_name[row[1]] = row[2]   
for hex, english_names in colors_name.items():
    print(f"{hex}: {english_names}")

#Q5
import csv
import os
import sys
colors_name = {}
with open(os.path.join(sys.path[0], "colours_20_simple.csv")) as csv_file:
    reader=csv.reader(csv_file)
    for row in reader:
        colors_name[row[1]] = [row[0],row[2]]  
for hex, RGB_english_name in colors_name.items():
    print(f"{hex}: {RGB_english_name}")


