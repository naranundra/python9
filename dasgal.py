# овог нэр дүн оруулаад data2.txt file руу бичнэ 
owog,ner,dvn = input('Овог нэр дүн: ').split()
f = open('data2.txt', 'a')
f.write("\n" + owog + ' ' + ner + ' ' + dvn)
f.close()


