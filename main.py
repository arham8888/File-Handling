fileobj=open("sample.txt",'r')
print(fileobj.read())
fileobj=open("sample.txt",'w')
fileobj.write("Hi there")
fileobj=open("sample.txt",'r')
count=0
for i in fileobj.readlines():
    count=count=1
print("The number of lines is " , count)


