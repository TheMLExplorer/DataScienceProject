string = input("Enter a string: ")

# Reverse the string
reverse_string = string[::-1]

# Check palindrome
if string == reverse_string:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
