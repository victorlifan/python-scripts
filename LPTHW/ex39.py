# create dict "states"
states = {
# input keys and associate values
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# crate dict "cities"
cities = {
# input keys and associate values
    'CA': 'San Fancisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add more keys and assoicate values to dict "cities"
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print('-'* 10)
#print out dict "cities", key "NY" associate values
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-'*10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print('-'*10)
# return a list with all the keys and values in "states" dict, then crate a list form it
# assign all the elements in list to valriables "state" and "abbrev"
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviation {abbrev}")

# print every city in state
print('-'*10)
# return a list with all the keys and values in dict "cities" then make a list from it
# assign all the elements in list to variables "abbrev" and "city"
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-'*10)
# return a list with all keys and values in dict "states" then make a list from it
# assign all the elements to variables "state" and "abbrev"
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    # call dict "cities" with keys from dict "states"
    print(f"and has city {cities[abbrev]}")

print('-'*10)
#.get() method return None because key "Texas" doesn't exit in dict "states"
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#.get() method return "Does Not Exit" and assign to city because Key "TX" doesn't exit
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
