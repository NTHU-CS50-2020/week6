
height = int(input("height:\n"))

if (height < 1 or height > 7):
    print("height out of range")

for i in range(height):
    
    for j in range(height*2 + 1):
        
        if (i + j >= height - 1 and j != height and i + height + 1 >= j):
            print("#", end="")
        else:
            print(" ", end="")
            
    print("")