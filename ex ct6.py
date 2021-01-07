import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("www.python.org", 80))

cmd = 'GET www.pyhon.com'.encode()
# 파이썬에 있는 문자열은 유니코드로 되어있 전송할 때는 UTF-8형식으로 전송하기 위해 encode
s.send(cmd)

while True: # 수신받을 수 있는 루프
    data = s.recv(512) # 512는 버퍼의 크기
    if(len(data) < 1):
        break
    print(data.decode())
    #데이터가 외부에서 오기 때문에 출력 전에 반드시 복호화(decode)
s.close()
