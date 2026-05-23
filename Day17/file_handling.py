
# file handling ??
# performing operations on files 

# create 
# read 
# write 
# update 
# delete 

# using python 

# types of files 
# .txt 
# .csv ---> comma separated values 
# JSON files -->
# binary files ---> image ,mp3 files , zip files 


# modes in file handling 

# r ---> read 
# w ---> write 
# a ---> append 
# x --> create 
# r+ ---> read and write 
# w+ --> read and write 
# a+ ---> append and read 
# rb --> read binary 
# wb ---> write binary 

'''
try:
    f=open("file1.txt",'x')

except Exception as e :
    print(e)


f=open("file1.txt",'r')
data = f.read()    # read()---> reads all the lines 
print(data)



f=open("file1.txt",'w')   # w ---> override all the data 
f.write("file handiling class")
f.close()


with open("file1.txt",'r') as f:
    data=f.readline()    # reads only one line 
    print(data)



with open("file1.txt",'r') as f:
    data=f.readlines()    # returs all the lines in the form of list 
    print(data)


with open("file1.txt",'r') as f:
    data=f.read(10)    # reads only one line 
    print(data)



with open("file1.txt",'w') as f:
    f.write("im batman\n")
    f.write("im batman\n")
    f.write("im batman")


with open("file1.txt",'a') as f:
    f.write("\nim superman")

'''

with open("file1.txt",'r+') as f:
    print(f.read())
    f.write("\n extra")
    print(f.read())




