# # This program checks if a student is eligible to sit in an exam based on their attendance.
# Total_classes = int(input("Enter the total number of classes held: "))
# Your_attendance = int(input("Enter the number of classes you attended: "))
# Attendence= (Your_attendance / Total_classes) * 100
# if Attendence >= 75:
#     print("You are eligible to sit in the exam.")
# else:
#     print("You are not eligible to sit in the exam.")
#     print("You need to attend at least 75% of the classes.")





# # If the passenger is a senior citizen (age > 60), give 40% discount. Else,full fare.
# Fare_Amount = float(input("Enter the fare amount: "))
# if Fare_Amount < 0:
#     print("Fare amount cannot be negative. Please enter a valid amount.")
#     Fare_Amount = float(input("Enter the fare amount: "))
# elif Fare_Amount == 0:
#     print("Fare amount cannot be zero. Please enter a valid amount.")
#     Fare_Amount = float(input("Enter the fare amount: "))
# print("The fare amount is:", Fare_Amount)
# age = int(input("Enter your age: "))
# if age > 60:
#     discount = 0.4 * Fare_Amount
#     Fare_Amount -= discount
#     print("You are a senior citizen, you get a 40% discount.")
#     print("The final fare amount is:", Fare_Amount)
# else:
#     print("The final fare amount is:", Fare_Amount)





#If age < 12, ticket = ₹100; if age >= 12 and < 60, ticket = ₹200; else ticket = ₹150.
# age = int(input("Enter your age: "))
# if age < 12:
#     ticket_price = 100
#     print("Your ticket price is ₹100.")
# elif age >= 12 and age < 60:
#     ticket_price = 200
#     print("Your ticket price is ₹200.")
# else:
#     ticket_price = 150
#     print("Your ticket price is ₹150.")




# If total order > ₹500, delivery is free. Else, add ₹50 delivery charge.
# total_order = float(input("Enter the total order amount: "))
# if total_order > 500:
#     print("Your total order amount is ₹", total_order, ". Delivery is free.")
# else:
#     delivery_charge = 50
#     total_order += delivery_charge
#     print("Your total order amount is ₹", total_order, ". A delivery charge of ₹50 has been added.")




#A student passes if the marks are 33 or more out of 100. Otherwise, the student fails.
# marks = int(input("Enter your marks (out of 100): "))
# if marks >= 33:
#     print("Congratulations! You have passed.")
# else:
#     print("Sorry, you have failed. You need at least 33 marks to pass.")




#If tank level is below 25%, print "Refill the water tank". Else, print "Sufficient water".
# tank_level = float(input("Enter the water tank level: "))
# if tank_level < 25:
#     print("Refill the water tank.")
# else:
#     print("Sufficient water in the tank.")




#If the signal is red, stop. If yellow, get ready. If green, go.
# signal = input("Enter the traffic signal color (red, yellow, green): ").lower()
# if signal not in ["red", "yellow", "green"]:
#     print("Invalid signal color. Please enter red, yellow, or green.")
# else:
#     print("You entered a valid signal color.")
# if signal == "red":
#     print("Stop.")
# elif signal == "yellow":
#     print("Get ready.")
# elif signal == "green":
#     print("Go.")




# If entered amount <= balance, print "Transaction Successful". Else, print "Insufficient Balance".
# balance = float(input("Enter your current balance: "))
# amount = float(input("Enter the amount to withdraw: "))
# if amount <= balance:
#     print("Transaction Successful. Your new balance is ₹", balance - amount)
# else:
#     print("Insufficient Balance. Your current balance is ₹", balance)



# If temperature > 40°C, print "Too hot". Else, print "Temperature is normal".
# temperature = float(input("Enter the temperature in °C: "))
# if temperature > 40:
#     print("Too hot.")
# else:
#     print("Temperature is normal.")



# If battery is less than 20%, show "Low Battery". Else, show "Battery OK".
# battery = float(input("Enter the battery percentage: "))
# if battery < 20:
#     print("Low Battery.")
# else:
#     print("Battery OK.")



# If rooms are available, confirm booking. Else, show "No rooms available".
# available_rooms = input("Are rooms available? (yes/no): ").strip().lower()
# if available_rooms not in ["yes", "no"]:
#     print("Invalid input. Please enter 'yes' or 'no'.")
#     available_rooms = input("Are rooms available? (yes/no): ").strip().lower()
# if available_rooms == "yes":
#     print("Booking confirmed.")
# else:
#     available_rooms == "no"
#     print("No rooms available.")



# If BMI < 18.5: "Underweight", 18.5–24.9: "Healthy", 25–29.9: "Overweight", else "Obese
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print("Underweight")
# elif 18.5 <= bmi < 25:
#     print("Healthy")
# elif 25 <= bmi < 30:
#     print("Overweight")
# else:
#     print("Obese")

# Even or Odd! write a program that check if a number entered by user is even or odd
# num=int(input("Enter a number to check it is even or odd: "))
# if num%2==0:
#     print("The number is Even")
# else:
#     print("The number is Odd")



# Ask the user to enter a number and check if it is positive, negative, or Zero
# num=float(input("Enter a number to check it is positive, negative, or Zero: "))
# if num>0:
#     print("The number is positive")
# elif num==0:
#     print("The number is Zero")
# else:
#     print("The number is Negative")




# Take two numbers as input and print the larger one
# num1=float(input("Enter first number: "))
# num2=float(input("Enter second number: "))
# if num1 < num2:
#     print(num2 ,"is Larger than",num1)
# elif num1 > num2:
#     print(num1, "is Larger than",num2)
# else:
#     print(num1 ,"is equal to", num2)




# Ask the user a number and check if it is divisible by 5 or not
# num=float(input("Enter a number to check it is divisible by 5 or not: "))
# if num%5==0:
#     print("The number is divisible by 5")
# else:
#     print("The number is not divisible by 5")




# Grade calculator
# marks=float(input("Enter your marks: "))
# if marks>=90:
#     print("Congratulations you have passed with A grade!!")
# elif marks<=90 and marks>=80:
#     print("Congratulations you have passed with B grade!!")
# elif marks<=80 and marks>=70:
#     print("Congratulations you have passed with c grade!!")
# elif  marks<70:
#     print("You are Failed!!")




# Ask a user to enter a password and verify if it is matches a predefined password
# import os
# Pass1=input("Enter your Password: ")
# os.system('cls' if os.name == 'nt' else 'clear')
# Pass2=input("verify your Password: ")
# if Pass1==Pass2:
#     print("You Entered the correct password!!")
# else:
#     print("Password is incorrect!!")




# Age Eligible for voting or not
# Age=int(input("Enter Your Age: "))
# if Age > 18:
#     print("You are eligible for vote")
# else:
#     print("You are not eligible for vote!!")




# leap year checker
# import calendar
# y = int(input("Enter a valid year: "))
# if calendar.isleap(y):
#     print("Leap year")
# else:
#     print("Not a leap year")




# vowel or consonant
# char = input("Enter a single character: ").lower()
# if char in 'aeiou':  # Check for vowels
#     print(f"{char} is a vowel.")
# else:  # If not a vowel, it's a consonant
#     print(f"{char} is a consonant.")


# check Triangle is Valid or Not
# a = int(input('Please Enter the first side of a Triangle: '))
# b = int(input('Please Enter the Second side of a Triangle: '))
# c = int(input('Please Enter the Third side of a Triangle: '))
# if a + b > c and a + c > b and b + c > a:
#     print("\nThis is a Valid Triangle")
# else:
#     print("\nThis is an Invalid Triangle")