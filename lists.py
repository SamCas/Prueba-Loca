# Lists.
my_list = [1,2,3]
print(my_list)
my_listTwo = ['lel',12,1.2]

# Print the number of elements on the list.
print(len(my_list))

my_list = ['one','two','three',4,5]
print(my_list[0])
print(my_list[1:])

modify_list = my_list + ['new item']
print(modify_list)

modify_list = my_list*2
print(modify_list)

# Methods for lists.
l = [1,2,3]
l.append('append me!')
print(l)

# Pop grabs the last item on the list.
print(l.pop())
x = l.pop(0)
print(x)

new_list = ['a','b','e','c','d']
new_list.reverse()
print(new_list)
new_list.sort()
print(new_list)

# List inside of a list.
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]

matrix = [l_1,l_2,l_3]
print(matrix)

print(matrix[0][0])

# First column of the matrix
first_col = [row[0] for row in matrix]
print(first_col)
