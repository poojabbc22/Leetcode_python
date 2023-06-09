import collections
def groupanagrm(list):
    res=collections.defaultdict(list)
    for s in list:
        count=[0]*26
        for c in s:
            count[ord(c)-ord("a")]+=1
        res[tuple(count)].append(s)
    return res.values()
list=["ram","sita","madam"]

