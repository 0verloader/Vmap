#!/bin/python
import subprocess
from socket import *
import sys
import threading


def checkUDP(host, port, ret_array, ret_index):
    """checks if there is udp connection on port #port at host"""
    udp_sock = socket(AF_INET, SOCK_DGRAM)
    udp_sock.settimeout(4)
    udp_sock.sendto("", (host, port))
    try:
        data, server = udp_sock.recvfrom(1)
        ret_array[ret_index] = 1
    except timeout:
        ret_array[ret_index] = 0
    finally:
        udp_sock.close()


def checkTCP(host, port, ret_array, ret_index):
    """checks if there is tcp connection on port #port at host"""
    tcp_sock = socket(AF_INET, SOCK_STREAM)
    try:
        tcp_sock.connect(host, port)
        ret_array[ret_index] = 1
    except:
        ret_array[ret_index] = 0
    finally:
        tcp_sock.close()


if __name__ == "__main__":

    max = int(raw_input("till:"))
    base=1200
    host = sys.argv[1]
    ret = [None] * (max * 2)
    threads = [None] * (max * 2)
    for y in range(base, max + 1, 20):
        tmp = subprocess.call('clear', shell=True)
        print int((float(y) / max) * 100), "%"
        if y + 20 > max + 1:
            z = max-base + 1
        else:
            z = y-max+ 20
        for i in range(y, z):
            threads[(2 * i) - 2] = threading.Thread(target=checkTCP, args=(host, y, ret, (2 * i) - 2))
            threads[(2 * i) - 1] = threading.Thread(target=checkUDP, args=(host, y, ret, (2 * i) - 1))
            threads[(2 * i) - 2].start()
            threads[(2 * i) - 1].start()
        for i in range(y, z):
            threads[(2 * i) - 2].join()
            threads[(2 * i) - 1].join()
    tmp = subprocess.call('clear', shell=True)
    print "100 %"
    print ret
    for y in range(0, max-base):
        if ret[y] == 1:
            print y