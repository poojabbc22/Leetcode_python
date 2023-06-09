def anagram(string):
    lst=list(s)
    lst1=list(t)
    for i in range(0,len(lst1)):
        temp=0
        temp=t[i]
        t[i]=t[i+1]
        t[i+1]=temp
    if lst1==lst:
        print("True")
    else:
        print("False")
s="median"
t="indian"
