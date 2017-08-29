def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


print(sum_many(99, 1))


def sum_and_mul(a, b):
    return a + b, a * b


result = sum_and_mul(3, 4)
print(result)
print(type(result))


def say_myself(name, old, man=True):
    print("my name is %s" % name)
    print("I'm %d years old" % old)
    if man:
        print("I'm a man")
    else:
        print("I'm a girl")


say_myself("Kim", 23)
say_myself("Lee", 52, False)
