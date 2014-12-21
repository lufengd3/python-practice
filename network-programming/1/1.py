#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import socket 
from binascii import hexlify

def get_machine_info(host):
    """
    打印设备名和ipv4地址
    """
    print "Host name is: ", host

    try:
        ip = socket.gethostbyname(host)
        print "IP address is:", ip
        convert_ipv4(ip)
        print "\nScanning host port..."
        print "Press Ctrl+C to stop scanning."
        scan_port(ip)
    except socket.error, e:
        print "Error: ", e


def convert_ipv4(ip):
    """
    将ipv4地址转换成不同格式
    """
    packed_ip = socket.inet_aton(ip)
    unpacked_ip = socket.inet_ntoa(packed_ip)
    # print "IP address: ", ip
    print "Packed format(binary):", packed_ip
    print "Packed format(hex):", hexlify(packed_ip)
    # print "Unpacked format: ", unpacked_ip

def scan_port(ip):
    """
    扫描主机开放的端口
    """
    try:
        for port in range(1, 1025):
            sock = socket.socket()
            if sock.connect_ex((ip, port)) == 0:
                print "port: %d => service name: %s" % (port, socket.getservbyport(port))
            sock.close()
    except KeyboardInterrupt:
        print "\nExit scanning."
        sys.exit()
    

if __name__ == "__main__":
    # host = socket.gethostname()
    # host = "lufeng.me"
    host = raw_input("Input the machine's domain name:\n>>>")
    get_machine_info(host)
