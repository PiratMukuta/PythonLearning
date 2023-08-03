# Page 20

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