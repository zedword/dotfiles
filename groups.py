from keys import keys
from libqtile.config import Group, Match, Key
from libqtile.lazy import lazy
from libqtile import layout

mod = "mod4"

group_names = [("", {'layout': 'columns'}),
               ("", {'layout': 'columns'}),
               ("", {'layout': 'columns'}),
               ("", {'layout': 'columns'}),
               ("", {'layout': 'columns'}),
               ("", {'layout': 'columns', 'matches':[Match(wm_class=['keepassxc'])]}),]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

def init_layout_theme():
    return {'margin':6,
            'border_width':5,
            'border_focus': '#ff79c6',
            'border_normal': '#8be9fd',
            }

layout_theme = init_layout_theme()

layouts = [
   layout.Columns(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
