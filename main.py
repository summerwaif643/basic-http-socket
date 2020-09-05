import socket
import sys

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Please insert a link.")
    elif len(sys.argv) >= 1:

        for element in sys.argv:
            print (element)

        browser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        browser_socket.connect((sys.argv[1], 80))

        get_command = "GET "+ sys.argv[1] +" HTTP/1.0\r\n\r\n".encode()
        browser_socket.send(get_command)

        while True:
            data = browser_socket.recv(512)
            if len(data) < 1:
                break
            print(data.decode(), end='')

        browser_socket.close() 