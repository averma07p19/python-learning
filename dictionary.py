family_members = {
    "papa" : "Vinesh Verma",
    "mummy" : "Manju Verma",
    "spouse" : "Pallavi Verma",
    "children" : "Rishan Verma",
    "whoami" : "Ankur Vermr",
    "everyone" : ["Me", "my Parents", "my wife", "and my kid"]
}

# print(family_members, type(family_members))
# print(family_members["papa"])

msg = f"""
    My name is {family_members["whoami"]} and I love every one in my family.
    We are total 5 members here, my parents are {family_members["papa"]} and {family_members["mummy"]}.
    My loving wife is {family_members["spouse"]} who takes care of everyone and everything at home.
    And our heart, our kid {family_members["children"]} is the cutest and lovable to everyone in my family.
    {family_members["everyone"]} are the Vermas 
    """

# print(msg)

# print(family_members.items())
# print(family_members.keys())
# print(family_members.values())

# update any pair
# family_members.update({"papa" : "Shri Vinesh Verma", "mummy" : "Shri Manju Verma"})
# print(family_members)

family_members.update({"sister": "Shilpi Verma"})

#get method
"""with get method you dont get any error if there is no key value pair in the dictionary, 
with print(family_members["brother"]) it will throw
error"""
# print(family_members.get("papa")) #key value exists
# print(family_members.get("brother"))  #key value doesnt exist but gives no error instead gives none
# print(family_members["brother"]) #will throw an error

# print(family_members.get("brother", "You had a brother bitch but now he dont recognise you as his brother, so move on mother fucker"))

#pop method
#it removes the key from dictionary and gives you its value as result
# family_members.update({"brother": "Ankit Verma"})
print(family_members.items())
# print(family_members.pop("brother"))
# print(family_members.items())
# print(family_members.pop("brother", "You had a brother bitch but now he dont recognise you as his brother, so move on mother fucker"))


