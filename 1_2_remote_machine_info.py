import socket
import sys

def get_remote_machine_info(remote_host = 'www.python.org'):
    try:
        print("IP address: " + socket.gethostbyname(remote_host))
    except (socket.error, err_msg):
        print(remote_host + ": " + err_msg)

if __name__=='__main__':
    input_prompt = "Enter the url of a remote machine (defaults to 'www.python.org'): "
    site_url = input(input_prompt)
    get_remote_machine_info(site_url)