#!/bin/python
import subprocess
from socket import *
import sys
import threading


def checkUDP(host, port, ret_array, ret_index):
    """checks if there is udp connection on port #port at host"""
    udp_sock = socket(AF_INET, SOCK_DGRAM)
    udp_sock.settimeout(4)
    udp_sock.sendto("hallo", (host, port))
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
        tcp_sock.connect((host, port))
        ret_array[ret_index] = 1
    except:
        ret_array[ret_index] = 0
    finally:
        tcp_sock.close()



if __name__ == "__main__":
    max_=1310
    base=1300
    host = sys.argv[1]
    ret = [None] * ((max_-base) * 2)
    threads = [None] * ((max_-base) * 2)
    for y in range(base, max_ + 1, 20):
        tmp = subprocess.call('clear', shell=True)
        print int((float(y) / max_) * 100), "%"
        if y + 20 > max_ + 1:
            z = max_-base + 1
        else:
            z = y-base+ 20
        k=y-base
        p_temp=y
        for i in range(k, z):
            threads[(2 * i) - 2] = threading.Thread(target=checkTCP, args=(host, p_temp, ret, (2 * i) - 2))
            threads[(2 * i) - 1] = threading.Thread(target=checkUDP, args=(host, p_temp, ret, (2 * i) - 1))
            threads[(2 * i) - 2].start()
            threads[(2 * i) - 1].start()
            p_temp=p_temp+1
        for i in range(k, z):
            threads[(2 * i) - 2].join()
            threads[(2 * i) - 1].join()
    tmp = subprocess.call('clear', shell=True)
    print "100 %"
    print ret

    for y in range(0, (max_ - base)*2):
        if ret[y]==1:
            if y % 2 ==1:
                temp=y-1#udp
                print "udp"
            else:
                temp=y#tcp
                print "tcp"
            temp=temp/2+1
            print base+temp
