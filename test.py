# #Q1
# str="a:b:c:d"
# split_str=str.split(":")
# print("#".join(split_str))

# #Q2
# a={'A':90, 'B':80}
# print(a.get('C',70))

# #Q4
# A=[20,55,67,82,45,33,90,87,100,25]
# result=0
# while A:
#     a=A.pop()
#     if a>=50:
#         result += a
# print(result)

# #Q5
# import sys
# b=0
# def fib(n):
#     if n==0: return 0
#     if n==1: return 1
#     return fib(n-2)+fib(n-1)
# print(fib(4))

# #Q6
# user_input= input('숫자를 입력하세요: ')
# input=user_input.split(',')
# result=0
# while input:
#     c=input.pop()
#     c= int(c)
#     result += c
# print(result)

#Q7
# user_input=input('구구단을 출력할 숫자를 입력하세요(2~9): ')
# user_input=int(user_input)
# for i in range(1,10):
#     print(user_input*i, end=" ")


# #Q8
# f=open('abc.txt', 'r')
# lines=f.readlines()
# f.close()

# lines.reverse()
# print(lines)
# f=open('abc.txt', 'w')
# for line in lines:
#     line=line.strip()
#     f.write(line)
#     f.write('\n')
# f.close

# #Q9
# f=open('sample.txt', 'r')
# lines=f.readlines()
# f.close()

# result=0
# for line in lines:
#     score=int(line)
#     result += score

# print("총합: "+str(result))
# average=result/len(lines)

# f=open('sample.txt', 'a', encoding='utf-8')
# f.write("\n평균: "+str(average))
# f.close

# #Q10
# class Calculator:
#     def __init__(self, numberList):
#         self.numberList=numberList
#     def setdata(self, numberList):
#         self.numberList=numberList
#     def sum(self):
#         result=0
#         for num in self.numberList:
#             result += num
#         return result
#     def avg(self):
#         total=self.sum()
#         return total/len(self.numberList)


# cal1= Calculator([1,2,3,4,5])
# print(cal1.sum())
# print(cal1.avg())

# cal2= Calculator([6,7,8,9,10])
# print(cal2.sum())
# print(cal2.avg())

# #Q13
# data = "4546793"
# numbers = list(map(int, data))
# result=[]
# for i, num in enumerate(numbers):
#     result.append(str(num))
#     if i<len(numbers)-1:
#         is_odd = num%2==1
#         is_next_odd = numbers[i+1]%2==1
#         if is_odd and is_next_odd:
#             result.append("-")
#         elif not is_odd and not is_next_odd:
#             result.append("*")

# print("".join(result))

# #Q14
# def compress_string(s):
#     _c=""
#     cnt=0
#     result=""
#     for c in s:
#         if c != _c:
#             _c = c
#             if cnt: result += str(cnt)
#             result += c
#             cnt = 1
#         else:
#             cnt += 1
#     if cnt: result += str(cnt)
#     return result

# print(compress_string("aaabbccccca"))

# #Q15
# def check_numbers(s):
#     result = []
#     for num in s:
#         if num not in result:
#             result.append(num)
#         else:
#             return False
#     return len(result) == 10

# print(check_numbers("0987654321"))
# print(check_numbers("382683"))

# #Q16
# dic = {
#     '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
#     '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
#     '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
#     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
#     '-.--':'Y','--..':'Z'
# }

# def morse(src):
#     result=[]
#     for word in src.split("  "):
#         for char in word.split(" "):
#             result.append(dic[char])
#         result.append(" ")
#     return "".join(result)

# print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

# #Q18
# import re
# p = re.compile("[a-z]+")
# m = p.search("5 python")
# print(m.start() + m.end())

# #Q19
# import re
# p = re.compile('(\w+\s\d{3}[-]\d{4})[-]\d{4}')
# m = """
# park 010-9999-9988
# kim 010-9909-7789
# lee 010-8789-7768
# """
# result = p.sub("\g<1>-####", m)
# print(result)

#Q20
import re

pat = re.compile(".+[@].+[.](?=com$|net$)")
s = pat.match("pahkey@gmail.com")
print(s.group())

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())