# First Install

## 1. Download the Latest Release:

[https://github.com/Nortica-Linux/nortica/releases](https://github.com/Nortica-Linux/nortica/releases)

> You need the *.iso.part.* files and the checksum-file (SHA256SUMS).


## 2. Build and Verify the ISO.
```bash
# Merge ISO
cat nortica-live-amd64.iso.part.* > nortica-live-amd64.iso

# Verify checksum
sha256sum -c SHA256SUMS
```

## 3. Flash the iso to your media:
```bash
sudo dd if=/path/to/*.iso of=/dev/<your-device> status=progress && sync 

# Example:
sudo dd if=~/Downloads/nortica-live-amd64.iso /dev/sdf status=progress && sync
```

## 4. Install your new system:
1. Boot your new system from the media you installed the iso to.
2. Connect to Wifi via the Menu from the Topbar if you are not connected via Ethernet.
3. Super + D to open the App-Menu -> Search for Nortica Install
4. Walk through the interactive installer.
5. Once its finished, reboot and **enjoy your new System!**
