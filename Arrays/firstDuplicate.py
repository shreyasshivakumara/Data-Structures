def firstDuplicate(a):
    temp = set()
    Nothing = -1
    for i in range(len(a)):
        if a[i] in temp:
            return a[i]
        else:
            temp.add(a[i]) 
    return Nothing      
