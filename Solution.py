def function(s):
    i=flag=count=0
    sub="
    while i<len(s):
        if s[i] not in sub:
            sub = sub + s[i]]
            flag=0
        else:
            count + 1
            sub=''
            flag = 1 
        if flag == 0:
            i+=1
    if sub is not '': 
        print(count+1)
    else: 
        print(count)
