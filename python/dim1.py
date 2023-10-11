s1 = "funw"
spacer = "$"
len1 = len(s1)
for j in range(1,len1+1,1):
    for i in range(0,len1-j,1):
        print(spacer, end = "")
    print(s1[0:j])
for i in range(0,1,1):
    print(spacer, end = "")
print(s1[0:3])
for i in range(0,2,1):
    print(spacer, end = "")
print(s1[0:2])
for i in range(0,3,1):
    print(spacer, end = "")
print(s1[0:1])
