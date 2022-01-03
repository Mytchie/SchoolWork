import os.path

# function to exchnage data between 2 file
def data_exchange(file1,file2):
    with open(file1,'r') as data1:
        fileData1= data1.readlines()

    with open(file2, 'r') as data2:
        fileData2=data2.readlines()

    f = open(file1, 'r+')
    f.truncate(0)

    f = open(file2, 'r+')
    f.truncate(0)

    for eachline in fileData1:
      filesecond = open(file2,'a')
      filesecond.write(eachline)

    for eachline in fileData2:
      filefirst = open(file1,'a')
      filefirst.write(eachline)

file1 = input("Enter first file name: ")

while(os.path.isfile(file1)==False):
  file1 = input("Please enter valid file: ")

#input file2
file2 = input("\nEnter second file name: ")

while(os.path.isfile(file2)==False):
  file2 = input("Please enter valid file: ")

data_exchange(file1,file2)