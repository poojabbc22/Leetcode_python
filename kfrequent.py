def ktimes(array,k):
    count={}
    for i in range(len(array)+1):
        freq=[]
    for n in array:
        count[n]=1+count.get(n,0)
    for n,c in count.items():
            freq[c].append(n)
    res=[]
    for i in range(len(freq) -1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res)==k:
                return res
array=[1,2,3,3,4,1,7]
k=3
result=ktimes(array,k)
print(result)

        


