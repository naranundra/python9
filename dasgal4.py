# list ээс item аа устгах 
def remove():
    owog, ner  = input('овог, нэр: ').split()
    f = open('data2.txt' , 'r')
    data = f.readlines()
    f.close()
    for item in data:
        line = item.split()
        if line[0] == owog and line[1] == ner:
            data.remove(item)
    txt = ''.join(data)
    print(txt)
    f.close()

remove()

print('-'*20)

# data наас овог нэр устгах 
def remove():
    owog, ner  = input('овог, нэр: ').split()
    f = open('data2.txt' , 'r')
    data = f.readlines()
    f.close()
    for item in data:
        line = item.split()
        if line[0] == owog and line[1] == ner:
            data.remove(item)
    txt = ''.join(data)
    f = open('data2.txt', 'w')
    f.write(txt)
    f.close()

remove()