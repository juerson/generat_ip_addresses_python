# python 3.11
import ipaddress
import random


def generate_ipv4_ips(ip_range):
    """
    传入一个IPv4的CIDR，生成CIDR范围内的所有IP地址，以列表的形式返回
    args:
        ip_range (str): 传入一个IPv4的CIDR
    yield
        str: CIDR 范围内的每个 IP 地址
    """
    try:
        ip = ipaddress.ip_network(ip_range)
        for addr in ip.hosts():
            yield str(addr)
    except ValueError:
        yield ValueError("传入的值错误！")


def generate_ipv6_ips(ip_range, count):
    """
    传入一个IPv6的CIDR，随机生成指定数量的IP地址，以列表的形式返回
    args:
        ip_range: 传入一个IPv6的CIDR
        count: 要生成的IP数量
    yield
        str: CIDR 范围内的每个 IP 地址
    """
    try:
        network = ipaddress.IPv6Network(ip_range)
        ipv6_addrs = []
        for i in range(count):
            random_int = random.randint(int(network.network_address), int(network.broadcast_address))
            random_addr = ipaddress.IPv6Address(random_int)
            # 去掉重复的
            if random_addr not in ipv6_addrs:
                ipv6_addrs.append(random_addr)
                yield str(random_addr)
    except ValueError:
        yield ValueError("传入的值错误")


if __name__ == '__main__':
    # 生成IPv4地址
    ipv4_address1 = list(generate_ipv4_ips('192.168.1.0/24'))
    print(ipv4_address1)
    ipv4_address2 = list(generate_ipv4_ips("120.253.240.192/26"))
    print(ipv4_address2)

    # 生成IPv6地址
    ipv6_address1 = list(generate_ipv6_ips('2400:cb00:a6a5::/48', 100))
    print(ipv6_address1)

    ipv6_address2 = list(generate_ipv6_ips('2001:db8::/109', 100))
    print(ipv6_address2)

    ipv6_address3 = list(generate_ipv6_ips('2001:db8::/48', 50))
    print(ipv6_address3)

    # 当IPv6 CIDR 的 IP 主机数量少时
    ipv6_address4 = list(generate_ipv6_ips('2001:db8::/125', 3))
    print(ipv6_address4)

    ipv6_address5 = list(generate_ipv6_ips('2001:db8::/125', 100))
    print(ipv6_address5)
