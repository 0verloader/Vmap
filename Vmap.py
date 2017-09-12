#!/usr/bin/python
import subprocess
from socket import *
import threading
import time
from decimal import Decimal


def check_udp(host, port, ret_array, ret_index):
    """Check if there is udp connection on port#port at host."""
    udp_sock = socket(AF_INET, SOCK_DGRAM)
    udp_sock.settimeout(7)
    udp_sock.sendto("hallo", (host, port))
    try:
        data, server = udp_sock.recvfrom(1)
        ret_array[ret_index] = 1
    except timeout:
        ret_array[ret_index] = 0
    finally:
        udp_sock.close()


def check_tcp(host, port, ret_array, ret_index):
    """Check if there is tcp connection on port #port at host."""
    tcp_sock = socket(AF_INET, SOCK_STREAM)
    tcp_sock.settimeout(12)

    try:
        tcp_sock.connect((host, port))
        ret_array[ret_index] = 1
    except:
        ret_array[ret_index] = 0
    finally:
        tcp_sock.close()


def port_translate(port):
    """Find the protocol that used the port."""
    return {
        1: "[tcpmux] TCP port service multiplexer",
        5: "[rje] Remote Job Entry",
        7: "[echo] Echo service",
        9: "[discard] Null service for connection testing",
        11: "[systat] System Status service for listing connected ports",
        13: "[daytime] Sends date and time to requesting host",
        17: "[qotd] Sends quote of the day to connected host",
        18: "[msp] Message Send Protocol",
        19: "[chargen] Character Generation service; sends endless stream of characters",
        20: "[ftp-data] FTP data port",
        21: "[ftp] File Transfer Protocol (FTP) port; sometimes used by File Service Protocol (FSP)",
        22: "[ssh] Secure Shell (SSH) service",
        23: "[telnet] The Telnet service",
        25: "[smtp] Simple Mail Transfer Protocol (SMTP)",
        37: "[time] Time Protocol",
        39: "[rlp] Resource Location Protocol",
        42: "[nameserver] Internet Name Service",
        43: "[nicname] WHOIS directory service",
        49: "[tacacs] Terminal Access Controller Access Control System for TCP/IP based authentication and access",
        50: "[re-mail-ck] Remote Mail Checking Protocol",
        53: "[domain] domain name services (such as BIND)",
        63: "[whois++] WHOIS++, extended WHOIS services",
        67: "[bootps] Bootstrap Protocol (BOOTP) services; also used by Dynamic Host Configuration Protocol (DHCP) services",
        68: "[bootpc] Bootstrap (BOOTP) client; also used by Dynamic Host Control Protocol (DHCP) clients",
        69: "[tftp] Trivial File Transfer Protocol (TFTP)",
        70: "[gopher] Gopher Internet document search and retrieval",
        71: "[netrjs-1] Remote Job Service",
        72: "[netrjs-2] Remote Job Service",
        73: "[netrjs-3] Remote Job Service",
        73: "[netrjs-4] Remote Job Service",
        79: "[finger] Finger service for user contact information",
        80: "[http] HyperText Transfer Protocol (HTTP) for World Wide Web (WWW) services",
        88: "[kerberos] Kerberos network authentication system",
        95: "[supdup] Telnet protocol extension",
        101: "[hostname] Hostname services on SRI-NIC machines",
        102: "[iso-tsap] ISO Development Environment (ISODE) network applications",
        105: "[csnet-ns] Mailbox nameserver; also used by CSO nameserver",
        107: "[rtelnet] Remote Telnet",
        109: "[pop2] Post Office Protocol version 2",
        110: "[pop3] Post Office Protocol version 3",
        111: "[sunrpc] Remote Procedure Call (RPC) Protocol for remote command execution, used by Network Filesystem (NFS)",
        113: "[auth] Authentication and Ident protocols",
        115: "[sftp] Secure File Transfer Protocol (SFTP) services",
        117: "[uucp-path] Unix-to-Unix Copy Protocol (UUCP) Path services",
        119: "[nntp] Network News Transfer Protocol (NNTP) for the USENET discussion system",
        123: "[ntp] Network Time Protocol (NTP)",
        137: "[netbios-ns] NETBIOS Name Service used in Red Hat Enterprise Linux by Samba",
        138: "[netbios-dgm] NETBIOS Datagram Service used in Red Hat Enterprise Linux by Samba",
        139: "[netbios-ssn] NETBIOS Session Service used in Red Hat Enterprise Linux by Samba",
        143: "[imap] Internet Message Access Protocol (IMAP)",
        161: "[snmp] Simple Network Management Protocol (SNMP)",
        162: "[snmptrap] Traps for SNMP",
        163: "[cmip-man] Common Management Information Protocol (CMIP)",
        164: "[cmip-agent] Common Management Information Protocol (CMIP)",
        174: "[mailq] MAILQ email transport queue",
        177: "[xdmcp] X Display Manager Control Protocol (XDMCP)",
        178: "[nextstep] NeXTStep window server",
        179: "[bgp] Border Gateway Protocol",
        191: "[prospero] Prospero distributed filesystem services",
        194: "[irc] Internet Relay Chat (IRC)",
        199: "[smux] SNMP UNIX Multiplexer",
        201: "[at-rtmp] AppleTalk routing",
        202: "[at-nbp] AppleTalk name binding",
        204: "[at-echo] AppleTalk echo",
        206: "[at-zis] AppleTalk zone information",
        209: "[qmtp] Quick Mail Transfer Protocol (QMTP)",
        210: "[z39.50] NISO Z39.50 database",
        213: "[ipx] Internetwork Packet Exchange (IPX), a datagram protocol commonly used in Novell Netware environments",
        220: "[imap3] Internet Message Access Protocol version 3",
        245: "[link] LINK / 3-DNS iQuery service",
        347: "[fatserv] FATMEN file and tape management server",
        363: "[rsvp_tunnel] RSVP Tunnel",
        369: "[rpc2portmap] Coda file system portmapper",
        370: "[codaauth2] Coda file system authentication services",
        372: "[ulistproc] UNIX LISTSERV",
        389: "[ldap] Lightweight Directory Access Protocol (LDAP)",
        427: "[svrloc] Service Location Protocol (SLP)",
        434: "[mobileip-agent] Mobile Internet Protocol (IP) agent",
        435: "[mobilip-mn] Mobile Internet Protocol (IP) manager",
        443: "[https] Secure Hypertext Transfer Protocol (HTTP)",
        444: "[snpp] Simple Network Paging Protocol",
        445: "[microsoft-ds] Server Message Block (SMB) over TCP/IP",
        464: "[kpasswd] Kerberos password and key changing services",
        468: "[photuris] Photuris session key management protocol",
        487: "[pim-rp-disc] Rendezvous Point Discovery (RP-DISC) for Protocol Independent Multicast (PIM) services",
        500: "[isakmp] Internet Security Association and Key Management Protocol (ISAKMP)",
        535: "[iiop] Internet Inter-Orb Protocol (IIOP)",
        538: "[gdomap] GNUstep Distributed Objects Mapper (GDOMAP)",
        546: "[dhcpv6-client] Dynamic Host Configuration Protocol (DHCP) version 6 client",
        547: "[dhcpv6-server] Dynamic Host Configuration Protocol (DHCP) version 6 Service",
        554: "[rtsp] Real Time Stream Control Protocol (RTSP)",
        563: "[nntps] Network News Transport Protocol over Secure Sockets Layer (NNTPS)",
        565: "[whoami] whoami user ID listing",
        587: "[submission] Mail Message Submission Agent (MSA)",
        610: "[npmp-local] Network Peripheral Management Protocol (NPMP) local / Distributed Queueing System (DQS)",
        611: "[npmp-gui] Network Peripheral Management Protocol (NPMP) GUI / Distributed Queueing System (DQS)",
        612: "[hmmp-ind] HyperMedia Management Protocol (HMMP) Indication / DQS",
        631: "[ipp] Internet Printing Protocol (IPP)",
        636: "[ldaps] Lightweight Directory Access Protocol over Secure Sockets Layer (LDAPS)",
        674: "[acap] Application Configuration Access Protocol (ACAP)",
        694: "[ha-cluster] Heartbeat services for High-Availability Clusters",
        749: "[kerberos-adm] Kerberos version 5 (v5) 'kadmin' database administration",
        750: "[kerberos-iv] Kerberos version 4 (v4) services",
        765: "[webster] Network Dictionary",
        767: "[phonebook] Network Phonebook",
        873: "[rsync] rsync file transfer services",
        992: "[telnets] Telnet over Secure Sockets Layer (TelnetS)",
        993: "[imaps] Internet Message Access Protocol over Secure Sockets Layer (IMAPS)",
        994: "[ircs] Internet Relay Chat over Secure Sockets Layer (IRCS)",
        995: "[pop3s] Post Office Protocol version 3 over Secure Sockets Layer (POP3S)",
    }.get(port, "[unknown]")


