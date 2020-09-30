key=input()      # To get key from user
keywords=['break','case','continue','default','defer','else',
          'for','func','goto','if','map','range',
          'return','struct','type','var'] # List with keywords
flag=0# flag initilaization
if key in keywords:
    print("{} is a keyword".format(key))
else:
    print("{} is not a keyword".format(key))
