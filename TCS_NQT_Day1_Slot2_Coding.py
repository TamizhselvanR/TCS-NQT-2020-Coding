n=int(input())    # To get value from user
s=str(n)         # To covert int to string
odd=0             # Initializing odd and even as 0
even=0
for i in range(len(s)):
    if(i%2 == 0):    # If odd,add with odd
        odd+=int(s[i])
    else:                    # Else add with even
        even+=int(s[i])
diff=abs(odd-even)            # Do subtraction and take absolute value
print(diff)

