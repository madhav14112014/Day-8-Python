n=int(input("Enter the input whose sum you want to find: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
    print("The sum of first",n,"numbers is:",sum)