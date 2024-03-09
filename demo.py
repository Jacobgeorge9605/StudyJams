num = int(input("Enter a number : "))
if(num<0):
    print("Please enter a positive number")
else:
    sum = 0
    sum = (num*(num+1))/2
print(f"sum of ",num,"is : ",sum)