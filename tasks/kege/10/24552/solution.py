from ipaddress import ip_network

net = ip_network('202.71.92.91/255.255.192.0', strict=False)
ip_net = net.hosts()
for ip in ip_net:
    arr = list(map(int, str(ip).split('.')))
    if arr[0] % 2 + arr[1] % 2 + arr[2] % 2 + arr[3] % 2 == 2:
        print(ip)

