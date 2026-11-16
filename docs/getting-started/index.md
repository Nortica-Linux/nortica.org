# Install Nortica

Nortica is built on Debian with ZFS and an optional Hyprland + Noctalia desktop.

!!! danger "Installation erases disks"
    Back up your files first. The installer formats the whole disks you select. Do not run it on your everyday workstation just to try it out; boot the live image or use a disposable VM instead.

## 1. Download and verify

Open the [Nortica releases](https://github.com/Nortica-Linux/nortica/releases/latest) page. Download every `.iso.part.*` asset for the same image, its matching `.iso.sha256` file and `REASSEMBLE.txt`.

Follow that release's `REASSEMBLE.txt`. For v1.0.0, put the downloaded files in one directory and run:

```sh
cat nortica-live-amd64-20261116T115839Z.iso.part.* > nortica-live-amd64-20261116T115839Z.iso
sha256sum -c nortica-live-amd64-20261116T115839Z.iso.sha256
```

Only proceed when the checksum reports **OK**. Do not mix parts from different releases. If a future release provides a single ISO, download it and verify its matching checksum directly.

## 2. Write the image to USB

Use an image writer to flash the verified ISO to a USB drive. This erases the USB drive too; double-check its identity and size before confirming.

On Linux, experienced users can use `dd`. First identify the USB with `lsblk`, then replace both placeholders below with the actual ISO and **whole USB device**, not a partition:

```sh
lsblk -o NAME,SIZE,MODEL,MOUNTPOINTS
# Unmount any mounted partitions on the USB before writing.
sudo dd if=/path/to/nortica-live-amd64-TIMESTAMP.iso of=/dev/YOUR_USB_DEVICE bs=4M status=progress conv=fsync
sync
```

## 3. Boot and connect

1. Boot in **x86-64 UEFI mode**, with **Secure Boot disabled**. Legacy BIOS installation is not supported.
2. Connect to the internet over Ethernet or the Noctalia Wi-Fi panel. Installation requires internet access.
3. Press **Super + D**, search for **Nortica Install**, and open it. Alternatively, run `nortica-install` from a terminal.

## 4. Configure the installation

The installer collects your choices before downloading packages or changing disks:

- Select the whole disk or disks to erase. A mirror requires two distinct disks.
- Choose swap, ZFS encryption, hostname, account and timezone.
- Choose whether to install the desktop and select a graphics profile if enabled. VM options are available too.
- Enter your account password and, if using encryption, your ZFS passphrase. Choose a passphrase you can type with ZFSBootMenu's **US keyboard layout**.
- Review the complete summary, especially the disks marked for erasure, then explicitly choose **Start installation**.

!!! note "Keyboard layouts"
    The console keyboard choice does not change the desktop's default German/Bone layout. Desktop layout settings live in `~/.config/hypr/hyprland.lua`.

Wait for the explicit success message, then reboot and remove the USB. Unlock encrypted ZFS in ZFSBootMenu and log in with your configured account. If you installed the desktop, Hyprland starts after interactive login on TTY1; exiting it returns to the shell.

## If something goes wrong

Read the failed stage and the full log under `/var/log/nortica-install/` **before rebooting**. The live system's copy includes the final pool export and cleanup; a target copy may not. Resolve any reported remaining mounts, pools or policy backups before retrying.

The [upstream installation walkthrough](https://github.com/Nortica-Linux/nortica/blob/main/step-by-step.md) has the full installer behavior, cleanup notes and instructions for running from standard Debian 13 live media.

[Report an installer issue](https://github.com/Nortica-Linux/nortica/issues/new){ .md-button }

## Building your own image

An amd64 Linux host, Docker, GNU Make, `flock` and internet access are required:

```sh
git clone --recurse-submodules https://github.com/Nortica-Linux/nortica.git
cd nortica
make iso
```

Images and checksums appear in `iso/`. See the [image build documentation](https://github.com/Nortica-Linux/nortica/tree/main/image) for configuration and caching details.
