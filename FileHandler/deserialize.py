import os
import pickle
from io import BytesIO

new_dir = './Aris'
if os.path.exists(new_dir) == False:
    try:
        os.mkdir(new_dir)
    except OSError:
        print('Creation of the directory %s failed' % new_dir)
        exit()
    else:
        print('Successfully created the directory %s ' % new_dir)

try:
    new_file = '/potongan_abstrak.ser'
    path_newFile = new_dir + new_file
    readfile = open(path_newFile, 'rb')
except:
    print('Something wrong happend')
    exit()

filea = readfile.read()

print('Successfully reading encrypt file')
print(filea)
readfile.close()
