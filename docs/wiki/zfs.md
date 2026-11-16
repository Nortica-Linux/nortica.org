# Using ZFS

## General health and status

### Get zpool status
```bash
# Get Status of whole Zpool and its mirror (if configured)
zpool status
```
```
[user@Host ~]$ zpool status
  pool: zroot
 state: ONLINE
  scan: scrub repaired 0B in 00:02:38 with 0 errors on Mon Oct 19 00:29:47 2026
config:

	NAME                                      STATE     READ WRITE CKSUM
	zroot                                     ONLINE       0     0     0
	  mirror-0                                ONLINE       0     0     0
	    8357462e-be8f-45cf-8031-b70e8afe3c75  ONLINE       0     0     0
	    e2fea235-edab-43b5-a67b-91940c00ac18  ONLINE       0     0     0

errors: No known data errors
```
---
```bash
# Get status of defined zfs-volumes:
zfs list
```
```
[user@Host ~]$ zfs list
NAME                USED  AVAIL  REFER  MOUNTPOINT
zroot              70.3G   391G   192K  none
zroot/ISOs         5.58G  44.4G  5.58G  /opt/VMM/ISOs
zroot/ROOT         13.4G   391G   192K  none
zroot/ROOT/debian  13.4G   391G  9.77G  /
zroot/VMs          32.5G  67.5G  32.5G  /opt/VMM/VMs
zroot/docker        178M  49.8G   178M  /opt/docker
zroot/home         18.5G   181G  16.9G  /home
```


## Create and use new volumes
> Todo:

## Snapshots
```bash
# list snapshots
zfs list -t snapshot
```
```
[user@Host ~]$ zfs list -t snapshot
NAME                                    USED  AVAIL  REFER  MOUNTPOINT
zroot/ROOT/debian@auto-daily-20260926  20.7M      -  6.48G  -
zroot/ROOT/debian@auto-daily-20260928  15.2M      -  6.50G  -
zroot/ROOT/debian@auto-daily-20260930   161M      -  8.00G  -
zroot/ROOT/debian@auto-daily-20261002  18.7M      -  9.44G  -
zroot/ROOT/debian@auto-daily-20261004  20.6M      -  9.45G  -
zroot/ROOT/debian@auto-daily-20261006  24.9M      -  9.04G  -
zroot/ROOT/debian@auto-daily-20261008  27.1M      -  9.06G  -
zroot/ROOT/debian@auto-daily-20261010  18.9M      -  9.18G  -
zroot/ROOT/debian@auto-daily-20261012  21.2M      -  9.19G  -
zroot/ROOT/debian@auto-daily-20261014  37.2M      -  9.21G  -
zroot/ROOT/debian@auto-daily-20261016  38.6M      -  9.22G  -
zroot/ROOT/debian@auto-daily-20261018  54.2M      -  9.24G  -
zroot/ROOT/debian@auto-daily-20261020  22.3M      -  9.25G  -
zroot/ROOT/debian@auto-daily-20261022  24.6M      -  9.27G  -
zroot/home@auto-60min-20261022-0746     180M      -  16.2G  -
zroot/home@auto-60min-20261022-0946    50.6M      -  16.3G  -
zroot/home@auto-60min-20261022-1146    42.8M      -  16.4G  -
zroot/home@auto-60min-20261022-1346    36.8M      -  16.4G  -
zroot/home@auto-60min-20261022-1546    34.6M      -  16.5G  -
zroot/home@auto-60min-20261022-1746    17.1M      -  16.6G  -
zroot/home@auto-60min-20261022-1946    15.8M      -  16.6G  -
zroot/home@auto-60min-20261022-2146    16.3M      -  16.7G  -
zroot/home@auto-60min-20261022-2346    15.2M      -  16.8G  -
zroot/home@auto-60min-20261023-0146    15.7M      -  16.8G  -
zroot/home@auto-15min-20261023-0315    11.1M      -  16.9G  -
zroot/home@auto-15min-20261023-0345    3.88M      -  16.9G  -
zroot/home@auto-60min-20261023-0346    3.95M      -  16.9G  -
zroot/home@auto-15min-20261023-0415    10.1M      -  16.9G  -
zroot/home@auto-15min-20261023-0445    11.0M      -  16.9G  -
zroot/home@auto-15min-20261023-0515    10.4M      -  16.9G  -
zroot/home@auto-15min-20261023-0545    3.77M      -  16.9G  -
zroot/home@auto-60min-20261023-0546    3.84M      -  16.9G  -
zroot/home@auto-15min-20261023-0615    11.2M      -  16.9G  -
zroot/home@auto-15min-20261023-0645    16.3M      -  16.9G  -
```
---
In order to browse snapshots, just go to the hidden .zfs folder in the root of the volume:
```bash
[user@Host ~]$ ls /home/.zfs/snapshot
auto-15min-20261023-0315  auto-60min-20261022-1146
auto-15min-20261023-0345  auto-60min-20261022-1346
auto-15min-20261023-0415  auto-60min-20261022-1546
auto-15min-20261023-0445  auto-60min-20261022-1746
auto-15min-20261023-0515  auto-60min-20261022-1946
auto-15min-20261023-0545  auto-60min-20261022-2146
auto-15min-20261023-0615  auto-60min-20261022-2346
auto-15min-20261023-0645  auto-60min-20261023-0146
auto-60min-20261022-0746  auto-60min-20261023-0346
auto-60min-20261022-0946  auto-60min-20261023-0546
```
These contain the state of their volume from their respective dates+times.

