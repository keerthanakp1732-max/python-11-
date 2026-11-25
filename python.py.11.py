


'''a=[10,2.3,True,5j,'hi',[1,2],(1,2),{1,2},{'a':10}]
print(a)'''


'''a=[10,2.3,True,'Hello']
a.append(10)
print(a)
a.remove(True)
print(a)
a.pop()
print(a)
a.pop(0)
print(a)'''


''' a=(10,2.3,5j,True,'hi',[1,2],(1,2),{1,2},{'A':10})
print(a[-1])'''

'''a={10,2.3,5j,False,'hi',(1,2)}
print(a)'''

'''a={{1:2}}
print(a)
'''
'''a={'a':[10,20,30],'b':40}
print(a['a'][1])'''

'''a='Hello'
print(a[3:0:-1])
print(a[-2:-5:-1])
print(a[::-1])'''
'''a='Good Morning'

'Mng'

print(a[5:11+1:3])
print(a[5::3])
print(a[-7::3])'''

''''nr '
print(len(a[-2:-8-1:-3]))'''

'''a=int(input("enter:"))

if a%2==0:
    print('even')
else:
    print('odd')
'''
'''l=eval(input("enter list:"))
if len(l)==5:
    print('yes')
else:
    print('no')'''

'''ch=input("enter:")

if "A"<=ch<="Z":
    print('upper')
elif "a"<=ch<="z":
    print('lower')
else:
    print('not an alpha')'''


'''un=input('enter:')
if un=='hero':
    print('correct username')
    pw=input("enter:")
    if pw=='hi@123':
        print('successfull login')
    else:
        print('incorrect pw')
else:
    print('incorrect un')'''


'''username='Hero'
password='Hi@123'

un=input('enter the un:')
if un==username:
    pw=input('enter the pw:')
    if pw==password:
        print('login')
    else:
        print('incorrect pw')
else:
    print('incorrect un')
'''

'''i=1
while i<=100:
    print(i)
    i+=1'''


'''i=1
while i<=50:
    if i%2==0:
        print(i,'even')
    i+=1
'''


'''i=2
while i<=50:
        print(i)
    i+=2
'''

'''n=int(input('enter num:'))
rev=0

while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print(rev)'''


'''for i in range(1,101):
    print(i)'''

'''for i in range(1,51):
    if i%2==0:
        print(i,'even')'''

'''l=[10,20,30]
for i in l:
    print(i)'''


'''s=input('enter:')
out=''

for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)'''

'''s=input("enter:")
rev=''

for i in s:
    rev=i+rev
print(rev)'''



'''for i in range(1,6):
    for j in range(1,6):
        print('*',end='')
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('1',end=' ')
        else:
            print('@',end=' ')
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i<j:
            print('1',end=' ')
        else:
            print('@',end=' ')
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i>j:
            print('1',end=' ')
        else:
            print('@',end=' ')
    print()'''

'''def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert(input('enter a string:'),''))'''

'''def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
print(convert(input('enter a string:'),''))'''

'''def convert():
    s=input('enter')
    out+=' '
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
convert()'''

'''def convert():
    s=input('enter:')
    out=''
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert())'''

'''class college:
    cname='GPLN'
    cloc='Hoodi'
s1=college()
print(s1.cname,s1.cloc)
college.cloc='KR PURAM'
print(college.cloc)

print(s1.cloc)

print('changing loc wtrsp obj')
s1.cloc='Hoodi'

print(s1.cloc)

print(college.cloc)'''

'''class college:
    cname='GPLN'
    cloc="Hoodi"
s1=college()
s1.snmae='Harish'
s1.phone=9866574788

s2=college()
s2.sname='Girish'
s2.phone=7865490875
print(s1.cloc)
s1.cloc='Kr Puram'
print('After changing')
print(s1.cloc)
print(s2.cloc)
print(college.cloc)'''

'''class college:
    def __init__(self,name,phno,usn):
        self.name=name
        self.phno=phno
        self.usn=usn
s1=college('Harish',9876543210,'234ed')
s2=college('Girish',675432198,'235ed')
print(s1.name)
print(s2.name)'''

'''class college:
    def __init__(self,name,phno,usn):
        self.name=name
        self.phno=phno
        self.usn=usn
    def display(self):
        print(self.name,self.phno,self.usn)
s1=college('Harish',9876543,'a1e3r3r')
s2=college('Girish',9876543,'#13531r')
s1.display()
s2.display()'''



    

