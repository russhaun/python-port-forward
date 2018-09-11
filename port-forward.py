# Author: Mario Scondo (www.Linux-Support.com)
# Date: 2010-01-08
# Script template by Stephen Chappell
#
# This script forwards a number of configured local ports
# to local or remote socket servers.
#
# Configuration:
# Add to the config file port-forward.config lines with
# contents as follows:
#   <local incoming port> <dest hostname> <dest port>
#
# Start the application at command line with 'python port-forward.py'
# and stop the application by keying in <ctrl-c>.
#
#
#
import os
import socket
import sys
try: 
    import thread
except ImportError: 
    import _thread as thread
import time


def main(setup, error):
    # open file for error messages
    sys.stderr = error
    # read settings for port forwarding
    print("[*] Docker Proxy: Starting setup.........")
    for settings in parse(setup):
        #print(settings)
        thread.start_new_thread(server(settings))
    # wait for <ctrl-c>
    while True:
       time.sleep(60)

def parse(setup):
    print("[*] Docker Proxy: Reading config.........")
    settings = []
    #print(settings)
    for line in setup:
        # skip comment line
        #print(line)
        if line.startswith('#'):
            continue   
        parts = line.split()
        settings.append((int(parts[0]), parts[1], int(parts[2])))
    #print(settings)   
    return settings

def server(settings):
    try:
        print("[*] Docker Proxy: Server starting..........")
        dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dock_socket.bind(('', settings[0]))
        dock_socket.listen(5)
        print("[*] Docker Proxy: Proxy running..........")
        while True:
            client_socket = dock_socket.accept()[0]
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((settings[1], settings[2]))
            thread.start_new_thread(forward, (client_socket, server_socket))
            thread.start_new_thread(forward, (server_socket, client_socket))
    finally:
        thread.start_new_thread(server(settings))

def forward(source, destination):
    string = ' '
    #print(destination)
    while string:
        string = source.recv(1024)
        if string:
            #print(string)
            destination.sendall(string)
        else:
            source.shutdown(socket.SHUT_RD)
            destination.shutdown(socket.SHUT_WR)

if __name__ == '__main__':
    if os.path.isfile('port-forward.config'):
        try:
            print("[*] Docker Proxy: config file exits continuing")
            setup = open('port-forward.config', 'r')
            error = open('error.log', 'a')
            main(setup, error)
        except KeyboardInterrupt:
            print('closing')
        #else:
        #    print("[*] Docker Proxy: Config file not found please make sure 'port-forward.config' is present")
        #    sys.exit()