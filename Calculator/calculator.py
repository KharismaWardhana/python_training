while True :
    a = input("Masukkan angka pertama : ")
    b = input("Masukkan angka kedua : ")
    operator = input("Masukkan operator : ")

    list_operator = ['+', '-', 'x', ':']
    while operator not in list_operator:
        print("operator yg anda inputkan salah")
        print("List supported operator = ")
        print("[ + - x : ]")
        operator = input("Masukkan operator : ")

    if operator == '+':
        print('hasil = ', float(a) + float(b))
    if operator == '-':
        print('hasil = ', float(a) - float(b))
    if operator == 'x':
        print('hasil = ', float(a) * float(b))
    if operator == ':':
        print('hasil = ', float(a) / float(b)) 

    print('\n')
    check = input('Apakah anda ingin keluar ? ')
    print('\n')
    if check == 'y':
        break
