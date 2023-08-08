cars = ['audi', 'bmw','subaru','toyota']

for car in cars:
    if car.lower()=='bmw':
        print(car.upper())
    else:
        print(car.title())

#Need to remember diferance between "=" and "=="
# = - it is operator
# == - check the equealents

answer_1 =17;
answer_2 =20;
answer_3 =22;

correct_answer=19;

print(correct_answer == answer_1) #False
print(correct_answer == 2) #False
print(correct_answer <= 19) #True

#For use several coditions, we can use operators "or" or "and", for example

if (answer_1 == 17 and answer_2 == 20):
    print("true")
else:
    print("false ")


#How we can chack existence inside tre massive ? We can use "not in", for example
users = ["Nikita", "John","James","Dilinger"]
user = "Nikita"
user_list_1 =users[:]

user_list_1.append("hhh")

if user not in users:
    print(f"{user} not exist")
else:
    print(f"{user} exist")
#Let's try to use for with if
#In this examle we check diference between "user_list_1" and "users"
for user in user_list_1:
    if user not in users:
        print(f"{user}, you are not exist")

user = "Nikita"


if user == "Nikittt":
    print("first")
elif user == "Nikita":
    print("Second error")
else:
    print("No Conditions")
