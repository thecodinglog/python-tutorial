import json


def secretmap(a, b):
    return list(map(lambda f: ("{0:0>"+str(len(a))+"}").format(str(bin(f))[2:]).replace('0',' ').replace('1','#'), [a[i]|b[i] for i in range(0,len(a))]))


## test cases
#case1
t1 = [9, 20, 28, 18, 11]
t2 = [30, 1, 21, 17, 28]

print(json.dumps(secretmap(t1, t2)))
print('["#####", "# # #", "### #", "#  ##", "#####"]')

#case2
t11 = [46, 33, 33 ,22, 31, 50]
t22 = [27 ,56, 19, 14, 14, 10]

print(json.dumps(secretmap(t11, t22)))
print('["######", "###  #", "##  ##", " #### ", " #####", "### # "]')