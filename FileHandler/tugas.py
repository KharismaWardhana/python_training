import os

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
    file_open = open(path_file, 'r')
except:
    print('File not found!!!')
    exit()

new_content = file_open.seek(80)
new_content = file_open.read()
print(new_content + '\n')
file_open.close()

try:
    new_file = '/potongan_abstrak.txt'
    path_newFile = new_dir + new_file
    writer = open(path_newFile, 'w')
except:
    print('Something wrong happend')
    exit()

line = writer.write(new_content)
print('Successfully writing to new file')
writer.close()
