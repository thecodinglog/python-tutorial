import re


def get_list(text):
    text = text.lower()
    text_list = []
    p = re.compile('[a-z]{2}')

    if len(text) == 0:
        return text_list
    for i in range(0, len(text) - 1):
        if p.match(text[i] + text[i + 1]):
            text_list.append(text[i] + text[i + 1])
    return text_list


def get_dic(items):
    dic = {}
    for item in items:
        if dic.get(item):
            dic[item] = dic[item] + 1
        else:
            dic[item] = 1
    return dic


def similarity(str1, str2):
    dic1 = get_dic(get_list(str1))
    dic2 = get_dic(get_list(str2))

    if len(dic1) == 0 or len(dic2) == 0:
        return 1

    set1 = set(dic1)
    set2 = set(dic2)

    inter_set = set1.intersection(set2)
    union_set = set1.union(set2)

    inter_rate = sum([min([dic1[key], dic2[key]]) for key in inter_set])
    union_rate = sum([max([dic1.get(key) or 0, dic2.get(key) or 0]) for key in union_set])

    return inter_rate / union_rate


def answering(str1, str2):
    return int(similarity(str1, str2) * 65536)


test_cases = []
test_cases.append(('FRANCE', 'french', 16384))
test_cases.append(('handshake', 'shake hands', 65536))
test_cases.append(('aa1+aa2', 'AAAA12', 43690))
test_cases.append(('E=M*C^2', 'e=m*c^2', 65536))

for case in test_cases:
    print(answering(case[0], case[1]))
