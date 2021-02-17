from typing import Match


PI=3.141592


class Math:
    def solv(self,r):
        return PI*(r**2)

def add(a,b):
    return a+b


a=Math()

if __name__=="__main__":
    print(a.solv(2))