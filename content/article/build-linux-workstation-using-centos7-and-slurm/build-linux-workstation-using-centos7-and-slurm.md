Title: Build Linux Workstation Using CentOS 7 and Slurm
Date: 2018-04-10 15:45
Category: HPC
Tags: Linux, HPC, CentOS, slurm

In this post, I will show you how to build a Linux development environment for high performance computation(HPC) on a workstation. In my early post, I have shown how to build a Linux HPC cluster based CentOS 7 and Slurm (although this serries is still updating :)~ ). For the workstation case, it's much easy because you only have to consider one node.

## Basic configuration
### Network configuration
```
vi /etc/sysconfig/network-scripts/ifcfg-NET_INTERFACE_NAME

# change the following items
----------------------------------------------------------
TYPE=Ethernet
BOOTPROTO=static
IPADDR=YOUR_IPADDR
GATEWAY=YOUR_GATEWAY
NETMASK=YOUR_NETMASK
ONBOOT=yes
----------------------------------------------------------
```

```
echo "nameserver YOUR_DNS_SERVER" >> /etc/resolv.conf

echo "YOUR_IPADDR YOUR_HOST_NAME" >> /etc/hosts

echo "YOUR_HOST_NAME" >> /etc/hostname
```

```
/etc/init.d/network restart
ping -c4 bing.com
```

```
shutdown -r now
```

### Build basic software enviroment
```
yum update -y
shutdown -r now
```

```
yum install epel-release -y
yum groupinstall "Development Tools" -y
yum install kernel-devel -y
yum install dkms -y     #Dynamic Kernel Module Support
```

```
yum install htop -y
yum install bash-completion-extras -y
```

install vim 8
```
curl -L https://copr.fedorainfracloud.org/coprs/mcepl/vim8/repo/epel-7/mcepl-vim8-epel-7.repo -o /etc/yum.repos.d/mcepl-vim8-epel-7.repo
yum install vim -y
```

install python3
```
yum install yum-utils make wget
yum-builddep python
cd tmp && wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
tar xf Python-3.6.5.tar.xz && cd Python-3.6.5
./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make
make altinstall

python3.6
```

install Intel compiler family
