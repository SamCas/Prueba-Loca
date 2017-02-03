# Printing on Python 3 whit parentesis, in Python 2 just with "" or ''.#
print("Hello! It's me Mario")
print("LEWL")

# New lines.
print("Here is a new line \n and this is another, but they are in the same print.")
print("And this is \t a tab.")

# String Basics.
x = len("Hello World")
print(x)

# Indexing.
x = "Hello World"
print("This is the first letter: ", x[0])
print("This is the last letter of the string: ", x[-1])

# Slicing.
print("This is the string after 'Hello'", x[5:])
print("This is before World", x[:5])
print("This is the string without the last letter: ", x[:-1])

# Frequencies.
print(x[::2])
print(x[::-1]) # Prints the string backwards.

# Immutability. You can change particular sections of a string, but you can
# concatenate another string.
b = "I like turtules!"
b = b + " ME TOO!"
print(b)

# Multiply on strings.
letter = 'z'
letter = letter*10
print(letter)

# Method calling. (Strings)
name = "Samuel Castillo Gaxiola"
print(name)
print(name.upper()) # Upper Case
print(name.lower()) # Lower Case
print(name.split())
print(name.split('a'))
