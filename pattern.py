# def pattern1(n):
#     count=0
#     for row in range(0,n):
#         count +=1
#         for col in range(0,n):
#             count +=1
#             print("*", end=' ')
#         print()
# pattern(4)

# def pattern2(n):
   
#     for row in range(0,n):
#         row +=1
#         for col in range(0,row+1):
#             col +=1
#             print("*",end="")
#         print()
# pattern2(4)
# def pattern3(n):
#     count=0
#     for row in range(0,n):
#         count+=1
#         for col in range(0,row+1):
#             count +=1
#             print(col,end=" ")
#         print()
# pattern3(5)
# def pattern4(n):
#     for row in range(0,n):
#         row +=1
#         for col in range(0,row):
#             col +=1
#             print(row,end=" ")
#         print()
# pattern4(5)
# def pattern5(n):
#     count=0
#     for row in range(0,n):
#         count +=1
#         for col in range(0,n-row+1):
#             count +=1
#             print("*",end=" ")
#         print()
# pattern5(5)
# def pattern6(n):
#     for row in range(0,n):
#         row +=1
#         for col in range(0,n-row+1):
#             col +=1
#             print(col,end=" ")
#         print()
# pattern6(5)
# def pattern7(n):
#     for row in range(0,n):
#         row +=1
#         for col in range(0,n-row-1):
#             col +=1
#             print()
#             for col in range(0,2*row+1):
#                   col+=1
#                   print("*",end=" ")
#                   for col in range(0,n-row-1):
#                     col+=1
#                     print()
#             print()             
# pattern7(5)
# def pattern10(n):
#     for row in range(0,2*n-1):
#         row+=1
#         star=row
#         if(row>n):
#             star=2*n-row
#         for col in range(0,star):
#             col +=1
#             print("*",end=" ")
#         print()
# pattern10(5)
# def pattern11(n):
#     for row in range(0,n):
#         row+=1
#         if (row%2==0):
#             start=1
#         else:
#             start=0
#         for col in range(0,row-1):
#             col +=1
#             print(start,end=" ")
#             start=1-start
#         print()
# pattern11(5)
# def pattern12(n):
#     space=2*(n-1)
#     for row in range(0,n):
#         row+=1
#         #numbers
#         for col in range(0,row):
#             col +=1
#             print(col,end=" ")
#             #space
#             for col in range(0,space):
#                 col +=1
#                 print()
#             for col in range(row,1):
#                 col -=1
#                 print(col,end=" ")
#             print()
#             space -=2
# pattern12(5)
# def pattern13(n):
#     num=1
#     for row in range(0,n):
#         row +=1
#         for col in range(0,row):
#             col +=1
#             print(num,end=" ")
#             num=num +1
#         print()
# pattern13(5)
# def pattern14(n):
#   for row in range(1,n+1):
#     for ch in range(65, 65+row):
#       print(chr(ch), end=" ")
#     print("")
# pattern14(5)
# def pattern15(n):
#   for row in range(0,n):
#     for ch in range(65, 65+(n-row+1)):
#       print(chr(ch), end=" ")
#     print("")
# pattern15(5)
# def pattern16(n):
#   for row in range(0,n):
#     char=chr(65 +row)
#     for col in range(0,row+1):
#         print(char,end=" ")
#     print("")
# pattern16(5)
# def pattern17(n):
#     for row in range(0,n):
#         row +=1
#         #spaces
#         for col in range(0,n-row-1):
#             col +=1
#             print()
#         #characters
#         char=chr(65)
#         breakup=(2*row+1)/2
#         for col in range(1,2*row+1):
#             col +=1
#         if(row<=breakup):
#             char +=1
#         else:
#             char -=1
#         #spaces
#         for col in range(0,n-row-1):
#             col +=1
#             print()
#         print()
# pattern17(5)
# def pattern15(n):
#   for row in range(0,n):
#     for ch in range(70-row,69,-1):
#       print(chr(ch), end=" ")
#     print("")
# pattern15(1)

def pattern18(n):
    for row in range(0,n):
      for ch in range(70-row,70):
        print(chr(ch), end=" ")
      print("")
pattern18(5)
# def pattern19(n):
#     inis=0
#     for row in range(1,n):
  
#         for col in range(1,n-row):
           
#             print("*")
#         for col in range(1,2*n):
#             print()
#         for col in range(1,n-row):
#             print("*")
        
#         inis +=2
#         print()
# pattern19(5)
# def pattern21(n):
#     for row in range(0, n):
#         for col in range(0, n):
#             if row == 0 or col == 0 or row == n - 1 or col == n - 1:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()

# pattern21(5)
