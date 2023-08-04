import this
# Page 20-35
#Data 04.08.2023

print("Hi I am Nikita")
print("Hi, I'm Nikita")
print('Hi, "AM" Nikita')

#Function for Title(Capital letter)

name = "nikiTa"
print(name.title())
#In result i get Nikita
print(name.upper())
#In result I get NIKITA
print(name.lower()) # Very useful for data saving(for example in DB)
#In result i get nikita


first_name ="Nikita"
last_name = "Pirat"
full_name =f"{first_name} {last_name}"
print(full_name)
#In Result I get "Nikita Pirat"

#We can use functions inside this type of strings
print(f"Hello, {full_name.upper()} !")
#In result i get Hello, NIKITA PIRAT !

#OR in more Older versions of Python we can use:
message = "{} {}".format(first_name,last_name)
print(message)
#In result i get Nikita Pirat

#Special symbols for arrays
print("\tPython")
#\t - Tab
#\n -New Line

favorite_lang =' python#$%#'
print(favorite_lang.rstrip())

#integer
print(2*2)
print(2**3)
print((2+3)*4)
print(0.2+0.3)
print(0.3*23)
print(2/4)

#For long number we can use _

univerce_age = 14_000_000_000
print(univerce_age)
#python will show 14000000000

x,y,z = 0,0,0;
print(x,y,z)
#in result i get 0 0 0

#for using CONSTANT value should use capital letters because python don't have any build-in velues for const
FIRST_NUMBER = 100
