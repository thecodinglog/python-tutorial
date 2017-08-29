import module1
print(module1.sum(3,4))

print(module1.safe_sum(3,5))

print(module1.safe_sum(3,'a'))

print(module1.sum(10,20))

#모듈의 메소드를 바로 임포트
from module1 import sum, safe_sum
#from module1 import *  => 모든 메소드를 사용
print(sum(3,4))
print(safe_sum(45,4))


import module3

a = module3.Math()
print("class call : "+a.solv(2))
