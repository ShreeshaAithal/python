f1 = open("in.txt","r")
num1 = f1.readlines()
print(num1[0],num1[1])
for j in range (int(num1[0]),int(num1[1])+1,1):
    
    for i in range (1,11,1):
        print(j  ," * ",i," = ", j*i)
    print()
