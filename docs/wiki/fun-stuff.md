# Fun Stuff
Stuff you may want to install for entertainment purpouses.

## Flatpaks

You **could** download the .deb files or compile it yourself, but you will have to redownload/compile and run it every time there is an update. We probably dont want that.

For some programs, there is not even much of a choice. Thats why will use Flatpaks for this.

```bash
# setup flatpak (if not already installed)
sudo apt install flatpak

# add their repo
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# do this to update your Flatpaks:
flatpak update
```
In order for the launcher to find flatpak applications, you have to add this line on top of your `~/.zprofile`:
```bash
export XDG_DATA_DIRS="/var/lib/flatpak/exports/share:$HOME/.local/share/flatpak/exports/share:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"
```


### Discord
```bash
flatpak install flathub com.discordapp.Discord
```

### Spotify
```bash
flatpak install flathub com.spotify.Client
```


!!! tip "Something missing?"
    If you think anything is missing, please create an [Issue](https://github.com/Nortica-Linux/nortica.org/issues/new?labels=Wiki).
