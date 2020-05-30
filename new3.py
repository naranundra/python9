# file устгах 
import os
os.remove(f)

# file байгаа эсэхийг шалгаад устгана байхгүй бол 
import os
if os.path.exists('demofile.txt'):
    os.remove('demofile.txt')
else:
    print('The file does not exists')

#  folder устгах 
import os 
os.rmdir('myfolder')