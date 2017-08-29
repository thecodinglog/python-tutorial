def sum(a, b):
    return a+b

def safe_sum(a,b):
    if type(a) != type(b):
        print("can not add")
        return
    else:
        result = sum(a,b)
    return result




#module2에서 import 하자마자 실행됨
print(safe_sum('1',3))

#방지방법
if __name__ == "__main__":
    print(safe_sum('a',5))

