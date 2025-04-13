height = int(input("Enter the height :"))
row = 1
while row <= height:
    col = 1
    while col <= height:
        print(" ", end = "" )
        col = col + 1
    col = 1
    while col <= row:
        print("*", end = "")
    print()
    row = row + 1