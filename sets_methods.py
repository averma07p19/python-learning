s1 = {1, 2, 5, 10, "ankur", "rishan"}
s2 = {35, 5, 5, 11, "pallavi"}

my_set1 = s1.union(s2)
print(my_set1)

s1.add("amma")
s2.add("babba")

my_set2 = s1.union(s2)
print(my_set2)

s3 ={"ankur", "rishan"}
print(s3.issubset(s1))