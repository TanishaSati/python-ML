n=int(input("Enter a number : "))
num=n
sum=0
while(num>0):
    digit=num%10
    sum+=digit
    num//=10
print("the sum is ",sum)