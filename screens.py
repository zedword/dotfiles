from libqtile import bar, qtile, widget
from libqtile.config import Screen

widget_defaults = dict(
    font='Fira Sans Condensed',
    fontsize=12,
    padding=3,
)

extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        wallpaper='/home/max/Pictures/Wallpapers/Sunshine.jpg',
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=20,
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
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
		            text='',
		            fontsize='64',
		            background='#282a36',
		            foreground='#bd93f9',
		            padding=-2,
	            ),
		        widget.CheckUpdates(
		            background='#bd93f9',
		            foreground='#f8f8f2',
		            colour_have_updates='#ff5555',
		            colour_no_updates='#f8f8f2',
		            fontsize='18',
		            distro='Arch',
                    no_update_string='  ',
                    display_format='  ',
		            mouse_callbacks = {"Button1":lambda:qtile.cmd_spawn("alacritty --hold -e sudo pacman -Syu")},
		            padding=-2,
                    update_interval=60
		        ),
		        widget.TextBox(
		            text='  ',
		            fontsize='18',
		            background='#bd93f9',
		            foreground='#f8f8f2',
		            mouse_callbacks={"Button1":lambda:qtile.cmd_spawn("alacritty -e sudo powertop --auto-tune")},
		        ),
		        widget.TextBox(
		            text='  ',
		            fontsize='18',
		            background='#bd93f9',
		            foreground='#f8f8f2',
		            mouse_callbacks={"Button1":lambda:qtile.cmd_spawn("alacritty -e bluetoothctl power on")},
		        ),
		        widget.TextBox(
		            text='  ',
		            fontsize='18',
		            background='#bd93f9',
		            foreground='#f8f8f2',
		            mouse_callbacks={"Button1":lambda:qtile.cmd_spawn("alacritty --hold -e vim /home/max/.config/qtile/config.py")},
		        ),		
		        widget.TextBox(
                    text='',
                    fontsize='50',
                    background='#bd93f9',
                    foreground='#ff79c6',
                    padding=-2,
                ),
                widget.TextBox(
                    text=' ',
                    fontsize='18',
                    background="#ff79c6"
                ),
                widget.Battery(
                    background="#ff79c6",
                    format='{percent:2.0%} {watt:.2f} W'
                ),
                widget.TextBox(
                    text= '',
                    fontsize='50',
                    background='#ff79c6',
                    foreground='#bd93f9',
                    padding=-2,
                ),
                widget.TextBox(
                    text="",
                    fontsize='18',
                    background='#bd93f9'
                ),
                widget.ThermalSensor(
                    background='#bd93f9',
		            update_interval=10,
                    padding=5,
                ),
                widget.TextBox(
                    text= '',
                    fontsize='50',
                    background='#bd93f9',
                    foreground='#ff79c6',
                    padding=-2,
                ),
                widget.TextBox(
                    text=' ',
                    fontsize='18',
                    background='#ff79c6'
                ),
                widget.Volume(
                    background='#ff79c6',
                ),
                widget.TextBox(
                    text= '',
                    fontsize='50',
                    background='#ff79c6',
                    foreground='#bd93f9',
                    padding=-2,
                ),
                widget.Clock(
                    background='#bd93f9',
                    format='%Y-%m-%d %a %I:%M %p'),
                widget.TextBox(
                    text='',
                    fontsize='48',
                    background='#bd93f9',
                    foreground='#ff79c6',
                    padding=-2
                ),
                widget.QuickExit(
                    background='#ff79c6',
                    foreground='#50fa7b',
                    default_text=' ',
                    fontsize=24,
                    countdown_format='({})'
                )
               ],
            32,
            background='#282a36',
            margin=[3,3,0,3],
            opacity=.8,
        ),
    ),
]
