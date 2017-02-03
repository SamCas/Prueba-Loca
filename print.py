# Print Formatting.
s = 'Im here!'
print('Place my Variable here: %s' %(s))

# Float
print("Float numer: %1.2f" %(13.145)) # 1.2f Second number is the number of decimals after de point.
# The first number is the total minimum number of digits th string should contain.
print("Float numer: %1.5f" %(13.145))
print("Float numer: %10.2f" %(13.145)) # Is the number isn't that big, it fills with white spaces.

# Convertion Format.
print("Conver to string: %s" %(123))
# Or
print("Conver to string: %s" %(123))

# Prnting multiple variables.
print("First: %s, Second: %s, Third: %s" %('hi', 'two', 3))

# Proper string formatting using format() function.
print("First: {x} Second: {y} Third: {x}".format(x='inserted',y='Two!'))
