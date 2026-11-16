## Aliases
Aliases are useful, if you dont want to type too much.

Adding an alias to install a package on your system:
```bash
# ~/.config/zsh/aliases:
alias ls=`ls --color`

# new alias:
alias xi=`sudo apt install -y`
```

*now you can just type xi <packagename>. to install a package - yay!*

## Keyboard Shortcuts
These are defined in you hyprland config:

Adding a shortcut to open firefox using Super + K:
```lua
-- ~/.config/hypr/hyprland.lu
...

hl.bind(mainMod .. " + K", hl.dsp.exec_cmd("firefox"))

...
```

!!! tip "Something missing?"
    If you think anything is missing, please create an [Issue](https://github.com/Nortica-Linux/nortica.org/issues/new?labels=Wiki).
