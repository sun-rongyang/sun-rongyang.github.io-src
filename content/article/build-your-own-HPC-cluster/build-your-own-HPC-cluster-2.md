title: Build Your Own HPC Cluster: (2) Configure Linux on Main Node
date: 2018-02-18 20:08
category: HPC
tags: HPC, cluster, Linux

## Install CentOS 7 on the main node
Installation of CentOS 7 is very straightforward. What I want to consider here is something need be noticed. For the hard disk partitioning, your plan should seems like:

| Partition | FileSystem | Note               |
| :-------- | :--------- | :----------------  |
| Swap      | Swap       | Memory * (1.0~2.0) |
| /boot     | xfs        |                    |
| /tmp      | xfs        | Not too large      |
| /         | xfs        |                    |
| /home     | xfs        | Large enough       |
| BIOSboot  | biosboot   | For bios boot      |

For temporary path `/tmp`, it is better to allocate a small part of the hard disk to it independently. Because all the users have `777` permission, someone wiil write some large temporary file to the path to drain the space of `/` if `/tmp` just mount to root path.

For the boot mode, we chose Legacy. Then the installation procedures are all straightforward. After installing CentOS 7, we can configure our network.

## Network configuration
At the login node, one network interface connects the Internet, the other one connects the LAN. First we get the names of the interfaces and check that they have been connected with network cable.

```shell
ip link # get the name of interface
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT qlen 1
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: enp6s0f0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT qlen 1000
    link/ether 00:25:90:98:bd:f0 brd ff:ff:ff:ff:ff:ff
3: enp6s0f1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT qlen 1000
    link/ether 00:25:90:98:bd:f1 brd ff:ff:ff:ff:ff:ff
```
**NOTE: We ignore the bash shell prompt ''#'' and we are always at root user except the final normal user test.** 

Here, we see two physical interfaces, enp6s0f0 and enp6s0f1. We select enp6s0f1 as the interface which connect Internet. We can use `ethtool` command to check whether the interface has been connected to the Internet.
```shell
ethtool enp6s0f1

Settings for enp6s0f1:
	Supported ports: [ TP ]
	Supported link modes:   10baseT/Half 10baseT/Full
	                        100baseT/Half 100baseT/Full
	                        1000baseT/Full
	Supported pause frame use: Symmetric
	Supports auto-negotiation: Yes
	Advertised link modes:  10baseT/Half 10baseT/Full
	                        100baseT/Half 100baseT/Full
	                        1000baseT/Full
	Advertised pause frame use: Symmetric
	Advertised auto-negotiation: Yes
	Speed: 1000Mb/s
	Duplex: Full
	Port: Twisted Pair
	PHYAD: 1
	Transceiver: internal
	Auto-negotiation: on
	MDI-X: off (auto)
	Supports Wake-on: d
	Wake-on: d
	Current message level: 0x00000007 (7)
			       drv probe link
	Link detected: yes # network cable connected

$ ethtool enp6s0f0
# similar output
```

Then we set the network parameters about the two interfaces.

```shell
$ vi /etc/sysconfig/network-scripts/ifcfg-enp6s0f1

TYPE=Ethernet
BOOTPROTO=static
IPADDR=your_own_internet_ip_address
NETMASK=your_netmask
GATEWAY=your_getway
NAME=enp6s0f1
UUID=1bb4d952-da42-4494-a43c-46ebc4442e0e
DEVICE=enp6s0f1
ONBOOT=yes
NETWORK=
BROADCAST=

---------------------------

$ vi /etc/sysconfig/network-scripts/ifcfg-enp6s0f0

TYPE=Ethernet
BOOTPROTO=static
IPADDR=192.168.6.1
NETMASK=255.255.255.0
NAME=enp6s0f0
UUID=c5469722-15c1-40b0-b033-fc45ef72c223
DEVICE=enp6s0f0
ONBOOT=yes
```

**NOTE: The LAN interface enp6s0f0 need not to set the "GATEWAY".**

Then we set the DNS servers.
```shell
vi /etc/resolv.conf
```
And add your own DNS servers to the file. Then we set the hosts and hostname of the login node. 

```shell
vi /etc/hosts # add the line below
-----------------------------
your_own_internet_ip_address your_loginNode_hostname # IP address and hostname of the Internet
192.168.6.1 master # IP address and hostname of the LAN

echo "your_loginNode_hostname" > /etc/hostname
```
Then, we restart the network service.
```shell
/etc/init.d/network restart

# check the Internet
ping -c4 bing.com
```
Now, we can reboot the login node.
```shell
shutdown -r now
```

## Basic Configuration
Now, we can upgrade our system first time.
```shell
yum upgrade -y
```
Then, we install some necessarily used softwares using yum.
```Shell
yum install -y wget net-tools vim
```
And we add EPEL repository and OpenHPC repository to the system.
```shell
cd /tmp
wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-10.noarch.rpm
rpm -ivh epel-release-7-10.noarch.rpm
yum install http://build.openhpc.community/OpenHPC:/1.3/CentOS_7/x86_64/ohpc-release-1.3-1.el7.x86_64.rpm
```

For the requirement for OpenHPC, we need disable by firewall.
```shell
systemctl disable firewalld
systemctl stop firewalld
```
To save time, we can also install bash autocompletion tool.
```shell
yum install bash-completion-extras -y
```

Finally, we upgrade the system again. 
```shell
yum upgrade -y
```

In next post, we will install OpenHPC and configure the provisioning system which is the most powerful tool to construct the compute nodes. Stay tuned! 
