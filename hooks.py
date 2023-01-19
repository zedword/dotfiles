

import os 
import subprocess

from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('/home/max/.config/qtile/autostart.sh')
    subprocess.run([home])
