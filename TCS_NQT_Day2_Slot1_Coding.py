l=int(input())  # To get lower range from user
u=int(input())     # To get Upper range from user
len=len(str(u))     # To find length of upper range
for i in range(l,u+1):     # Iterate from lower to upper
    if i<10:                # if i < 10 print 2 zeros before value
       print(("0"*(len-1))+str(i))
    elif i<100:                     # if i < 100 print 1 zeros before value
        print(("0"*(len-2))+str(i))
    else:                           # else print as it is  i.e 100
        print(str(i))


