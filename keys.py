
from libqtile.config import Key, Drag, Click
from libqtile.lazy import lazy


keys = [
    #Special Keys
    Key([mod, "control"], "b", lazy.spawn('alacritty --hold -e python /home/max/Documents/Python/BluetoothToggle.py'), desc="Toggle Bluetooth Power On/Off"),
    Key([], 'XF86Battery', lazy.spawn('light-locker-command -l'), desc="Lock screen"),	
    Key([], '3270_PrintScreen', lazy.spawn('gnome-screenshot'), desc="Take a screenshot"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -s set 200-")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -s set +200")),
    #Application Keybindings
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "f", lazy.spawn('alacritty --hold -e ranger'), desc='Open Ranger Terminal'),
    Key([mod], "m", lazy.spawn('alacritty --hold -e cmus'), desc='Open Cmus Terminal'),
    Key([mod, "shift"], "Return", lazy.spawn('rofi -show run'), desc="Spawn a rofi run window"),
    Key([mod], "w", lazy.spawn('librewolf'), desc="Spawn a browser window"),
    #Volume Control
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture toggle")),
    Key([], "XF86AudioMute", lazy.spawn("amixer -D pulse set Master 1+ toggle")), 
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+")),
    #Float Control
    Key([mod], "space", lazy.window.toggle_floating()),
    # Switch between windows
    Key([alt], "Tab", lazy.group.next_window(), desc="Change Float Focus"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "n", lazy.layout.next(),
        desc="Move window focus to other window"),
 
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
 
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([alt], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile")

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

