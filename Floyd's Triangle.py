n = int(input("Enter the number of rows :"))
z = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(z, end = " ")
        z = z + 1
    print()