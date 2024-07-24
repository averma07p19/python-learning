import random

def hiscore_write(score):
     with open("random-game-hiscore.txt", "w") as f:
          f.write(str(score))
          return


def game():
    score = random.randint(1,100)
    with open("random-game-hiscore.txt") as f:
        hiscore = f.read()
    if (hiscore == ""):
        hiscore = 0
        print(f"Your score is {score} and hiscore is {hiscore}, You WON!")
        hiscore_write(score)
    elif (score>int(hiscore)):
        print(f"Your score is {score} and hiscore is {hiscore}, You WON!")
        hiscore_write(score)
    else:
        print(f'Your score is {score} and hiscore is {hiscore}, you LOSE! ')
    return score

a = game()

print(a)