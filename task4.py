width = int(input("Enter width square:"))
height = int(input("Enter height square: "))
for i in range(0, height):
    for j in range(1, width):
        print("*", end = "")
    print("*")
