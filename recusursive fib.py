def fiboncci(n):
    if(n<=1):
        return n
    else:
        return(fiboncci(n-1)+fiboncci(n-2))
n=int(input("enter number of terms:"))
print("fiboncci sequence:")
for i in range(n):
    print(fiboncci(i))
