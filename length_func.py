"""Different string functions in python
1. len() - gives you length of string
2. str.capitalize() - coverst first letter of string to block
3. str.upper() - coverts whole string to upper case
4. str.lower() - coverts whole string to lower case
5. str.title() - coverts every first letter all syllabals in string to upper case
6. str.split(separator) - split all the syllabals of the strings
7. str.strip() - eliminate the leading and trailing spaces of the string
8. str.replace("old,"new") - replace occurances to new word in the string, you can do replace chaing as well for different occurance like
                                replace("old","new").replace(old1,new1)
9. str.join(iretable) - joins different words to make a string
10. str.find(sub_str) - gives first lowest index of that occurance in the string otherwise -1
11. str.count(sub_str) - gives count of non-overlapping occurances in the string
12. str.starswith('prifix') - returns boolean after checking prefix of the string (case sensitive)
13. str.endswith('suffix') - returns boolean after checking suffix in the string (case sensitive)
14. str.isdigit() - checks if string is purely numbers and returns boolean
15. str.isalpha() - checks if all are letters in the string and returns boolean"""

mystr = "my name is ankur verma and i live in ghaziabad"

print(f"length of mystr is : {len(mystr)}")
print("capitalized mystr is :", mystr.capitalize())
print("upper cased mystr is :", mystr.upper())
print("lower cased mystr is :", mystr.lower())
print("Titled mystr is :", mystr.title())
print("splitted mystr is :", mystr.split(" "))
# print("Name in mystr :", mystr.split(" ").[3:4])


