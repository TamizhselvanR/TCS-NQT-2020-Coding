key=input()      # To get key from user
keywords=['break','case','continue','default','defer','else'
          'for','func','goto','if','map','range',
          'return','struct','type','var']        # List with keywords
flag=0                              # flag initilaization
for word in keywords:
    if(word==key):                   # if key found make flag as 1 and break the Loop
        flag+=1
        break
if(flag==1):                          # If flag is 1 print found
    print("{} is a keyword".format(key))
else:                                           # Else print not found
    print("{} is not a keyword".format(key))


