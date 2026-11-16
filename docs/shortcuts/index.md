---
hide:
  - toc
---

# Keyboard shortcuts

These defaults come from [Nortica's Hyprland configuration](https://github.com/Nortica-Linux/config/blob/main/dotfiles/hypr/hyprland.lua). Customize them in `~/.config/hypr/hyprland.lua`; see [configuration files](../wiki/config-files.md) before updating linked dotfiles.

Each monitor has ten workspaces. Number keys select workspaces on the focused monitor; **0** means the tenth workspace. **Super + mouse wheel** cycles through them, and **Super + .** focuses the next monitor.

<div class="shortcut-grid">

  <section class="shortcut-card">
    <div class="shortcut-eyebrow">01</div>
    <h2>Applications</h2>

    <dl>
      <div class="shortcut-row">
        <dt>Open Alacritty</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>Return</kbd></span>
        </dd>
      </div>
      <div class="shortcut-row">
        <dt>Open Thunar</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>E</kbd></span>
        </dd>
      </div>
      <div class="shortcut-row">
        <dt>Find and launch an app</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>D</kbd></span>
        </dd>
      </div>
    </dl>
  </section>

  <section class="shortcut-card">
    <div class="shortcut-eyebrow">02</div>
    <h2>Workspaces</h2>

    <dl>
      <div class="shortcut-row">
        <dt>Switch workspace</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>1–9, 0</kbd></span>
        </dd>
      </div>
      <div class="shortcut-row">
        <dt>Move the active window to a workspace</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>Shift</kbd><span class="shortcut-plus">+</span><kbd>1–9, 0</kbd></span>
        </dd>
      </div>
    </dl>
  </section>

  <section class="shortcut-card">
    <div class="shortcut-eyebrow">03</div>
    <h2>Windows</h2>

    <dl>
      <div class="shortcut-row">
        <dt>Focus another window</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>Arrow keys</kbd></span>
        </dd>
      </div>
      <div class="shortcut-row">
        <dt>Swap windows</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>Shift</kbd><span class="shortcut-plus">+</span><kbd>Arrow keys</kbd></span>
        </dd>
      </div>
      <div class="shortcut-row">
        <dt>Adjust the master-area width</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>Ctrl</kbd><span class="shortcut-plus">+</span><kbd>Left / Right</kbd></span>
        </dd>
      </div>
      <div class="shortcut-row">
        <dt>Toggle fullscreen</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>F</kbd></span>
        </dd>
      </div>
      <div class="shortcut-row">
        <dt>Toggle floating mode</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>V</kbd></span>
        </dd>
        <p class="shortcut-caution">Use the mouse shortcuts to resize and move.</p>
      </div>
      <div class="shortcut-row">
        <dt>Close the active application</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>Q</kbd></span>
        </dd>
      </div>
    </dl>
  </section>

  <section class="shortcut-card">
    <div class="shortcut-eyebrow">04</div>
    <h2>Mouse</h2>

    <dl>
      <div class="shortcut-row">
        <dt>Move a window</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>Left drag</kbd></span>
        </dd>
      </div>
      <div class="shortcut-row">
        <dt>Resize a window</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>Right drag</kbd></span>
        </dd>
      </div>
    </dl>
  </section>

  <section class="shortcut-card">
    <div class="shortcut-eyebrow">05</div>
    <h2>Session</h2>

    <dl>
      <div class="shortcut-row">
        <dt>Lock your screen</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>L</kbd></span>
        </dd>
      </div>
      <div class="shortcut-row">
        <dt>Exit Hyprland</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>M</kbd></span>
        </dd>
      </div>
    </dl>

    <p class="shortcut-caution">Exits immediately without a confirmation dialog. Save your work first.</p>
  </section>

  <section class="shortcut-card">
    <div class="shortcut-eyebrow">06</div>
    <h2>Screenshots</h2>

    <dl>
      <div class="shortcut-row">
        <dt>Take a screenshot of a selection</dt>
        <dd>
          <span class="shortcut-keys"><kbd>Super</kbd><span class="shortcut-plus">+</span><kbd>Shift</kbd><span class="shortcut-plus">+</span><kbd>S</kbd></span>
        </dd>
        <p class="shortcut-caution">The screenshot is saved to your clipboard.</p>
      </div>
    </dl>
  </section>

</div>
