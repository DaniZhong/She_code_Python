#Q1
moths_in_house=input("Pleas reply Yes if there are any moths in the house and No if there aren't any.")

if moths_in_house=="Yes":
    print("Get the moths!")
elif moths_in_house=="No":
    print("No threats detected.")
else:
    print("Please check if there are moths in the house and reply Yes or No, Thank you!")



#Q2
moths_in_house=input("Pleas reply Yes if there are any moths in the house and No if there aren't any.")
mitch_is_home=input("Pleas reply Yes if Mitch is home and No if he isn't.")

if moths_in_house=="Yes" and mitch_is_home=="Yes":
    print("Hoooman! Help me get the moths!")

elif moths_in_house=="No" and mitch_is_home=="Yes":
    print("Climb on Mitch.")

elif moths_in_house=="Yes" and mitch_is_home=="No":
    print("Meooooooooooooow! Hissssss!")

elif moths_in_house=="No" and mitch_is_home=="No":
    print("No threats detected.")

else:
    print("Please check if there are moths in the house and if Mich is home.And reply Yes or No, Thank you!")


#Q3
light_color = "Red"
car_detected = True

if light_color == "Red" and car_detected:
    print("Flash!")
else:
    print("Do nothing.")

#Q4
height=input("Please enter your height in cms.")
if int(height)>=120:
    print('Hoop on!')
else:
    print("Sorry, not today :(")

#Q5
username=input("Please your user name.")
print(f"User name: {username}")
password=input("Pleae enter your password.")
print(f"Password: {password}")
if username=="fleur" and password=="password123":
    print("Correct!")
else:
    print("Incorrect!")

#Q6
email_address=input("Please enter your email address.")
print(f"Email: {email_address}")
if "@" in email_address and "." in email_address:
    print("Valid email address.")
else:
    print("Invalid email address.")


