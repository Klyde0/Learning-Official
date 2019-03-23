monthconversions = {
'Jan': "January" ,
'Feb': 'February' ,
'Mar': 'March' ,}

print(monthconversions.get('an', 'Not a valid key'))

# sometimes we want to use the .get function when we want to know if there is a default value
# if the given key doesnt have a value in the dictionary

# Keys dont have to be strings, they can be int, booleans