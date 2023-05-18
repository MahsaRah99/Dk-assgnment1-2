#Q3_changing a string

my_str = input("Enter a string: ")

my_str = my_str.replace(" ","")
vowels = ('A','a','E','e','I','i','O','o','U','u')
for char in vowels:
        my_str = my_str.replace(char,".")

my_str = my_str.swapcase()

print(my_str)

#string = input("Enter Your String: ")
#result = ""
#VOWELS = "aieou"
#for char in string:
#    if char.lower() in VOWELS:
#        result += "."
#    elif char != " ":
#        result += char.swapcase()

#print(result)

