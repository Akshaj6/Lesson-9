height = int(input("Enter the height :"))
row = 0
while row < height:
    col = 0
    while col < row:
        print(" ", end= "" )
        col = col + 1
    col = 0
    while col < (height - row):
        print("*", end= "")
        col = col + 1
    print()
    row = row + 1