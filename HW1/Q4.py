#Q4_counting each character in a string

my_str = input("Enter any statement: ")
my_dic = {}

for char in my_str:
    if char in my_dic:
        continue
    freq = my_str.count(char)
    my_dic[char] = freq

print(my_dic)

