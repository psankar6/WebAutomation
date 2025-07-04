#reverse strring
def string_reverse(s):
    rev=""
    for char in s:
        rev=char+rev
    return rev
original_string="Parthiban sankaran"
reverse_String=string_reverse(original_string)
print(f"The Original string is {original_string}")
print(f"The Revered String is  {reverse_String}")