

print('---------------------------	---------------------------')
import fileinput
for line in fileinput.input('123.txt',backup='.back'):
	line=line.replace('999','123')
	print(line,end='')

f=open('123.txt.back')
print(f.read())


	