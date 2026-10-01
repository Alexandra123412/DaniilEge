from ipaddress import ip_network

net = ip_network('192.168.12.207/255.192.0.0', strict=False)
ip_net = net.hosts()
for ip in ip_net:
    b_ip = f"{int(ip):032b}"
    a = b_ip.count('1')
    b = b_ip.count('0')
    if a == b:
        print(ip)