# Ex. 1 - to create hindi - english dict and ask user to provide input
# word_list = {
#     "dikkat" : "problem",
#     "khushi" : "happiness",
#     "khana" : "food"
# }

# user_input = input("Enter your word of choice : ")


# if word_list.get(user_input):
#     print(word_list.get(user_input))
#     another = input("you wanna see another word : ")
#     if word_list.get(another):
#         print(word_list.get(another))
#     else:
#         another_word = input("cloudnt find this one, you wanna try another word : ")
#         print(word_list.get(another_word))
# else:
#     another_word = input("cloudnt find this one, you wanna try another word : ")
#     print(word_list.get(another_word))

#Ex. 2 - to create a set of 8 numbers given by user and then show all the distinct number
s1 = set()
user_input = str(input("Please provide all the numbers separated by comma (,) and hit enter :\n"))
user_input_list = user_input.split(",")
total_numbers = len(user_input_list)
print(total_numbers, type(total_numbers))
i = 1
while i <= total_numbers:
    s1.add(int(user_input_list[i-1])) 
    i = i+1
print(s1)

