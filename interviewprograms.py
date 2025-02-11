def reverse_string(s):
    return s[::-1]

input_String="MALAYALAM"
reversed_string=reverse_string(input_String)

print("Original string:", input_String)
print("reversed_string",reversed_string)

assert input_String== reversed_string
print("The given string is palindrome")

