
import socket, hashlib, os

client = socket.socket()

client.connect(('localhost', 9999))
md5 = hashlib.md5()


def send_to_server(client, msg):
    '''
    check if server is ready
    :param client:
    :param msg:
    :return: True or False
    '''
    client.send(msg.encode(encoding='utf-8'))
    rtn = client.recv(50)
    print(rtn)
    if rtn == b'ok':
        return True
    else:
        return False


while True:
    operation = input('Do you wanna upload or download ? >>:').strip()
    if not operation:
        print('can not input blank.')
        continue
    elif 'upload' == operation:
        filename = ''
        if send_to_server(client, operation):
            filename = input('Server is ready, please type in the filename of which you wanna upload:').strip()
        # print(filename)
        isfile = os.path.isfile(filename)
        if isfile:
            readin = open(filename, encoding='utf-8').read()  # read is all in once for now
            # print(content)
            cont = readin.encode(encoding='utf-8')  # get md5 code of upload file
            # print(b)
            md5.update(readin.encode(encoding='utf-8'))
            # print(md5.hexdigest())
            code = md5.hexdigest()
            # print(code)
            send_to_server(client, code)
            if not send_to_server(client, filename):  # send filename
                exit('Fail to send file name.')

            length = os.stat(filename).st_size
            print(length)
            if send_to_server(client, str(length)):
                print('a')
                client.send(cont)

    elif 'download' == operation:
        filename = input('Please type in the filename of which you wanna download:').strip()
        pass
    else:
        print('Those are the options you can choose from:\n upload, download')

client.close()

isfile = os.path.isfile('test.txt')
data = open('test.txt', encoding='utf-8').read()
print(data)
code = md5.update(data.decode())
print(code)
