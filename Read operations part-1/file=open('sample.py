file=open('sample.txt','r')
print(file.readlines())
file.close()

file=open('sample.txt','r')
print(file.readline(16))
file.close()

file=open('sample.txt','a')
print(file.write('This is added line'))
file.close()
