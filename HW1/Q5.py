#Q5_Comparing laptops

num = int(input('how many laptops you wanna compare? '))
laptops_list = list(tuple(map(int,input("Enter price,quality :").split(','))) for r in range(num)) 

print(laptops_list,'\n')
flag = False

for i in laptops_list:
    for j in laptops_list:
        if i[0] > j[0]:
            if i[1] < j[1]:
                flag = True
                break
    if flag:
        break


if flag:
    print("Founded")
else:
    print("Not Found")


    
