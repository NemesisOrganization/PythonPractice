#first_name = input("Please enter your first name:")
#age = int(input("Your age:"))
#age = age + 1  
#print(f"Hello {first_name}")
#print(f"your age is{age}")

#rectangle practice
#length = int(input("Enter Length: "))
#width = int(input("Enter Width: "))
#area = length * width
#print(area)

#arithmetic
#friends = 50
#friends += 1
#friends -= 1
#friends *= 2 
#friends /= 2
#friends ** 2
#remainder = friends % 3

#x = 3.14
#y = -4
#z = 5
#result = round(x)
#result = abs(y)
#result = pow(4,3)
#result = max (x,y,z) 
#result = min (x,y,z) 
#print (result)

import math
#circumference of a circle
#pi = math.pi
#radius = 10.5
#circumference = 2 * pi * radius 
#print(math.e)
#result = math.sqrt(x)
#result = math.ceil(x)
#result = math.floor(x)
#print (round(circumference, 2))

#area of a circle
#radius = float(input("Enter radius: "))
#area = math.pi * pow(radius,2)
#print(round(area, 2))

#hypothenus of a triangle
#a = int(input("Enter value of a"))
#b = int(input("Enter value of b"))
#c = math.sqrt(pow(a,2)+pow(b,2))
#print(f"The Hypothenus is {c}")  

#If Else
#age = int(input("Enter your age: "))

#if age >= 18:
    #print("You are now signed up")
#else:
    #print("You need to be 18 above to sign up")
    
#num1 = float(input("Enter 1st number: "))
#operation = input("Enter operation")
#num2 = float(input("Enter 2nd number: "))


#if operation == "+":
    #print(math.floor(num1 + num2))
#elif operation == "-":
    #print(math.floor(num1 - num2))
#elif operation == "*":
    #print(math.floor(num1 * num2))
#elif operation == "/":
    #print(math.floor(num1 / num2))
#else:
    #print("Wrong Format")
    

#Unit conversion program 
#unit = input("Celsius or Fahrenheit (C/F): ")
#temp = float(input("Enter temperature: "))

#if unit == "C":
    #fahrenheit = (9 * temp)/5 + 32
    #print(f"The Celsius {temp} is {fahrenheit} in Fahrenheit")
#elif unit == "F":
    #celsius = ((temp - 32) * 5) / 9
    #print(f"The Fahrenheit {temp} is {celsius} in Celsius")
#else:
    # print("Invalid Temperature Measurement")
        
#Conditonal Expression
#num = 6
#result = "Even" if num% 3 == 0 else "Odd"
#print(result)

#String methods
#Validate user input Exercise
#userName = input("Enter your desired username: ")
#print(len(userName))
#if len(userName) > 12:
    #print("Username must not be greater than 12 Characters!")
#elif not userName.find(" ") == -1:
    #print("Username can't contain spaces")
#elif not userName.isalpha():
#    print("Username can't contain numbers")
#else:
#    print(f"You are signed up {userName}")


#String Indexing 
#credit_number = "1234-5678-9012-3456"
#to reverse the string you need to reverse the step to -1
#[start:end:step]
#last_digits = credit_number[15:]
#print(last_digits)

#While Loop
#name = input("Enter your Name: ")
#age = int(input("Enter your age"))

#while name == "":
#    print("You did not enter your name")
#    name = input("Enter your Name: ")
#print(f"Hello {name}")

#Compound Interest Calculator
principle = 0 
rate = 0
time = 0

#while principle <= 0:
#    principle = float(input("Enter the principle: "))
#    if principle <= 0:
#        print("Principle cannot be less than or equal to zero")
        
#while rate <= 0:
#    rate = float(input("Enter the rate: "))
#    if rate <= 0:
#        print("Rate cannot be less than or equal to zero")
        
#while time <= 0:
#    time = int(input("Enter the time: "))
#    if time <= 0:
#        print("Time cannot be less than or equal to zero")

#you can use break for allowing 0
#while True:
#    principle = float(input("Enter the principle: "))
#    if principle < 0:
#        print("Principle cannot be less than or equal to zero")
#    else:
#        break
        
#while True:
#    rate = float(input("Enter the rate: "))
#    if rate < 0:
#        print("Rate cannot be less than or equal to zero")
#    else:
#        break
        
#while True:
#    time = int(input("Enter the time: "))
#    if time < 0:
#        print("Time cannot be less than or equal to zero")
#    else:
#        break
    
#total = principle * pow((1 + rate / 100),time)
#print(total)


#forloop
#for x in range (1,11):
#    print(x)

#Collection List,Set,Tupple
#List = [] Ordered and changeable,Duplicates allowed
#Set = {} Unordered and immutable/No Duplicates Allowed
#Tuple = () Ordered and unchangeable,Duplicates allowed
#name = "Justin"
#fruits = ["apple", "orange", "banana", "coconut","durian"]
#print(name[::-1])
#for fruit in fruits:
#    print(fruit)  

