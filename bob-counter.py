# Counts the number of bob 's, in a string determined by the user.

s = input("Enter a string: ")
bob = "bob"
counter = 0

for i in range(len(s)):
    if (s[i:i+3] == bob):
        counter = counter + 1

print("Number of bob 's in the string is: " + str(counter))
    
