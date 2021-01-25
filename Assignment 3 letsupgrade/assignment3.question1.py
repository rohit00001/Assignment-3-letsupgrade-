#Question 1
#Write a python program to merge two files into third file –
#Program

data = data2 = "" 
with open('file1.txt') as fp: 
    data = fp.read() 
 with open('file2.txt') as fp: 
    data2 = fp.read()
data += "\n"
data += data2 
with open ('file3.txt', 'w') as fp: 
fp.write(data)