# Data Communication Homework 5 - Mininet Layer 3 Network Simulation

## Author
Elan A. Cote

## Overview
This project implements a Layer 3 network topology using Mininet. The network consists of:
- 3 routers: rA, rB, rC
- 3 LANs connected via switches
- Multiple hosts per LAN
- A router backbone network using 20.10.100.0/24

The goal of this assignment is to demonstrate:
- IP addressing and subnetting
- Static routing configuration
- Inter-router communication
- End-to-end connectivity testing using ping and traceroute

---

## Network Topology

### LAN Subnets
- LAN A: 20.10.172.128/26
- LAN B: 20.10.172.0/25
- LAN C: 20.10.172.192/27

### Backbone Network
- Inter-router links: 20.10.100.0/24

### Routers
- rA connects LAN A and backbone
- rB connects LAN B and backbone
- rC connects LAN C and backbone

---

## Requirements

Install dependencies:
    pip install -r requirements.txt

## How to Run

After starting the Mininet-VM, run

sudo python3 layer3_network_code.py
rA sysctl -w net.ipv4.ip_forward=1
rB sysctl -w net.ipv4.ip_forward=1
rC sysctl -w net.ipv4.ip_forward=1

Add routes:
rA route add -net 20.10.172.0 netmask 255.255.255.128 gw 20.10.100.2
rA route add -net 20.10.172.192 netmask 255.255.255.224 gw 20.10.100.3

rB route add -net 20.10.172.128 netmask 255.255.255.192 gw 20.10.100.1
rB route add -net 20.10.172.192 netmask 255.255.255.224 gw 20.10.100.3

rC route add -net 20.10.172.128 netmask 255.255.255.192 gw 20.10.100.1
rC route add -net 20.10.172.0 netmask 255.255.255.128 gw 20.10.100.2

Finally, you can perform ping and traceroute test like:

    Ping:
        hA1 ping -c 4 hB1

    Traceroute:
        hA1 traceroute hC1
        hA2 traceroute hC1
        hB1 traceroute hC1

## Notes
Each LAN is connected using a switch (Layer 2 domain)
Routers forward packets between subnets using IP forwarding
Static routes define paths between LANs via backbone links
No dynamic routing protocols are used

