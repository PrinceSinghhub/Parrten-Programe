n=int(input("Enter your number"))
for i in range (n):
    for j in range (n,i,-1):
        print(j,end="")
    print(" "*(2*i),end="")
for k in range(i+1,n+1):
    print(k,end="")
print()
