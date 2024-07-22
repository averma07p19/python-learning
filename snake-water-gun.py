import random

comp = random.choice([1,-1,0])
you = input("Enter your move :\n")
dict = {
    's' : 1,
    'w' : -1,
    'g' : 0
}
revdict = {
    1 : "Snake",
    -1 : "Water",
    0 : "Gun"
}

# print(f"Computer choice is : {revdict[comp]}")
younum = dict[you]
print(f"you chose {revdict[younum]} and Computer chose {revdict[comp]}")



