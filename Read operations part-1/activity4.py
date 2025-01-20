file1=open('sample3.txt','r')
file2=open('sample4.txt','w')
for i in file1.readlines():
    if not (i.startswith("Hasnain")):
        file2.write(i)
file1.close()
file2.close()