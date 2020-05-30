# файл дээр нэмэх 
def create():
    owog, ner  = input('овог, нэр: ').split()
    f = open('data2.txt' , 'a')
    f.write('\n' , + owog + '' + ner + '' + dvn)
    f.close()

remove()

# файлаас хасах
def remove():
    owog, ner  = input('овог, нэр: ').split()
    f = open('data2.txt' , 'r')
    data = f.readlines()
    f.close()
    for item in data:
        line = item.split()
        if line[0] == owog and line[1] == ner:
            print(item)
    f.close()

remove()