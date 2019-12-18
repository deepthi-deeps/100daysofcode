list = []
number = int(input('How many numbers: '))
for n in range(number):
    num = int(input('Enter number '))
    list.append(num)
print(list)
print("Sum = ", sum(list))