import ipaddress
ips = []

def enumerateIP(subnets):
    for x in subnets:
        net = ipaddress.ip_network(x)
        ipa = net.hosts()
        for addr in ipa:
            ips.append(addr)

def returnIP():
    return ips
    
enumerateIP(subnets)

returnIP()