# python 3.11
import ipaddress
import random


def generate_ipv4_ips(ip_range):
    """
    传入一个IPv4的CIDR，生成CIDR范围内的所有IP地址，以列表的形式返回
    args:
        ip_range: 传入一个IPv4的CIDR
    return 返回生成的列表或空列表
    """
    try:
        ip_addresses = ipaddress.ip_network(ip_range)
        return [str(ip) for ip in ip_addresses.hosts()]
    except ValueError:
        return []


def generate_ipv6_ips(ip_range, generation_number):
    """
    传入一个IPv6的CIDR，随机生成指定数量的IP地址，以列表的形式返回
    args:
        ip_range: 传入个IPv6的CIDR
        generation_number: 要生成的IP数量
    return 返回生成的列表或空列表
    """
    try:
        ip_networks = ipaddress.IPv6Network(ip_range, strict=False)
        return [str(ipaddress.IPv6Address(
            random.randint(int(ip_networks.network_address),
                           int(ip_networks.broadcast_address))))
            for _ in range(generation_number)]
    except ValueError:
        return []


if __name__ == '__main__':
    # 生成IPv4地址
    ipv4_address1 = generate_ipv4_ips('192.168.1.0/24')
    print(ipv4_address1)
    
    ipv4_address2 = generate_ipv4_ips("120.253.240.192/26")
    print(ipv4_address2)

    # 生成IPv6地址
    ipv6_address1 = generate_ipv6_ips('2400:cb00:a6a5::/48', 100)
    print(ipv6_address1)

    ipv6_address2 = generate_ipv6_ips('2001:db8::/109', 100)
    print(ipv6_address2)

    ipv6_address3 = generate_ipv6_ips('2001:db8::/48', 50)
    print(ipv6_address3)

    # 当IPv6 CIDR 的 IP 主机数量少时，会生成重复的IP地址
    ipv6_address4 = generate_ipv6_ips('2001:db8::/125', 3)
    print(ipv6_address4)

    ipv6_address5 = generate_ipv6_ips('2001:db8::/125', 100)
    print(ipv6_address5)
