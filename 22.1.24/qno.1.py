 REVERSE A NUMBER

LOGIC 1

n=int(input())
print(str(n)[::-1])

LOGIC 2

n=int(input())
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n//=10
    
print(rev)
