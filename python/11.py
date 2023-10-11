def diamond1(word1):
    s1=word1
    len1=len(s1)
    for i in range(0,len1+1,1):
        print(s1[0:i+1])
    for i in range(len1,0,-1):
        print(s1[0:len1])
diamond1("ShreeshaAithal")
print()
