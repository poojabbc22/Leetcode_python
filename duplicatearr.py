def duplicate(array):
    for i in range(0,len(array)):
        L=array[0]
        R=array[0+1]
        if L==R:
            print("True")
        else:
            print("False")
array=[1,2,4,4,6,1]
result=duplicate(array)

