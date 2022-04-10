x="balasubramanian"
dict={}
for i in x:
    # keys=dict.keys()
    # print(keys)
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=+1
print(dict)