str='the quick brown fox jumps over the lazy dog'
result=dict()

spt=str.split(" ")
print(spt)
for i in spt:
    if i in result:
        result[i]+=1
    else:
        result[i]=1


print(result)
va={}
va["a"]=2
va['b']=3
print(va)