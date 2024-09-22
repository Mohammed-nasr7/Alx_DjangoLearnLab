size = int(input("Enter the size of the pattern:"))
rows = 0
while rows < size :
    for col in range(size):
        print("*", end="")
    print()
    rows +=1    