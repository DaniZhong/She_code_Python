#Q1
foods = ["orange","apple","banana","strawberry","grape","blueberry",["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]
print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[6][-1])

#Q2
mailing_list = [["Chilli", "chilli@thechihuahua.com"],["Roary", "roary@moth.catchers"],["Remus", "remus@kapers.dog"],["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],["Ivy", "noreply@goldendreamers.xyz"],]
print(mailing_list[0][0],": ",mailing_list[0][1])
print(mailing_list[1][0],": ",mailing_list[1][1])
print(mailing_list[2][0],": ",mailing_list[2][1])
print(mailing_list[3][0],": ",mailing_list[3][1])
print(mailing_list[4][0],": ",mailing_list[4][1])

#Q3
name1 = input("Please enter the first name.")
print(f"Enter a name: {name1}")
name2 = input("Please enter the second name.")
print(f"Enter a name: {name2}")
name3 = input("Please enter the third name.")
print(f"Enter a name: {name3}")
name_entered=[name1,name2,name3]
print(name_entered)

#Q4
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []
d=[a,b,c]
print(d)
e=[a[0],a[1],a[2],b[0],b[1],b[2],c[0],c[1],c[2]]
print(e)

