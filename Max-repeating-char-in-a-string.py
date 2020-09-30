a = 'aaaaaadddccccccccc'
max = 0
dic = {}
for i in a:
    if(not dic.get(i)):
        dic[i] = 1
    else:
        dic[i] += 1
    if(dic[i] > max):
        max = dic[i]
        big = i
print('The biggest no is {} and its repeated {} times'.format(big,max))
