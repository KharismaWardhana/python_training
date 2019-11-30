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
    path_file = './abstrak.txt'
    file_open = open(path_file, 'rb')
except:
    print('File not found!!!')
    exit()

new_content = file_open.seek(80)
new_content = file_open.read()
print('File byte == ', new_content)
file_open.close()

encrypt = BytesIO()
encrypt.write(new_content)

try:
    new_file = '/potongan_abstrak.ser'
    path_newFile = new_dir + new_file
    writer = open(path_newFile, 'wb')
except:
    print('Something wrong happend')
    exit()

pickle.dump(encrypt, writer)
print('\n Successfully writing to new file')
writer.close()
