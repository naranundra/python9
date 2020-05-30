# data.txt file ийг унших горимд
# file дээр нэмсэн уншсан брол file аа хааж байх  
f = open('data.txt', 'r')
txt = f.readlines()
for t in txt:
    print(t)
f.close()