#print(dir(fruits))
#print(len(fruits))

#fruits = {"apple", "orange", "banana", "coconut","durian"}
#fruits = ("apple", "orange", "banana", "coconut")  


#Shoppin cart exercise 

#foods = []
#prices = []
# total = 0

# while True:
#     food = input("Enter the Food you like(press Q to quit): ")
#     if food == "q":
#         break
#     else:
#         price = float(input("Enter the price of the food: "))
#         foods.append(food)
#         prices.append(price)
#         total = sum(prices)

# print ("---Your Cart---")

# for food in foods:
#     print(food)    
     
# print(f"The total bill is {total}")        


#2d List
# fruits = ["apple", "banana", "orange"]
# vegetables = ["celery", "carrots", "potatoes"]
# meat = ["chicken", "beef", "pork"]

# groceries = [fruits, vegetables, meat]

# for collection in groceries:
#     for food in collection:
#         print(food, end = " ")
#     print()

#Numpad_exercise
# numpad = ((1,2,3),
#           (4,5,6),
#           (7,8,9),
#           ("*",0,"#"))

# for row in numpad:
#     for num in row:
#         print(num, end = " ")
#     print()

#quiz exercise 
# questions = ("What is AG in periodic table?: ",
#              "What is the biggest mammal: ",
#              "What is the hottest planet: ")
# options = (("a.Gold","b.Siver","c.Carbon"),
#            ("a.Whale","b.Ostrich", "c.Rat"),
#            ("a.Mercury","b.Pluto","c.Neptune"))
# right_answers = ("a","a","a")
# answers = []
# guesses = []
# score = 0
# question_num = 0

# # for question in questions:
# #     print("-----------------------------")
# for i in range(len(questions)):
#     print(questions[i])
#     print(options[i])
#     user_answer = input("Enter the letter of your answer: ").lower()
#     answers.append(user_answer)
    
#     if user_answer == right_answers[i]:
#         score += 1

# print("\nYour answers:", answers)
# print("Correct answers:", right_answers)
# print("Your score:", score, "out of", len(questions))


#Dictionaries collection of key value pairs, no duplicate, changeable
#great functions: get, update, pop, clear, keys = will get the key
# values = will get the value of the keys, items = will show 2d in tupples

#Concesion stand exercise

# menu = {"Popcorn":5.00,
#         "Soda": 2.00,
#         "Pizza": 10.00,
#         "Burger": 3.00}
# cart = []
# total = 0 

# print("Please choose your food from the menu: ") 

# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# while True:
#     order = input("Please Enter the food you want to Order: ")
#     if order == "Done":
#         break
#     elif order in menu:
#         cart.append(order)
#         total += menu[order]
#         print(f"{order} added to your cart")
#     else:
#         print("Item not found in the menu")           

# print ("Your cart")
# print ("----------------------")
# print(cart)
# print(f"The total amount: ${total:.2f}")        


#Random Number
# import random   
# options = ("Rock","Paper","Scissor")
# computer_choice = random.choice
# score = 0

# while True:
#     player_choice = input("Choose (Paper, Rock, Scissor), Press q to quit:")
#     computer_choice = random.choice(options)
#     if player_choice == "q":
#         break
#     elif player_choice == "Rock" and computer_choice == "Scissor" or player_choice == "Paper" and computer_choice == "Rock" or player_choice == "Scissor" and computer_choice == "Paper":
#         print(f"Player: {player_choice} vs. Computer: {computer_choice} You Win")
#         score += 1
#     # elif player_choice == "Paper" and computer_choice == "Rock":
#     #     print(f"Player: {player_choice} vs. Computer: {computer_choice} You Win")
#     #     score += 1
#     # elif player_choice == "Scissor" and computer_choice == "Paper":
#     #     print(f"Player: {player_choice} vs. Computer: {computer_choice} You Win")
#     #     score += 1
#     elif player_choice == "Paper" and computer_choice == "Paper" or player_choice == "Rock" and computer_choice == "Rock" or player_choice == "Scissor" and computer_choice == "Scissor" :
#         print(f"Player: {player_choice} vs. Computer: {computer_choice} Tie")
#     # elif player_choice == "Rock" and computer_choice == "Rock":
#     #     print(f"Player: {player_choice} vs. Computer: {computer_choice} Tie")
#     # elif player_choice == "Scissor" and computer_choice == "Scissor":
#     #     print(f"Player: {player_choice} vs. Computer: {computer_choice} Tie")      
#     else:
#         print(f"Player: {player_choice} vs. Computer: {computer_choice} You Lose")
# print(f"Your Score: {score}")    


#Functions
# def happy_birthday(name):
#     print(f"Happy Birthday {name}")

# happy_birthday("Bro")

#return function - statement used to end a function and send a result back to the caller
# def add(x,y):
#     z = x + y
#     return z

# print(add(1,2))



#Default Arguments
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 -discount) * (1 + tax)

print(net_price(500, 0.1, 0))

          
    