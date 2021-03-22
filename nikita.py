from socket import *

def main():
    ip_add = "192.168.1.7"
    port = 80

    try:
        get_socket_con = socket(AF_INET,SOCK_STREAM)
        get_socket_con.bind((ip_add,port))
        get_socket_con.listen(10)
        while 1:
            client_con,client_addr = get_socket_con.accept()
            print("Vistor found!  [{}]".format(client_addr[0]))
            b=open("403.html","rb")
            client_con.send(b.read())
            d = client_con.recv(2048)
            print(d.decode('utf-8'))
    except error as identifier:
        print(" UNspecified [{}]" .format(identifier)) 

    except KeyboardInterrupt as key:
        print("process terminated")
    finally:            
        f = open("demofile.log", "a")
        f.write(d.decode('utf-8')) 
        get_socket_con.close()
    get_socket_con.close()
    exit()


if __name__ == "__main__":
    main()