This allows for easy restore of files.

### zfs-autosnap
Check if its running:
```bash
# Check if its running:
sudo sysemctl status zfs-autosnap

● zfs-autosnap.service - ZFS autosnapshot daemon
     Loaded: loaded (/etc/systemd/system/zfs-autosnap.service; enabled; preset: enabled)
     Active: active (running) since Wed 2026-09-02 13:45:05 CEST; 1 month 20 days ago
 Invocation: 25386333174d487f8fa62c57ef1848f2
   Main PID: 1006 (zfs-autosnap.sh)
      Tasks: 7 (limit: 38287)
     Memory: 1.9M (peak: 5.4M)
        CPU: 4min 57.116s
     CGroup: /system.slice/zfs-autosnap.service
             ├─   1006 /bin/sh /usr/local/bin/zfs-autosnap.sh
             ├─   1097 /bin/sh /usr/local/bin/zfs-autosnap.sh
             ├─   1167 /bin/sh /usr/local/bin/zfs-autosnap.sh
             ├─   1217 /bin/sh /usr/local/bin/zfs-autosnap.sh
             ├─1170883 sleep 172799
             ├─1917337 sleep 7200
             └─1940668 sleep 1800

Oct 23 05:46:46 PC330152 zfs-autosnap.sh[1217]: [INFO] 60min-home cycle done
Oct 23 05:46:46 PC330152 zfs-autosnap.sh[1217]: [INFO] 60min-home waiting 7200s
Oct 23 06:15:00 PC330152 zfs-autosnap.sh[1167]: [INFO] 15min-home snapshot zroot/home@aut>
Oct 23 06:15:00 PC330152 zfs-autosnap.sh[1167]: [INFO] 15min-home prune keep=8
Oct 23 06:15:00 PC330152 zfs-autosnap.sh[1167]: [INFO] 15min-home cycle done
Oct 23 06:15:00 PC330152 zfs-autosnap.sh[1167]: [INFO] 15min-home waiting 1800s
Oct 23 06:45:00 PC330152 zfs-autosnap.sh[1167]: [INFO] 15min-home snapshot zroot/home@aut>
Oct 23 06:45:00 PC330152 zfs-autosnap.sh[1167]: [INFO] 15min-home prune keep=8
Oct 23 06:45:00 PC330152 zfs-autosnap.sh[1167]: [INFO] 15min-home cycle done
Oct 23 06:45:00 PC330152 zfs-autosnap.sh[1167]: [INFO] 15min-home waiting 1800s
```

### Configuring zfs-autosnap
just edit `/etc/zfs-autosnap/jobs.conf` accordingly:

```bash
[user@Host ~]$ cat /etc/zfs-autosnap/jobs.conf
# name|dataset|label|schedule|keep|slack|flags
daily-root|zroot/ROOT/debian|auto-daily-$(%Y%m%d)|-H0 -M0|14|1d|r
15min-home|zroot/home|auto-15min-$(%Y%m%d-%H%M)|-H* -M/15|8|15min|-
60min-home|zroot/home|auto-60min-$(%Y%m%d-%H%M)|-H* -M0|12|1h|-
```


!!! tip "Something missing?"
    If you think anything is missing, please create an [Issue](https://github.com/Nortica-Linux/nortica.org/issues/new?labels=Wiki).
