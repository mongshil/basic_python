# #1
# def GuGu(n):
#     result=[]
#     for i in range(1,10):
#         result.append(n*i)
#     print(result)

# GuGu(2)

# #2
# result=0
# for i in range(1,1000):
#     if i%3==0 or i%5==0:
#         result+=i
# print(result)

# #3
# def getTotalPage(m,n):
#     if m%n==0:
#         return m//n
#     else:
#         return m//n+1

# print(getTotalPage(105,20))

#7-2
import re
p = re.compile("white|blue|red|yellow")
print(p.sub('coulour', 'blue socks and red shoes', count=1))