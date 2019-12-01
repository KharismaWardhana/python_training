from netmiko import ConnectHandler

ip_addr = input('Masukkan ip addr = ')
username = input('Masukkan username = ')
password = input('Masukkan password = ')
port = input('Masukkan port = ')

print('Options setting network : ')
print('[1] send command')
print('[2] send config file')
send_opt = input('option = ')

linux = {
    'device_type': 'linux',
    'ip': ip_addr,
    'username': username,
    'password': password,
    'port': port,
    'verbose': True
}

conn = ConnectHandler(**linux)
conn.enable()

if send_opt == '1':
    output = conn.send_command('ls /cd/home')
if send_opt == '2':
    dir_file = input('Masukkan directory config file = ')
    output = conn.send_config_from_file(dir_file)

print(output)
conn.disconnect()
