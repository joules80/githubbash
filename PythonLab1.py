# creatin a string
myString = "This is a string."
print(myString)

# use the function type() to print out the class type
print(type(myString))
print(myString + " It is of the data type " + str(type(myString)))

# combine string to form words
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# using input() to read data from user. you can also use raw_input()
#!!!Attention raw_input() don't work on python3 and it read only string varible
name = input("What is your name? ")
print(name)
age= input("How old are you?")
print(age)

# exple of using print() with multiple variable. answer the question to let python go forward
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you are {} and you like a {} {}!".format(name,age,color,animal))
