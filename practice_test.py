#p.112 연습문제 1번
a=80+75+55
print(a/3)

#p.112 연습문제 2번


#p.112 연습문제 3번
pin="881120-1068234"
yymmdd=pin[0:6]
num=pin[7:-1]
print(yymmdd)
print(num)

#p.113 연습문제 4번
print(pin[7])

#p.113 연습문제 5번
a="a:b:c:d"
b=a.replace(':','#')
print(b)

#p.113 연습문제 6번
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#p.114 연습문제 7번
a=['Life','is','too','short']
result=" ".join(a)
print(result)

#p.114 연습문제 8번
a=(1,2,3)
b=(4,)
print(a+b)

#p.115 연습문제 10번
a={'A':90,'B':80,'C':70}
result=a.pop('B')
print(a)
print(result)

#p.115 Q11
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

#p.115 Q12
a=b=[1,2,3]
a[1]=4
print(b)

#p.146 Q2
result=0
i=1
while i<=1000:
    if i%3==0:
        result=result+i
    i=i+1

print(result)

#p.147 Q3
i=0
while True:
    i=i+1
    if i>5: break
    print('*'*i)

#p.147 Q4
for i in range(1,101):
    print(i)

#p.148 Q5
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total=total+score
average=total/10
print(average) 

#p.148 Q6
numbers=[1,2,3,4,5]
result=[n*2 for n in numbers if n%2==1]
print(result)

#p.179 Q1
def is_odd(number):
    if number%2==0:
        return True
    else:
        return False

print(is_odd(3))

#p.179 Q2
def avg_numbers(*args):
    result=0
    for i in args:
        result = result+i
    return result/len(args)

print(avg_numbers(1,2,3,4,5))

#p.179 Q3
# input1=input('첫번째 숫자를 입력하세요:')
# input2=input('두번째 숫자를 입력하세요:')

# total=int(input1)+int(input2)
# print("두 수의 합은 %s입니다." %total)

# #p.180 Q5
f1=open("test.txt", 'w', encoding='utf-8')
f1.write("Life is too short")
f1.close()
f2=open("test.txt", 'r')
data=f2.read()
print(data)
f2.close()

#p.181 Q6
user_input=input("저장할 내용을 입력하세요:") #you need java
f=open("test.txt", 'a', encoding='utf-8')
f.write("\n")
f.write(user_input)
f.write("\n")
f.close()

#p.181 Q7
f=open("test.txt",'r')
body=f.read()
f.close()
body2=body.replace("java",'python')
f=open("test.txt", 'w')
f.write(body2)
f.close

#p.262 Q1
class Calculator:
    def __init__(self):
        self.value=0
    def add(self, val):
        self.value+=val

class UpgradeCalculator(Calculator):
    def min(self, val):
        self.value-=val

cal=UpgradeCalculator()
cal.add(10)
cal.min(7)

print(cal.value)

#p.262 Q2
class Calculator:
    def __init__(self):
        self.value=0
    def add(self,val):
        self.value +=val

class MaxLimitCalculator(Calculator):
    def add(self,val):
        self.value +=val
        if self.value>100:
            self.value=100

cal=MaxLimitCalculator()

cal.add(50)
cal.add(60)

print(cal.value)

#p.263 Q4
print(list(filter(lambda a: a>0, [1,-2,3,-5,8,-3])))

#p.263 Q5
print(int(0xea))

#p.264 Q6
print(list(map(lambda a: a*3, [1,2,3,4])))

#p.264 Q7
print(max([-8,2,7,5,-3,5,0,1])+min([-8,2,7,5,-3,5,0,1]))

#p.264 Q8
print(round(17/3,4))

#p.264 Q9
import sys
numbers=sys.argv[1:]

result=0
for number in numbers:
    result = result + int(number)

print(result)

#p.265 Q10
import os
os.chdir("c:\coding")
result=os.popen("dir")
print(result.read())

#p.265 Q11
import glob
print(glob.glob("c:\coding\*.py"))

#p.265 Q12
import time
print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))

#p.265 Q13
import random
result=[]
while len(result)<6:
    num=random.randint(1,45)
    if num not in result:
        result.append(num)

print(result)