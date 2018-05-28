Title: V2Ray Configuration
Date: 2018-04-30 16:06
Modified: 2018-05-28 23:21
Category: Web
Tags: Web, Linux, CentOS, Windows, MacOS, IOS, Android, v2ray


## Server (To be continued)
### Basic configuration
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

### Install V2Ray
```bash
bash <(curl -L -s https://install.direct/go.sh)
```

### Configure V2Ray
#### Time
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

#### Configuration file
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

#### Setup
```bash
systemctl status v2ray

netstat -plnt | grep v2ray
```

## Client
Check the time of your client device first.

### Windows
- Create a new folder at any path you want with any name to contain client app and data. I use `V2RayN` here.
- Download the newest version client app [V2RayN](https://github.com/2dust/v2rayN). Go to [V2RayN-release](https://github.com/2dust/v2rayN/releases), select a version and download related `v2rayN.exe` file to `V2RayN` folder.
- Download `v2ray` core for Windows. Go to [v2ray-core-release](https://github.com/v2ray/v2ray-core/releases), select a version and download related `v2ray-windows-64.zip` file. Then extract to `V2RayN` folder.
- Go to `V2RayN` folder and `double click v2rayN` to setup the client. If you meet some problem, you should check whether the version of your `.NET framework` is larger than 4.5. If everything goes right, you can find an icon at lower right system tray.
- `click` the icon => `Server`(`服务器`) => `Add [VMess] server`(`添加[VMess]服务器`)
- Set parameters which include `address`, `port`, `id`, `alterId` and `remarks`. Then `click` `OK` to save the configuration.
- `right click` the icon at system tray. Check the first item to turn on the proxy. You can chose proxy mode in the second item. It is sensible to select `PAC mode`. You can switch server in the third item.
- Download and install `firefox` brower.
- Setup `firefox` brower.
- `click` `open menu` icon at upper right => `Options` => `Network Proxy`/`Settings...` => select `Manual proxy configuration` => Set `SOCKS Host` as `127.0.0.1` and set `Port` as `1080` => check `Proxy DNS when using SOCKS v5` at the last line => `OK`.

### MacOS X
- Download the newest version [V2RayX](https://github.com/Cenmrev/V2RayX/). Go to [V2RayX-release](https://github.com/Cenmrev/V2RayX/releases), select a version and download `.app.zip` file.

- Move the `V2RayX` application to `Applications` folder and `right click` => `Open`. If you meet any permission request or something like that, enter Mac's password and click `install`/`next`. If you do not meet any problem, you will see an icon at the status bar.

- `click the icon` => `Configure...`, You will see the dialog box. Set parameters as in the following image:

![]({attach}figure/v2rayx-config-OSX-1.png)

- `click the icon` => `Servers`, select the server you configured at the last step. Finally, select `V2Ray Rules` to turn on the smart agent mode.

### IOS
Go to `App Store` and download `Kitsunebi`. Then configure the server as following images:

- **Step 1, 4, 5**:

  ![]({attach}figure/v2rayx-config-IOS-1.png)

- **Step 2**:

  ![]({attach}figure/v2rayx-config-IOS-2.png)

- **Step 3**: scan a QR code to add a server.

  ![]({attach}figure/v2rayx-config-IOS-3.png)

### Android
I do not have any Android device. But I find an active updated client for Android device, [v2rayNG](https://github.com/2dust/v2rayNG/releases), you can try it.
