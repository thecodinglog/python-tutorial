f = open("newfile.txt", "w", encoding='utf-8')
for i in range(1, 11):
    data = "%d번째 줄\n" % i
    f.write(data)

f.close()

f = open("newfile.txt", "r", encoding='utf-8')
line = f.readline()
print(line)
f.close()

f = open("newfile.txt", "r", encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()


f = open("newfile.txt", "r", encoding="utf-8")
lines  = f.readlines()
for line in lines:
    print(line)
f.close()



f = open("newfile.txt","r",encoding="utf-8")
data = f.read()
print(data)
f.close()


#자동 file close
# with block 끝날 때 자동 close
with open("newfile.txt","a",encoding="utf-8") as f:
    f.write("new one")

with open("newfile.txt","r",encoding="utf-8") as f:
    data = f.read()
print(data)

