# Switching variable outcomes between a and b by creating a new third variable (cup) to switch with.
a = input("a: ")
b = input("b: ")

# creating a new variable to "have another cup to switch with"
c = a
a = b
b = c

print("a: " + a)
print("b: " + b)
