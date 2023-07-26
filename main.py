#!/usr/bin/env python3
print("Hello")
pet = ""
age = int(input("How old are you?  "))
if age > 30:
  print("Your ideal pet is a cat.")
elif age < 30 and age > 14:
  Q_Pet = input("What is your ideal pet?  ")
  pet = Q_Pet
  print(f"Your ideal pet is a {pet}")
else:
  pet = "fish" 
  print(f"The pet for you is a {pet}")

