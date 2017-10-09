import re

sample = "1D2S3T*"

p = re.compile("\d+[SDT][*#]?")


def parse(exp):
    n = re.compile("^\d+")
    b = re.compile("[SDT]")
    o = re.compile("[*#]*$")
    number = n.search(exp).group()
    bonus = b.search(exp).group()
    option = o.search(exp).group()
    return number, bonus, option


def calc(operand, operator):
    if operator == 'S':
        return operand
    elif operator == 'D':
        return operand ** 2
    elif operator == 'T':
        return operand ** 3


tryList = p.findall(sample)
option = ''
acc = 0

while len(tryList) > 0:
    el = parse(tryList.pop())
    val = calc(int(el[0]), el[1])

    if option == '*':
        val = val * 2
        option = ''

    if el[2] == '*':
        val = val * 2
        option = '*'
    elif el[2] == '#':
        val = val * -1

    acc += val

print(acc)
