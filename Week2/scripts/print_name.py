def printName(name, age):
    print(f"My name is {name}, I am {age} years old.")
    if age < 13:
        print("I am a pre-teen.")
    elif age > 13 and age < 20:
        print ("I am a teen.")
    else:
        print("I am an adult now.")

printName("Ibrahim", 17)