# Dictionary :
# 
# Dynamic in structure --> one can add new key - value pairs to a dictionary always

# alien_0 [a collection of key value pairs] [use s key to acess a value]

alien_0 = {'color' : 'green', 'points' : 5}


# name of dictionary then place a key inside s square bracket

print(alien_0['color']) # It returns the value associated with the key value color:

print(alien_0['points'])

# retrieving the points

new_points = alien_0['points']

print(f"The points earned are {new_points}")


# aDDING NEW KEY VALUE

alien_0['X_position'] = 0

alien_0['Y_position'] = 25

print(alien_0)



#key value\
    
vehicles = {'body': 'brown', 'speed_max': '200km/hr'}

# retrieve

print(vehicles['speed_max'])



# add

vehicles['price'] = 'One Million'

print(vehicles)


new_key = vehicles['price']

print(f"the price of the car is {new_key}")

#####################################################

# starting with an empty dictionary

cows = {}

cows['color'] = 'black and white'

cows['type'] = 'freshaian'

print(cows)

#modifying values in a dictionary:

tiger = {"country": "siberia"}

print(f"The tiger is from {tiger['country']}")

tiger = {"country": "Kenya"}

print(f"the tiger is now from {tiger['country']}")



 # Alien's current speed

alien_0 = {'X_position': 0, 'Y_position': 25, 'speed':'fast'}

print(f"original position: {alien_0['X_position']}")

if alien_0['speed'] == 'slow':
    
    x_increment = 1
    
elif alien_0['speed'] == 'medium':
    
    x_increment = 2
    
else:
    
    x_increment = 3
    
#The new position is old plus new position

alien_0['X_position'] = alien_0['X_position'] + x_increment


print(f"new position: {alien_0['X_position']}")

#####################################################################

alien_0 = {'color': 'green', 'points': 5}

print(alien_0)

del alien_0['points'] # Used to delete a key from a dictionary

print(alien_0)


# A dictionary of similar objects.

# For instance you want to poll a number of people and ask them their best programming language.

favorite_languages = {
    
    'jen':'python',
    
    'sarah':'C',
    
    'Edward':'Rust',
    
    'Phil':'Python'
}

language = favorite_languages['sarah']

print(f"Sarah's favourite language is {language}")





# Using get() to access values

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned')

print(point_value)