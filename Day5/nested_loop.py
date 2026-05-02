'''
# nested loops -- loop inside a loop 

for i in range(1,5): # 1,2,3,4
    for j in range(1,6): # 1,2,3,4,5
        print(i,j)

# for every outer loop , inner loop will excecute completely 

l =[[1,2] ,[3,4] ,[5,6]]
total = 0

for row in l:
    for val in row:
        total = total + val
print(total)


# square pattern 

# # # # 1
# # # # 2
# # # # 3
# # # # 4


for i in range(1,5):  #  rows  
    for j in range(1,5): # column values
        print("*",end=" ")
    print()

# right angled triangle 
#
# #
# # # 
# # # # 
# # # # # 

for i in range(1,5): # rows
    for j in range(i): #
        print("*", end=" ")
    print()


for i in range(1,5): # rows
    for j in range(i): #
        print("*" * i, end=" ")
    print()

# reverse 
for i in range(5 ,0, -1):
    for j in range(i):
        print("*",end=" ")
    print()


# reverse of right angled triangle 

# # # # #  5
  # # # #  4
    # # #  3
      # #  2
        #  1

'''

rows = 5
for i in range(rows):   # generating the rows  

    for j in range(i):  # print spaces 
        print(" " , end="")

    for k in range(rows-i): # print *
        print("*",end="")
    print()



