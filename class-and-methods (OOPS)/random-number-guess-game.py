import random

class random_number_game:
    def __init__(self):
        self.ran_num = random.randint(20,30)
        # user_number = int(input("Lets play random number guess, guess no. between 1 to 10 and write below\n"))
        print("Lets play random number guess, guess no. between 20 to 30.")

    def random_number(self):
        # ran_num = random.randint(20,25)
        # print(f"ran_num = {self.ran_num}")
        user_num = int(input("Guess the number and enter :\n"))
        while user_num != self.ran_num:
            if (user_num > self.ran_num + 5):
                user_num = int(input(f"You guessed {user_num} which is too HIGH, guess again :\n"))
            elif (self.ran_num -5 <= user_num <= self.ran_num + 5) and (user_num != self.ran_num):
                user_num = int(input(f"you are close, guess again :\n"))            
            elif user_num < self.ran_num - 5:
                user_num = int(input(f"You guessed {user_num} which is too LOW, guess again :\n"))
        else:
            print(f"Congrats! You guessed the right number this time. {self.ran_num} = {user_num}")
        # return ran_num

user = random_number_game()
user.random_number()
# print(a)
