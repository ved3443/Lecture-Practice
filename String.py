# Python String Manipulation

print("----- Python String Manipulation -----\n")

s1 = 'Hello'
s2 = "World"
s3 = ''' Multiline
        string'''
s4 = r"Raw \n String"
print("\n")
print(s1)
print(s2)
print(s3)
print(s4)

print("\n")

# Comman String method

print("----- Comman String method -----\n")

s = "Hello World!!"

print(s.upper())
print(s.lower())
print(s.split())
print(s.endswith("!"))
print(s.startswith("H"))
print(s.find("Hello"))
print(s.count("l"))

print("\n")


# String Formatting

print("----- String Formatting -----\n")

name = "Ved"
age = "17"

# f string

print("----- f string -----\n")

print(f"Name -_- {name} Age -_- {age}")

print("\n")

# .formating

print("----- .formating -----\n")

print("Name -_- {} Age -_- {} " .format(name, age))

print("\n")

# Slicing

print("----- Slicing -----\n")

s = "Hello , Python"

print(s[0])
print(s[12])
print(s[0:5])
print(s[:5])
print(s[::-1])

print("\n")

# Joinning and Splitting in Python

print("----- Joinning and Splitting in Python -----\n")

words = ["I" , "am" , "Ved"]
print(" " .join(words))

splits = ("a, b, c")
print(splits.split(","))
