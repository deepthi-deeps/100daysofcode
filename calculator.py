print("Enter the operation (add,sub,mul,div): ")
operation = input()
if operation == "add":
 x = [int(x) for x in input("Enter the values: ").split()] 
 print("Answer: ")
 answer = sum(x)
 print(answer)
elif operation == "sub":
 a = int(input("First value: "))
 b = int(input("Second value: "))
 output= a - b
 print (output)
elif operation == "mul":
  i = int(input("First number:"))
  j = int(input("Second number:"))
  output = i * j
  print(output)
else:
  u = int(input("First Number: "))
  v = int(input("Second Number: "))
  output = u/v
  print(output)