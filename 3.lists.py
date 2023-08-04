#page 35-51
#For use List we should write [], like that:

names = ["John","Nikita","Oleg"]
print(names[0])
print(names[1])
print(names)

print(names[0].title())


#To get last element of list we need to use -1
print(names[-1])

hello_msg= f"Hello, {names[1]}"
print(hello_msg)

#All lists is dinamic, base on that we can change elements
names[0] = "Katrin"
print(names)

#We can use append()
names.append("Ksenia") # Appenr for adding new elements
print(names)

#To insert ellement inside arrau we can use insert()
names.insert(0,"Vika") #To inser inside the array
print(names)


#For delate elements from array we can use del
del names[4] #del is not method, it is instructions
print(names)

#If i want to delate by veluse i can use remove()
names.remove("Oleg")
print(names)

#Sorting of lists by alphab
names.insert(3,"Alph")
names.sort()
print(names)


#For sort in ise


size = len(names)
print(size)

#Sort in inverce
names.reverse()
print(names)