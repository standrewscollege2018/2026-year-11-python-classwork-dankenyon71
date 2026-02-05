'''This program demonstrates print(), data types, variable, inputs and f-string'''
import time
import sys

#print() is a function that outputs whatever is inside the brackets
#numbers don't need speech marks
print(1)
print(1.5)

#words need speech marks which make it a string
input("You know what's crazy? ")
print("The low taper fade meme is still MASSIVE")

#there are lots of data types
#integers, floating point numbers (floats), text (string), boolean (T/F)

#We use variables to store information
time.sleep(2)
name = "Ilana"
first_name="Max"
last_name="Nuthall"
age=15

#you can include variables in print() statements

print(first_name)
time.sleep(0.5)

#to combine variables with a string we use f-strings
#The variable goes inside curly brackets

print(f"My name is {first_name} {last_name} and my girlfriends name is {name} and we are {age} years old")
time.sleep(0.5)
username = input("What is your name? ")
time.sleep(0.5)
print(f"{first_name} {last_name}: Hi {username}")
time.sleep(0.5)

print(f"Took {time.process_time()} seconds to run.")
time.sleep(0.5)
sys.exit()