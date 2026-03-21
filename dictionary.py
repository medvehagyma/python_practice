person1 = {"name" : "Jolán", "age" : 45}
print(person1["name"])
print(person1["age"])

person2 = {"name" : "Ödönke", "age" : 4, "favouriteSubjects" : ["statistics", "sociology", "social anthropology"]}
print(person2["name"])
print(person2["age"])
print(person2["favouriteSubjects"][2])

person3 = {"name" : "Elvira", "age" : 65}

persons = [person1, person2]

persons.append(person3)

for person in persons :
    print(person["name"])


# TO DO:
# Print the names of all the persons wo are above 30 years of age.
# The output should be in the following format: <name> is above 30.

for person in persons :
    if person["age"] > 30 :
        print(person["name"] +" is above 30.")



    