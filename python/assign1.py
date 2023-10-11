start = int(input("Enter the start value :"))
end = int(input("Enter the end value: "))

for num in range(start,end + 1):
    for i in range(1,11):
        print(f"{num} * {i} = {num * i}")
    print()
