"""
hellofriend.py
Author: Ed Dennison
Credit: 

Assignment:

Write and submit an interactive Python program that asks for the user's name and age, 
then prints how much older Python is than the user (based on a simple comparison of 
birth year). Python's first public release occurred in 1991. Something like this:

Please tell me your name: Guido
Please tell me your age: 16
Hello, Guido. Python is 8 years older than you are!

Note that the text: "Guido" and "16" are entered by the user running the program. 
The final line ("Hello...") is generated dynamically when you run the program, based 
on the name and age that the user enters.
"""
from datetime import datetime

nom = input("Comment appelez-vous?")
age = input("Quel age est vous?")
ageint = int(age)

pythonage = datetime.now().year - 1991
print(pythonage)
print(ageint)f
if (pythonage > ageint):
    print (pythonage - ageint , "years older than python.")
if (pythonage < ageint) :
    print (ageint-pythonage , "years younger than python.")
if (ageint == pythonage):
    agestr = "the same age as python."

print(agestr)

# print ("Allo ", nom , ". Vous etes ", agestr)

