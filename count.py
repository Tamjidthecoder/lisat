def matcword(words):
    ctr=0
    list=[]
    for i in words:
        if len(i)>1 and i[0]==i[-1]:
            ctr +=1
            list.append(i)
    print("number of words having first and last word same\n",list)
    return ctr
count=matcword(['abc','122231','zayan','maymonnam'])
print("number of words having first and last word same:",count)