Title: V2Ray Configuration
Date: 2018-04-30 16:06
Category: Web
Tags: Web, Linux, CentOS, Windows, MacOS, v2ray
Status: draft


## Basic configuration
Set some custom usage for bash.
```bash
yum install wget
wget -o /etc/profile.d/bashrc_global.sh https://raw.githubusercontent.com/sun-rongyang/dotfiles/master/OnLinux/general/bashrc_global.sh
bash
```

Use SSH key to log in the server.
```bash
vi ./ssh/authorized_keys
```

Change SSH port and forbidden root password log in.
```bash
vi /etc/ssh/sshd_config
```
change the following item.
```
...

Port SSH_PORT   # change ssh port

...

# forbid root password log in.
Match User root
    PasswordAuthentication no
```

```bash
sestatus
semanage port -a -t ssh_port_t -p tcp SSH_PORT
systemctl restart sshd
```

```bash
yum upgrade -y
yum install vim -y
yum install epel-release -y
yum groupinstall "Development Tools" -y
yum install kernel-devel -y
yum install dkms -y     # Dynamic Kernel Module Support
yum install htop -y
yum install bash-completion-extras -y
yum install git -y
```

## Install V2Ray
```bash
bash <(curl -L -s https://install.direct/go.sh)
```

## Configure V2Ray
### Time
```bash
yum install ntp -y
ntpdate time.nist.gov
```
```bash
crontab -e
```
```
* */2 * * * ntpdate time.nist.gov
```
```bash
systemctl restart crond
```

### Configuration file
```bash
vim /etc/v2ray/config.json
```

```json
{
  "log" : {
    "access": "/var/log/v2ray/access.log",
    "error": "/var/log/v2ray/error.log",
    "loglevel": "warning"
  },
  "inbound": {
    "port": V2RAY_LISTEN_PORT,
    "protocol": "vmess",
    "settings": {
      "clients": [
        {
          "id": "YOUR_UUID",
          "level": 1,
          "alterId": 64
        }
      ]
    }
  },
  "outbound": {
    "protocol": "freedom",
    "settings": {}
  }
}
```

### Start
```bash
systemctl status v2ray

netstat -plnt | grep v2ray
```
