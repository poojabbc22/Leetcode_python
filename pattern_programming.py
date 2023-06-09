# def pattern(n):
#     count=0
#     for row in range(0,n):
#         count +=1
#         for col in range(0,row+1):
#             count +=1
#             print("&", end=' ')
#         print()
# pattern(4)
# def pattern(n):
#     count=0
#     for row in range(0,n):
#         count +=1
#         for col in range(0,n):
#             count +=1
#             print("&", end=' ')
#         print()
# pattern(4)

# def pattern(n):
#     count=0
#     for row in range(0,n):
#         count +=1
#         for col in range(0,n-1):
#             count -=1
#             print("&", end=' ')
#         print()
# pattern(4)
# def pattern(n):
#     count=0
#     for row in range(0,n):
#         count +=1
#         for col in range(0,row):
#             count +=1
#             print(col, end=' ')
#         print()
# pattern(5)
def pattern(n):
    count=0
    for row in range(0,n):
        count +=1
        for col in range(0,(row%2)+1):
            count +=1
            print("&", end=' ')
        print()
pattern(9)