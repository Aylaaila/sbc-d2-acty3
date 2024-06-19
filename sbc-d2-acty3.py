import random

print("Bet Number")

first = int(input("first number: "))
second = int(input("second number: "))
third = int(input("third number: "))

Lfnum = random.randint(4, 6)
Lsnum = random.randint(4, 5)
Ltnum = random.randint(5, 6)

mylist = first,second,third
lotolist = Lfnum,Lsnum,Ltnum

print(f"your number are: ",mylist)
print("Result:",lotolist)


if first == Lfnum and second == Lsnum and third == Ltnum:
    print("Wow")
elif (
    first in {Lfnum, Lsnum, Ltnum} and
    second in {Lfnum, Lsnum, Ltnum} and
    third in {Lfnum, Lsnum, Ltnum} and
    len({first, second, third}) == 6 
):
    print("you win")
else:
    print("thank you next")