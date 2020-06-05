import ipaddress

class MyIP(ipaddress.IPv4Address):
    def __init__(self, address, anmerkung):
        super().__init__(address)
        self.anmerkung = anmerkung


ip = MyIP("192.168.72.1", "Daddel")

print("{} {}".format(ip.is_loopback, ip.anmerkung))
