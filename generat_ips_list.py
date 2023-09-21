# python 3.11
import ipaddress
import random


def generate_ipv4_ips(cidr_network):
    """ 生成 IPv4 CIDR 范围内的所有IP地址 """
    try:
        ip_network = ipaddress.ip_network(cidr_network)
        return [str(ip) for ip in ip_network.hosts()]
    except ValueError as e:
        return []


def generate_ipv6_ips(cidr_ip, num_ips):
    """生成IPv6 CIDR 范围内，随机num_ips个IP地址"""
    try:
        network = ipaddress.IPv6Network(cidr_ip, strict=False)
        return [str(ipaddress.IPv6Address(random.randint(int(network.network_address), int(network.broadcast_address))))
                for _ in range(num_ips)]
    except ValueError as e:
        return []


if __name__ == '__main__':
    # 生成IPv4地址
    ipv4_address1 = generate_ipv4_ips('192.168.1.0/24')
    print(ipv4_address1)
    ipv6_address2 = generate_ipv4_ips("120.253.240.192/26")
    print(ipv6_address2)

    # 生成IPv6地址
    ipv6_address1 = generate_ipv6_ips('2400:cb00:a6a5::/48', 100)
    print(ipv6_address1)

    ipv6_address2 = generate_ipv6_ips('2001:db8::/109', 100)
    print(ipv6_address2)

    ipv6_address3 = generate_ipv6_ips('2001:db8::/48', 210)
    print(ipv6_address3)

    # 当cidr的主机IP数量不足（含随机的IP数据超过CIDR范围内容的IP数量），会生成重复的IP
    ipv6_address4 = generate_ipv6_ips('2001:db8::/125', 3)
    print(ipv6_address4)

    ipv6_address5 = generate_ipv6_ips('2001:db8::/125', 100)
    print(ipv6_address5)
