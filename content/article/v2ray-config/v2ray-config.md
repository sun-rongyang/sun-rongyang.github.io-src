Title: V2Ray Configuration
Date: 2018-04-30 16:06
Category: Web
Tags: Web, Linux, CentOS, Windows, MacOS, v2ray
Status: draft


## Basic configuration
```
yum upgrade -y
yum install git -y
mkdir github-repos && cd github-repos
git clone https://github.com/sun-rongyang/dotfiles.git
ln /root/github-repos/dotfiles/OnLinux/general/bashrc_global.sh /etc/profile.d/bashrc_global.sh

yum install vim -y
vim ./ssh/authorized_keys

yum install epel-release -y
yum groupinstall "Development Tools" -y
yum install kernel-devel -y
yum install dkms -y     # Dynamic Kernel Module Support

yum install htop -y
yum install bash-completion-extras -y
```

## Install V2Ray
```
bash <(curl -L -s https://install.direct/go.sh)
```

## Configure V2Ray
### Time
```
yum install ntp -y
ntpdate time.nist.gov
crontab -e
---------------
* */2 * * * ntpdate time.nist.gov
---------------
systemctl restart crond
```

### Configuration file
```
vim /etc/v2ray/config.json

{
  "log" : {
    "access": "/var/log/v2ray/access.log",
    "error": "/var/log/v2ray/error.log",
    "loglevel": "warning"
  },
  "inbound": {
    "port": 10086,
    "protocol": "vmess",
    "settings": {
      "clients": [
        {
          "id": "UUID",
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
