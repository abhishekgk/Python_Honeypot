from socket import *
import tqdm
import os

SEPERATOR = "<SEPERATOR>"
BUFFER_SIZE = 4096 #send 4096 bytes each time step

def main():
    ip_add = "0.0.0.0"
    port = 8080
    filename="modified403.html"
    filesize=os.path.getsize(filename)

    try:
        get_socket_con = socket(AF_INET,SOCK_STREAM)
        get_socket_con.bind((ip_add,port))
        get_socket_con.listen(10)
        while 1:
            client_con,client_addr = get_socket_con.accept()
            print("Vistor found!  [{}]".format(client_addr[0]))
            client_con.send(f"{filename}{SEPERATOR}{filesize}".encode())
            with open(filename, "rb") as f:
                while True:
                    # read the bytes from the file
                    bytes_read = f.read(BUFFER_SIZE)
                    if not bytes_read:
                    # file transmitting is done
                        break
                    # we use sendall to assure transimission in 
                    # busy networks
                    client_con.sendall(bytes_read)
                    #update the progress bar
                    progress.update(len(bytes_read))
            
            data = client_con.recv(2048)
            print(data.decode('utf-8'))
    except error as identifier:
        print(" UNspecified [{}]" .format(identifier)) 

    except KeyboardInterrupt as key:
        print("process terminated")
    finally:
        get_socket_con.close()
    get_socket_con.close()

if __name__ == "__main__":
    main()