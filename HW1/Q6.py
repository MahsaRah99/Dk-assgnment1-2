#Q6_finding prime numbers

start,end = map(int, input("Enter begginig and end of an interval in a,b format: ").split(",",2))

for number in range(start+1,end):
    for  counter in range(2,number):
        if number%counter == 0:
            break
    else:
        print(number,end='  ')

print('\n')

