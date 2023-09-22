import ipaddress
import random


def generate_ipv4_ips(cidr_network):
    """
    生成IPv4 CIDR 范围内的所有IP地址
    Args:
        cidr_network: IPv4的CIDR
    Returns:
      生成的IP地址列表
    """
    try:
        ip_network = ipaddress.ip_network(cidr_network)
        return [str(ip) for ip in ip_network.hosts()]
    except ValueError as e:
        return []


def generate_ipv6_ips(cidr_network, random_number):
    """
    IPv6 CIDR 范围内，随机生成指定数量的IP地址

    Args:
      cidr_network: IPv6的CIDR
      random_number: 要生成的随机数量
    Returns:
      生成的IP地址列表
    """
    try:
        network = ipaddress.IPv6Network(cidr_network, strict=False)
        return [str(ipaddress.IPv6Address(random.randint(int(network.network_address), int(network.broadcast_address))))
                for _ in range(random_number)]
    except ValueError as e:
        return []


def check_cidr_version(cidr):
    """判断CIDR的版本是IPv4 CIDR、IPv4 CIDR

    Args:
      cidr: 要检查的 CIDR。

    Returns: 如果是CIDR就返回对应CIDR版本，其他就返回False
    """
    try:  # IPv4、IPv6
        ip_version = "IPv{}".format(ipaddress.ip_address(cidr).version)
        raise ValueError
    except ValueError:  # 判断CIDR
        try:
            # 该函数是判断cidr版本，应该将ipv4和ipv6排除，要不然会出现判断为"是CIDR"
            cidr_str = cidr if "/" in cidr else "IPv4 or IPv6"
            return 'IPv{} CIDR'.format(ipaddress.ip_network(cidr_str).version)
        except ValueError:  # 不是CIDR
            return False


def check_ip_version(address):
    """检查 IP 地址的版本。

    Args:
      address: 要检查的 IP 地址。

    Returns:
      如果是ip地址，就返回对应ip的版本
    """

    try:  # IPv4、IPv6
        ip_address = ipaddress.ip_address(address)
        if ip_address.version:
            return "IPv{}".format(ip_address.version)
    except ValueError:
        return '不是IP地址，但是不排除是CIDR'


def check_ip_and_cidr_version(address):
    try:  # IPv4、IPv6
        return "IPv{}".format(ipaddress.ip_address(address).version)
    except ValueError:  # CIDR
        try:
            return 'IPv{} CIDR'.format(ipaddress.ip_network(address).version)
        except ValueError:  # 不是IP，也不是CIDR
            return '不是IP，也不是CIDR'


if __name__ == "__main__":
    ipv4 = '192.168.100.111'
    ipv6 = '2001:db8::1'
    ipv4_cidr = "192.166.1.0/24"
    ipv4_cidr1 = "116.129.226.128/26"
    ipv6_cidr = "2001:db8::/71"
    # 错误的IP和错误的CIDR
    str1 = "1921.144.42.2"
    str2 = "116.129.226.128/60"
    str3 = "1234:5678:9012:3456:7890:1234:5678:9012/64"

    for i in [ipv4, ipv6, ipv4_cidr, ipv4_cidr1, ipv6_cidr, str1, str2, str3]:
        # print(check_ip_version(i))
        # print(check_cidr_version(i))
        state = check_ip_and_cidr_version(i)
        if state == "IPv4 CIDR":
            print(generate_ipv4_ips(i))
        if state == "IPv6 CIDR":
            print(generate_ipv6_ips(i, 30))
