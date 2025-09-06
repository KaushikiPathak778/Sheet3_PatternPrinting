n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-i):
        if ((j==0) or j==(n-i-1)):
            print("*",end=" ")
        else:
            print("_",end=" ")
    print()