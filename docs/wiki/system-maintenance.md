## Changing your package mirrors:
A mirror is the location, your system downloads packages from.
> A bad mirror can result in slow package downloads.

A list of available, public mirrors can be found here:
> [https://www.debian.org/mirror/list](https://www.debian.org/mirror/list)

I recommend you choose a trusted mirror close to you:
```bash
# /etc/apt/sources.list

deb http://debian.lagis.at/debian trixie main contrib non-free non-free-firmware
deb http://debian.lagis.at/debian trixie-updates main contrib non-free-firmware
deb http://security.debian.org/debian-security trixie-security main contrib non-free non-free-firmware
```
> replace the 3 existing lines, dont just append these new ones.

Once you replaced these 3 deb.. lines inside of your  `/etc/apt/sources.list`, run:
```bash
sudo apt update && sudo apt upgrade
```

!!! tip "Something missing?"
    If you think anything is missing, please create an [Issue](https://github.com/Nortica-Linux/nortica.org/issues/new).
