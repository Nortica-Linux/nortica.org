# Configuration files

Nortica's shared desktop configuration lives in [Nortica-Linux/config](https://github.com/Nortica-Linux/config). The main repository pins it as a Git submodule and installs the checkout at `~/.local/nortica-config`.

**Keep that directory:** your dotfiles link into it.

| Location | What it controls |
| --- | --- |
| `~/.config/hypr/hyprland.lua` | Monitors, layout, keyboard, shortcuts and desktop behavior |
| `~/.config/nortica/graphics.lua` | Symlink to the selected GPU/VM profile |
| `~/.config/zsh/aliases` | Shell aliases |
| `~/.local/nortica-config/dotfiles/` | Shared Hyprland, Zsh, Alacritty, GTK and Neovim files |
| `~/.local/nortica-config/noctalia/` | Default Noctalia settings; existing user settings are preserved |
| `~/.local/state/nortica/settings.sh` | Saved graphics settings |

## Refresh the desktop configuration

Run as your **normal user**, not root:

```sh
cd ~/.local/nortica-config
git pull --ff-only
./deploy.sh
```

Check `git status` first if you have edited linked files: those changes are in the checkout too. Commit or back up your customizations before updating; do not discard them blindly.

Replaced files are backed up under `~/.local/state/nortica-config/backups/`. Set `NORTICA_SKIP_OPTIONAL_ASSETS=true` when running deployment to skip font and Zsh-plugin downloads.

System packages and services are managed by [Nortica-Linux/nortica](https://github.com/Nortica-Linux/nortica), not the config repository. See the [config README](https://github.com/Nortica-Linux/config#readme) for current deployment details.

!!! tip "Something missing?"
    Suggest a [documentation improvement](https://github.com/Nortica-Linux/nortica.org/issues/new).
