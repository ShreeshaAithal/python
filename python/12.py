prision=['c','c','c','c','c','c','c','c','c','c']
print(prision)

for i in range(0,10,1):
    prision[i]="o"
print(prision)

for i in range(1,10,2):
    prision[i]="c"
print(prision)

for i in range(2,10,3):
    if prision[i]=="o":
        prision[i]="c"
    else:
        prision[i]="o"
print(prision)

for i in range(3,10,4):
    if prision[i]=="c":
        prision[i]="c"
    else:
        prision[i]="o"
print(prision)

        
