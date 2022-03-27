programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}
print(programming_dictionary["Bug"])

#to add to a dictionary
programming_dictionary["SHEESH"] = "The sickest thing you can say to someone"
print(programming_dictionary)

#to create empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"] = "A small critter"

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#GRADING_PROGRAM
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)

#Nesting
capitals = {
    "France": "Paris", 
    "Germany": "Berlin"
}

#Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Koln"]
}

#Nesting dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"trains_taken_to": ["Berlin", "Hamburg", "Koln"]}
}

#Nesting Dictionaries inside a list
travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "trains_taken_to": ["Berlin", "Hamburg", "Koln"], 
        "total_cousins": 2
    },
]


#ADDING TO THE LIST
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
