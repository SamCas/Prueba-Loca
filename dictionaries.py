my_dict = {'key1':'value','key2':'value2'}
print(my_dict['key1'])

# Dictionaries can store multiple values
my_dict = {'k1':123,'k2':2.34,'k3':'string'}
print(my_dict['k2'])

# Methods.
print(my_dict['k3'][::-1].upper())

my_dict2 = {'k1':123}
print(my_dict2)
my_dict2['k1'] += 100
print(my_dict2)

# Working with empty dictionaries.
d = {}
d['animal'] = 'Dog'
d['number'] = 123
print(d)

# Nesting with dictionaries.
d = {'k1':{'nestkey':{'subnestkey':'string'}}}
print(d['k1']['nestkey']['subnestkey'].upper())

# More Methods.
d = {}
d['k1'] = 1
d['k2'] = 2
d['k3'] = 3
