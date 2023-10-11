num1 = input("Enter the number")
num2 = input("Enter the value")
num1 = int(num1)
num2 = int(num2)
for j in range (num1,num2+1,1):
    for i in range (1,11,1):
        print(j  ," * ",i," = ", j*i)
    print()
