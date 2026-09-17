# write your code here
import random

numbers_peoples = int(input("Enter the number of friends joining (including you):\n"))
peoples = {}

# check numbers of people. add people in dict
if numbers_peoples <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")

    for _ in range(numbers_peoples):
        peoples[input()] = 0
    total_bill = int(input("Enter the total bill value:\n"))
    lucky_one = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n").lower()

    lucky_name = ''

    if lucky_one == "yes":
        numbers_peoples -= 1
        lucky_name = random.choice(list(peoples.keys()))
        print(f"{lucky_name} is the lucky one!")
    else:
        print("No one is going to be lucky")

    personal_bill = round(total_bill / numbers_peoples, 2)

    for name in peoples:
        if name == lucky_name:
            continue
        peoples[name] = personal_bill

    print(peoples)