if __name__ == "__main__":
    while(True):
        host = raw_input("host (exit): ")
        if host == "exit":
            break
        base = int(raw_input("base port: "))
        max_ = int(raw_input("max port: ")) + 1
        if(max_ < base or base < 1):
            continue
        ret = [None] * ((max_ - base) * 2)
        threads = [None] * ((max_ - base) * 2)
        start = time.time()
        for y in range(base, max_ + 1, 20):
            tmp = subprocess.call('clear', shell=True)
            print int((float(y - base) / (max_ - base)) * 100), "%"
            if y + 20 > max_ + 1:
                z = max_ - base
            else:
                z = y - base + 20
            k = y - base
            p_temp = y
            for i in range(k, z):
                threads[(2 * i)] = threading.Thread(target=check_tcp, args=(host, p_temp, ret, (2 * i)))
                threads[(2 * i) + 1] = threading.Thread(target=check_udp, args=(host, p_temp, ret, (2 * i)+ 1))
                threads[(2 * i)].start()
                threads[(2 * i) + 1].start()
                p_temp = p_temp + 1
            for i in range(k, z):
                threads[(2 * i)].join()
                threads[(2 * i) + 1].join()
        tmp = subprocess.call('clear', shell=True)
        print "100 %  [COMPLETE]"
        for y in range(0, (max_ - base) * 2):
            if ret[y] == 1:
                if y % 2 == 1:
                    '''udp'''
                    temp = y - 1
                    print "[UDP]",
                else:
                    '''tcp'''
                    temp = y
                    print "[TCP]",
                temp = temp / 2
                print base + temp, port_translate(base + temp)
                print round(Decimal(time.time() - start), 1), "s"
        print "__________________"
