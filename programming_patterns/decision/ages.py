import sys

# print("Hello! The first commandline argument is: " + sys.argv[0])
# print("Hello! The second commandline argument is: " + sys.argv[1])

# inputs
defaultPersons = [
        {"name": "Falesz", "age": 29}, 
        {"name": "Encsi", "age": 26}, 
        {"name": "Virág", "age": 27}, 
        {"name": "Anna", "age": 39}
]
persons = []

if len(sys.argv) >= 2:
    if sys.argv[1] == "keyboard":
        num_of_persons = int(input("Please enter the number of persons: ")) # we get the count of people from the keyboard and convert it to an integer type
        for i in range(0, num_of_persons): # we want to do the following num_of_persons times, once for each distinct person
            current_person = {} # we create an empty dictionary object for the current person
            current_person["name"] = input(f"Enter the name of the {i + 1}th person: ") # to the "name" key we map the value that we get from the keyboard
            current_person["age"] = int(input(f"Enter the age of the {i + 1}th person: ")) # to the "age" key we map the value that we get from the keyboard after converting it to an integer type 
            persons.append(current_person) # we add the person that we just "built" to the persons list, which the algorithm will process
    else: # reading from files with given filename
        with open("data/"+sys.argv[1], "r", encoding="utf-8") as infile:
            for line in infile:
              # print(line, end="")
                dataChunks = line.split(";") # strings' lists
                current_person = {}
                current_person["name"] = dataChunks[0]
                current_person["age"] = int(dataChunks[1])
                persons.append(current_person)
else:
    persons = defaultPersons


# algorithm


def olderThan28 (persons) :
    exists = False

    for i in range (0, len(persons)) :
        if persons[i]["age"] > 28 :
            exists = True

    return exists


# outputs

print(olderThan28(persons))