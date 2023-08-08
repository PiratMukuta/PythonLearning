names =["Vika","Alice","John","James"]
for name in names:
    print(F"You are grete, {name}")
#Result:
#You are grete, Vika
#You are grete, Alice
#You are grete, John
#You are grete, James


#We can use range() for generate list of numbers in increment otder
for number in range(1,6):
    print(number)

#How to create list with range() function

numbers =list(range(0,10))
print(numbers)

numbers = []
for number in range(1,9):
    numbers.append(number*2)

print(numbers[-1])
print(numbers)


#Slices
print(numbers[1:3])
print(numbers[:3])
print(numbers[-3:]) #last 3 symbvols
print(numbers[:-3]) #all wihout last 3 symbvols


#How to copy slices we can use :