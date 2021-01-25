
a=""
with open("a.txt", encoding='utf-8') as f:
    try:
        a = f.read()
    except UnicodeEncodeError as e:
        pass
b=a.split("：")
for i in range(0,len(b)):
    with open((str(i)+"a.txt"),'a+', encoding='utf-8') as f:
        try:
            f.write(b[i])
        except UnicodeEncodeError as e:
            pass

