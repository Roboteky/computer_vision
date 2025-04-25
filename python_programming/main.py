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