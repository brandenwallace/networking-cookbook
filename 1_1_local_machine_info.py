import socket

def print_machine_info():
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)

    print("Hostname: {}".format(hostname))
    print("IP address: {}".format(ipaddress))

if __name__=='__main__':
    print_machine_info()