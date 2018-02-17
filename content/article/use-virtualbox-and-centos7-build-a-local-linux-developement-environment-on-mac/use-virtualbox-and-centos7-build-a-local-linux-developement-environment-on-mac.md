Title: Use Virtualbox and CentOS 7 Build a Local Linux Developement Environment on Mac
Date: 2018-02-17 18:27
Category: Unix/Linux
Tags: Linux, OSX, Mac, VM

## Introduction
Although the Mac OS X operating system is _similar_ as Linux, there are still several differences between them. So it is necessarily to switch to a pure Linux at any time you want if you are a developer for Linux. The most convenient way is ssh to a Linux server when you have a usable internet connection. But internet is not always usable, for example, you are in a aircraft. If one can virtualise a pure Linux environment at background in your local machine and log in though ssh and use a local file system as shared folder, that is very convenient. In this post, I will show you how to virtualise a Linux environment at background locally and set a local folder as a shared folder for the virtual machine. When you ssh to the virtual machine though a local port, you can use this pure Linux environment as your familiar remote Linux server.

## Install Virtualbox on Mac
Virtualbox installation on your Mac is very easy. You just need go to the [download page](http://download.virtualbox.org/virtualbox/5.2.6/), download the [dmg file](http://download.virtualbox.org/virtualbox/5.2.6/VirtualBox-5.2.6-120293-OSX.dmg) (version 5.2.6, now) and install it.

## Install CentOS 7 in the Virtualbox
Linux environment installation is still straightforward. I select CentOS 7 as an example, here. You can chose any Linux distribution as you want, like Ubuntu, OpenSUSE and Arch.

First, download CentOS 7 distribution iso file at [official website](https://www.centos.org/download/).

Then open the Virtualbox application and click `New`:

![]({attach}figure/install-centos7-in-the-virtualbox-1.png)

and type some basic information:

![]({attach}figure/install-centos7-in-the-virtualbox-2.png)

Then set memory size of your virtual machine:

![]({attach}figure/install-centos7-in-the-virtualbox-3.png)

Then create a virtual hard disk to your virtual machine:

![]({attach}figure/install-centos7-in-the-virtualbox-4.png)

![]({attach}figure/install-centos7-in-the-virtualbox-5.png)

![]({attach}figure/install-centos7-in-the-virtualbox-6.png)
`Dynamically allocated` can save hard disk space of your Mac.

![]({attach}figure/install-centos7-in-the-virtualbox-7.png)

Then mount CentOS 7 installation iso file to the optical drive of your virtual machine:

![]({attach}figure/install-centos7-in-the-virtualbox-8.png)

![]({attach}figure/install-centos7-in-the-virtualbox-9.png)

Finally, `Start` the virtual machine and install the CentOS 7 follow the installation guide.

![]({attach}figure/install-centos7-in-the-virtualbox-10.png)

### Network configurations for the virtual machine
After normal installation, the virtual machine can not connect to the Internet, because the network device is not turned on when you boot for default configuration. We need modify the default configuration:
```
    vi /etc/sysconfig/network-scripts/ifcfg-enp0s3
```
Modify `ONBOOT=no` to `ONBOOT=yes` and reboot.

## Install Virtualbox Guest Additions
### Download the matched version iso file
First get the version of your Virtualbox, and go to the [download page](http://download.virtualbox.org/virtualbox/5.2.6/)(for 5.2.6) to download matched version Virtualbox guest additions iso file, `VBoxGuestAdditions_[version].iso` (for 5.2.6: [VBoxGuestAdditions_5.2.6.iso](http://download.virtualbox.org/virtualbox/5.2.6/VBoxGuestAdditions_5.2.6.iso)).

### Install required packages on CentOS 7 virtual machine
Before install Virtualbox guest additions, we need install some development tools which are needed. The following commends need be executed by a root account or a account with `sudo`.

```
    yum update
    yum groupinstall "Development Tools"
    yum install kernel-devel
    yum install epel-release
    yum install dkms
```

### Run installation script to install Virtualbox guest additions
First, we mount the iso file on the optical drive of the virtual machine like when we installed CentOS 7 and reboot. Then we create a folder to mount the optical drive:
```
    mkdir /tmp/VBoxLinuxAdditions
    mount /dev/cdrom /tmp/VBoxLinuxAdditions/
```

Then we install Virtualbox guest additions:
```
    cd /tmp/VBoxLinuxAdditions
    sh /tmp/VBoxLinuxAdditions/VBoxLinuxAdditions.run
```

Finally, we reboot the virtual machine:
```
    shutdown -r now
```

## Set SSH Login through Localhost
### In Virtualbox application
First, we need shut down the virtual machine. Then we set ssh login port:

![]({attach}figure/set-ssh-login-through-localhost-1.png)

![]({attach}figure/set-ssh-login-through-localhost-2.png)

![]({attach}figure/set-ssh-login-through-localhost-3.png)

### Start up the virtual machine through command line
You can start up and manage your virtual machine through command line. We can list all the virtual machines on the host machine:
```shell
    VBoxManage list vms

    ...
    "CentOS7" {055381a3-fa87-4ed9-a2a7-4a426cd42c44}
    ...
```
And start up the virtual machine by the command:
```shell
   VBoxManage startvm CentOS7 --type headless

   Waiting for VM "CentOS7" to power on...
   VM "CentOS7" has been successfully started.
```
where `--type headless` start up the virtual machine in the background. If you want to use GUI, you can change it as `--type gui`. Then you can list all the running virtual machines:
```shell
    VBoxManage list runningvms

    "CentOS7" {055381a3-fa87-4ed9-a2a7-4a426cd42c44}
```
And you can shut down the running virtual machine:
```shell
    VBoxManage controlvm CentOS7 poweroff
```

### Connect your virtual machine through command line
After started up your virtual machine using `--type headless`, you can connect to your virtual machine through command line as connecting to a remote Linux server:

![]({attach}figure/set-ssh-login-through-localhost-4.png)

## Set Shared Folder for the Virtual Machine
### In the Virtualbox application
Now we shut down the virtual machine and set a folder of host machine as the shared folder:

![]({attach}figure/set-shared-folder-for-the-virtual-machine-1.png)

![]({attach}figure/set-shared-folder-for-the-virtual-machine-2.png)

![]({attach}figure/set-shared-folder-for-the-virtual-machine-3.png)

### Share the folder to normal user on the virtual machine
Now we start up the virtual machine. And we can find the shared folder at `/media/sf_[NameOfTheSharedFolder]`. But this folder can only be readded/written by root and users in the `vboxsf` group. We need add normal user to the `vboxsf` group to use the shared folder:
```shell
    usermod -a -G vboxsf USER
```
where `USER` is the name of user you want to add to `vboxsf` group. Then reboot the virtual machine.

### Mount the shared folder to a appointed path
Now we can use the shared folder, but it is convenient to mount the folder automatically to a appointed path during start up. Add the following code to `/etc/rc.local`
```
    mount -t vboxsf -o uid=USER_UID,gid=USER_GID NameOfTheSharedFolder /a/appointed/path
```
`USER_UID` and `USER_GID` can be found in `/etc/passwd` file. Then add `-x` attribute to the file:
```shell
   chmod +x /etc/rc.d/rc.local
```
Finally, reboot the virtual machine. You will find the shared folder with read/write have been mounted at `/a/appointed/path` .

That's it! A local pure Linux environment with a host machine shared folder has been constructed.
