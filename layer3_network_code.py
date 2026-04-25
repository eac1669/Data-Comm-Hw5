"""
Layer 3 Network Topology for Mininet - PART 1 (Fixed version)
Uses switches for LANs. No routing between LANs.
"""

from mininet.net import Mininet
from mininet.node import Node
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink


class Router(Node):
    """Router with IP forwarding disabled."""
    def config(self, **params):
        super(Router, self).config(**params)
        self.cmd('sysctl -w net.ipv4.ip_forward=0')


def create_network():
    net = Mininet(link=TCLink)

    rA = net.addHost('rA', cls=Router)
    rB = net.addHost('rB', cls=Router)
    rC = net.addHost('rC', cls=Router)

    s1 = net.addSwitch('s1', failMode='standalone')
    s2 = net.addSwitch('s2', failMode='standalone')
    s3 = net.addSwitch('s3', failMode='standalone')

    hA1 = net.addHost('hA1', ip='20.10.172.131/26')
    hA2 = net.addHost('hA2', ip='20.10.172.132/26')

    hB1 = net.addHost('hB1', ip='20.10.172.10/25')
    hB2 = net.addHost('hB2', ip='20.10.172.11/25')

    hC1 = net.addHost('hC1', ip='20.10.172.193/27')
    hC2 = net.addHost('hC2', ip='20.10.172.194/27')

    net.addLink(hA1, s1)
    net.addLink(hA2, s1)
    net.addLink(rA, s1)

    net.addLink(hB1, s2)
    net.addLink(hB2, s2)
    net.addLink(rB, s2)

    net.addLink(hC1, s3)
    net.addLink(hC2, s3)
    net.addLink(rC, s3)

    net.addLink(rA, rB)
    net.addLink(rB, rC)
    net.addLink(rA, rC)

    net.start()

    rA.setIP('20.10.172.129/26', intf='rA-eth0')
    rB.setIP('20.10.172.1/25', intf='rB-eth0')
    rC.setIP('20.10.172.195/27', intf='rC-eth0')

    rA.setIP('20.10.100.1/24', intf='rA-eth1')
    rA.setIP('20.10.100.2/24', intf='rA-eth2')

    rB.setIP('20.10.100.3/24', intf='rB-eth1')
    rB.setIP('20.10.100.4/24', intf='rB-eth2')

    rC.setIP('20.10.100.5/24', intf='rC-eth1')
    rC.setIP('20.10.100.6/24', intf='rC-eth2')

    print("\nTesting LAN connectivity:\n")

    print("LAN A:")
    print(net.ping([hA1, hA2]))

    print("LAN B:")
    print(net.ping([hB1, hB2]))

    print("LAN C:")
    print(net.ping([hC1, hC2]))

    print("\nCross-LAN test (shouldn't work in Task 2):\n")
    print(net.pingAll())

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    create_network()