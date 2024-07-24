"""to open and read a txt file and print the content"""
# f = open("datafile.txt") #open a file using this function
# text = f.read() #read the file 
# f.close() #close the file
# print(text, type(text), len(text)) #print the specific content

"""to open a text file and write some content into it"""
# str = "Lets do some other real exercise, we have to become proficient in this to secure a worthy job"
# str ="look for a method to amend text instead of rewrite the file"
# str = "\nI think we got the solution for appending, we will use 'a' when opening the file"
# f = open("datafile.txt", "a")
# f.write(str)
# f.close()
# g = open("datafile.txt")
# text = g.read()
# print(text)

"""differet methods to open a file which depends on the operation you will make after that
    "r" : is for reading only, which is a default setting so no need to explictly give in the statement
    "w" : is for writing, which will truncate the file and then write whatever string/input you are giving
    "a" : is for appending, which will open the file and append the input into it"""

"""WITH statement to read and close the file without giving close() comamnd at the end"""
str = "So using WITH statement we dont need to give close() command at the end but it will automatically close"
with open("datafile.txt") as f:
    print(f.read())
# with open("datafile.txt", "w") as g:
#     f.write(str)
# with open("datafile.txt") as h:
#     print(h.read())
    # f.write(str)
    # print(f.read,"a")
    # f.write(str)
    # print(f.read())


    