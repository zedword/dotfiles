
import os
from subprocess import CalledProcessError, Popen
from libqtile.log_utils import logger
from libqtile.widget import base
from libqtile import bar, qtile, widget
from libqtile.config import Screen

widget_defaults = dict(
    font='Font Awesome 6 Free',
    fontsize=13,
    padding=4,
)
 
extension_defaults = widget_defaults.copy()

def win_names(text):
    if text.startswith('cmus'):
        text = 'Cmus'
    elif text.endswith('— LibreWolf'):
        text = 'LibreWolf'
    elif text.endswith('— Mozilla Firefox'):
        text = "Firefox"
    elif text.endswith('Geeqie'):
        text = 'Geeqie'
    elif text.endswith('Writer'):
        text = 'Writer'
    elif text == 'kitty':
        text = 'Kitty'
    elif text == 'max@Patches:~':
        text = 'Home'
    elif text == 'max@Patches:/':
        text = 'Root'
    return text

screens = [
    Screen(
        wallpaper='/home/max/Pictures/Wallpapers/Sunshine.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.GroupBox(
                    font='Font Awesome 6 Free',
                    fontsize=22,
                    rounded=True,
                    highlight_method='text',
                    this_current_screen_border='#ff79c6',
                    block_highlight_text_color='#ff79c6',
                    active='#8be9fd',
                    highlight_color='#ff5555',
                    urgent_alert_method='text',
                    urgent_text='#ff5555',
                ),
                widget.Prompt(),
                widget.WindowName(
                    empty_group_string='Patches',
                    font='Fira Sans',
                    fontsize=14,
                    foreground='#f8f8f2',
                    max_chars=60,
                    parse_text=win_names,
                    padding=10,
                    ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
		            text='  ',
		            font='Font Awesome 6 Free', 
			        fontsize='45',
		            background='#282a36',
		            foreground='#bd93f9',
		            padding=-8,
	            ),
		       # widget.BluetoothWidget(
               #     colour_bluetooth_on='#ff5555',
               #     colour_bluetooth_off='#f8f8f2', 
               #     bluetooth_on_string="  ",
               #     bluetooth_off_string="  ",
               #     ),
                widget.CheckUpdates(
		            background='#bd93f9',
		            foreground='#f8f8f2', colour_have_updates='#ff5555',
		            colour_no_updates='#f8f8f2',
                    font='Font Awesome 6 Free',
                    fontsize='18',
		            distro='Arch_checkupdates',
                    no_update_string='  ',
                    display_format='  ',
		            mouse_callbacks = {"Button1":lambda:qtile.cmd_spawn("kitty --hold -e sudo pacman -Syu")},
                    update_interval=60,
                    padding=0,
		        ),
	            widget.TextBox(
		  	        text='  ',
		            font='Font Awesome 6 Free',
                    fontsize='18',
		            background='#bd93f9',
		            foreground='#f8f8f2',
                    padding=5,
                    mouse_callbacks={"Button1":lambda:qtile.cmd_spawn("kitty -e sudo powertop --auto-tune"), "Button2":lambda:qtile.cmd_spawn("kitty -e sudo cpupower frequency-set -g powersave"), "Button3":lambda:qtile.cmd_spawn("kitty -e sudo x86_energy_perf_policy --turbo-enable 0")}
		        ),
		        widget.TextBox(
		            text='  ',
		            font='Font Awesome 6 Free',
                    fontsize='18',
		            background='#bd93f9',
		            padding=5,
                    foreground='#f8f8f2',
		            mouse_callbacks={"Button1":lambda:qtile.cmd_spawn("kitty -e bluetoothctl power on")},
		        ),
		        widget.TextBox(
		            text='  ',
		            font='Font Awesome 6 Free',
                    fontsize='18',
		            background='#bd93f9',
		            padding=0,
                    foreground='#f8f8f2',
		            mouse_callbacks={"Button1":lambda:qtile.cmd_spawn("kitty --hold -e vim -p /home/max/.config/qtile/config.py /home/max/.config/qtile/groups.py /home/max/.config/qtile/keys.py /home/max/.config/qtile/screens.py")},
		        ),		
		        widget.TextBox(
                    text=' ',
                    font='Font Awesome 6 Free',
		            fontsize='45',
                    background='#bd93f9',
                    foreground='#ff79c6',
                    padding=-8,
                ),
                widget.TextBox(
                    text=' ',
                    font='Font Awesome 6 Free',
                    fontsize='18',
                    background="#ff79c6"
                ), 
                widget.Battery(
                    background="#ff79c6",
                    format='{percent:2.0%} {watt:.2f} W',
                    padding=0,
                ),
                widget.TextBox(
                    text= ' ',
                    font='Font Awesome 6 Free',
		            fontsize='50',
                    background='#ff79c6',
                    foreground='#bd93f9',
                    padding=-8,
                ),
                widget.TextBox(
                    text=" ",
                    font='Font Awesome 6 Free',
                    fontsize='18',
                    background='#bd93f9'
                ),
                widget.ThermalSensor(
                    background='#bd93f9',
		            update_interval=10,
                    padding=-1,
                ),
                widget.TextBox(
                    text= ' ',
                    font='Font Awesome 6 Free',
		            fontsize='50',
                    background='#bd93f9',
                    foreground='#ff79c6',
                    padding=-8,
                ),
                widget.TextBox(
                    text=' ',
                    font='Font Awesome 6 Free',
                    fontsize='18',
                    background='#ff79c6'
                ),  
                widget.Volume(
                    background='#ff79c6',
                    padding=-1,
                ),
                widget.TextBox(
                    text= ' ',
                    font='Font Awesome 6 Free',
		            fontsize='50',
                    background='#ff79c6',
                    foreground='#bd93f9',
                    padding=-8,
                ),
                widget.Clock(
                    background='#bd93f9',
                    format='%Y-%m-%d %a %I:%M %p'
                ),
                widget.TextBox(
                    text=' ',
                    font='Font Awesome 6 Free',
		            fontsize='45',
                    background='#bd93f9',
                    foreground='#ff79c6',
                    padding=-8,
                ),
                widget.QuickExit(
                    background='#ff79c6',
                    foreground='#50fa7b',
                    default_text=' ',
                    font='Font Awesome 6 Free',
                    fontsize=22,
                    countdown_format=' {} '
                )
               ],
               26,
            background='#282a36',
            margin=[3,3,0,3],
            opacity=1.0,
        ),
    ),
    Screen(
            wallpaper='/home/max/Pictures/Wallpapers/Sunshine.jpg',
            wallpaper_mode='fill',
            top=bar.Bar(
                [
                widget.GroupBox(
                    font='Font Awesome 6 Free',
                    fontsize=22,
                    rounded=True,
                    highlight_method='text',
                    this_current_screen_border='#ff79c6',
                    block_highlight_text_color='#ff79c6',
                    active='#8be9fd',
                    highlight_color='#ff5555',
                    urgent_alert_method='text',
                    urgent_text='#ff5555',
                    background='#282a36',
                ),
                widget.Prompt(
                    background='#282a36',
                    ),
                widget.WindowName(
                    empty_group_string='Patches',
                    font='Fira Sans',
                    fontsize=14,
                    foreground='#f8f8f2',
                    background='#282a36',
                    max_chars=60,
                    parse_text=win_names,
                    padding=10,
                    ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
		            text='  ',
		            font='Font Awesome 6 Free', 
			        fontsize='45',
		            background='#282a36',
		            foreground='#bd93f9',
		            padding=-8,
	            ),
		       # widget.BluetoothWidget(
               #     colour_bluetooth_on='#ff5555',
               #     colour_bluetooth_off='#f8f8f2', 
               #     bluetooth_on_string="  ",
               #     bluetooth_off_string="  ",
               #     ),
                widget.CheckUpdates(
		            background='#bd93f9',
		            foreground='#f8f8f2', colour_have_updates='#ff5555',
		            colour_no_updates='#f8f8f2',
                    font='Font Awesome 6 Free',
                    fontsize='18',
		            distro='Arch_checkupdates',
                    no_update_string='  ',
                    display_format='  ',
		            mouse_callbacks = {"Button1":lambda:qtile.cmd_spawn("kitty --hold -e sudo pacman -Syu")},
                    update_interval=60,
                    padding=0,
		        ),
	            widget.TextBox(
		  	        text='  ',
		            font='Font Awesome 6 Free',
                    fontsize='18',
		            background='#bd93f9',
		            foreground='#f8f8f2',
                    padding=5,
                    mouse_callbacks={"Button1":lambda:qtile.cmd_spawn("kitty -e sudo powertop --auto-tune"), "Button3":lambda:qtile.cmd_spawn("kitty -e sudo x86_energy_perf_policy --turbo-enable 0")}
		        ),
		        widget.TextBox(
		            text='  ',
		            font='Font Awesome 6 Free',
                    fontsize='18',
		            background='#bd93f9',
		            padding=5,
                    foreground='#f8f8f2',
		            mouse_callbacks={"Button1":lambda:qtile.cmd_spawn("kitty -e bluetoothctl power on")},
		        ),
		        widget.TextBox(
		            text='  ',
		            font='Font Awesome 6 Free',
                    fontsize='18',
		            background='#bd93f9',
		            padding=0,
                    foreground='#f8f8f2',
		            mouse_callbacks={"Button1":lambda:qtile.cmd_spawn("kitty --hold -e vim -p /home/max/.config/qtile/config.py /home/max/.config/qtile/groups.py /home/max/.config/qtile/keys.py /home/max/.config/qtile/screens.py")},
		        ),		
		        widget.TextBox(
                    text=' ',
                    font='Font Awesome 6 Free',
		            fontsize='45',
                    background='#bd93f9',
                    foreground='#ff79c6',
                    padding=-8,
                ),
                widget.TextBox(
                    text=' ',
                    font='Font Awesome 6 Free',
                    fontsize='18',
                    background="#ff79c6"
                ), 
                widget.Battery(
                    background="#ff79c6",
                    format='{percent:2.0%} {watt:.2f} W',
                    padding=0,
                ),
                widget.TextBox(
                    text= ' ',
                    font='Font Awesome 6 Free',
		            fontsize='50',
                    background='#ff79c6',
                    foreground='#bd93f9',
                    padding=-8,
                ),
                widget.TextBox(
                    text=" ",
                    font='Font Awesome 6 Free',
                    fontsize='18',
                    background='#bd93f9'
                ),
                widget.ThermalSensor(
                    background='#bd93f9',
		            update_interval=10,
                    padding=-1,
                ),
                widget.TextBox(
                    text= ' ',
                    font='Font Awesome 6 Free',
		            fontsize='50',
                    background='#bd93f9',
                    foreground='#ff79c6',
                    padding=-8,
                ),
                widget.TextBox(
                    text=' ',
                    font='Font Awesome 6 Free',
                    fontsize='18',
                    background='#ff79c6'
                ),  
                widget.Volume(
                    background='#ff79c6',
                    padding=-1,
                ),
                widget.TextBox(
                    text= ' ',
                    font='Font Awesome 6 Free',
		            fontsize='50',
                    background='#ff79c6',
                    foreground='#bd93f9',
                    padding=-8,
                ),
                widget.Clock(
                    background='#bd93f9',
                    format='%Y-%m-%d %a %I:%M %p'
                ),
                widget.TextBox(
                    text=' ',
                    font='Font Awesome 6 Free',
		            fontsize='45',
                    background='#bd93f9',
                    foreground='#ff79c6',
                    padding=-8,
                ),
                widget.QuickExit(
                    background='#ff79c6',
                    foreground='#50fa7b',
                    default_text=' ',
                    font='Font Awesome 6 Free',
                    fontsize=22,
                    countdown_format=' {} '
                )   
                ], 
                30),
            ),
]
