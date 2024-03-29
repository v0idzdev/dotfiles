# -*- coding: utf-8 -*-

# IMPORTS
from libqtile.command import lazy
from libqtile.utils import guess_terminal
from libqtile.config import (
    Click,
    Drag,
    Group,
    Key,
    Match,
    Screen,
)
from libqtile import (
    bar,
    layout,
    widget,
    qtile,
)

mod = "mod4"            # Set the windows key as the mod key.
terminal = "alacritty"  # Set Alacritty as the default terminal.

# KEYBINDINGS
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Bindings for the volume keys.
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
]


# GROUPS
#
# Initialise an empty list to keep groups in.
# Set the names of the groups, along with their default layout.
groups = []
group_names = [
    # ("A", {"layout": "monadtall"}),    # ♫  
    # ("B", {"layout": "monadtall"}),    # ✉
    # ("C", {"layout": "monadtall"}),    # »
    # ("D", {"layout": "monadtall"}),    # ⚒
    # ("E", {"layout": "monadtall"}),
    # ("F", {"layout": "monadtall"}), 
    # ("G", {"layout": "monadtall"}), 
    # ("H", {"layout": "monadtall"}),
    # ("I", {"layout": "monadtall"}), 
    ("➀", {"layout": "monadtall"}),
    ("➁", {"layout": "monadtall"}),
    ("➂", {"layout": "monadtall"}),
    ("➃", {"layout": "monadtall"}),
    ("➄", {"layout": "monadtall"}),
    ("➅", {"layout": "monadtall"}),
    ("➆", {"layout": "monadtall"}),
]

# Create the groups and set keybindings for switching between them,
# as well as moving windows between them.
for num_key, (name, params) in enumerate(group_names, 1):
    groups.append(Group(name, **params))

    # Number each group and bind its number to a key.
    # For instance, if "SYS" is group 3, Mod + 3 switches to it.
    keys.append(Key([mod], str(num_key), lazy.group[name].toscreen()))         # Switch to another group.
    keys.append(Key([mod, "shift"], str(num_key), lazy.window.togroup(name)))  # Send window to another group.


# LAYOUTS
# 
# Set some themes that all work the same.
# Change `theme` to one of the ones below to change the colors.  
hybrid = {
    "bar":  "1d1f21",
    "text": "c5c8c6",
    0:      "282a2e",
    1:      "a54242",
    2:      "8c9440",
    3:      "de935f",
    4:      "5f819d",
}
kasugano = {
    "bar":  "1b1b1b",
    "text": "ffffff",
    0:      "3d3d3d",
    1:      "6673bf",
    2:      "3ea290",
    3:      "b0ead9",
    4:      "31658c",
}
blue_and_black = {
    "bar":  "1c1c1c",
    "text": "ececec",
    0:      "212121",
    1:      "313131",
    2:      "414141",
    3:      "515151",
    4:      "0680da",  # Accent color
}
blue_gradient = {
    "bar":  "151515",
    "text": "fafafa",
    0:      "191919",
    1:      "282828",
    2:      "323232",
    3:      "3b3b3b",
    4:      "0841a9", # Changed from 0e4d99
}

theme = blue_gradient

# Change this to true if you'd like gaps between
# your windows.
use_gaps = True

# Define some common aesthetics and functionality that
# most layouts will have in common.
layout_defaults = {
    "border_width":  2,
    "border_focus":  theme[4],
    "border_normal": theme[3],
    "margin":        12 if use_gaps else 0, 
}

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_defaults),
]

# WIDGETS
#
# Set some default settings for widgets.
# These can be unpacked as they are passed into constructors.
widget_defaults = {
    "font":       "Ubuntu Mono Bold",
    "fontsize":   12,
    "padding":    6,
    "foreground": theme["text"],
}

# This is redundant as of now.
extension_defaults = widget_defaults.copy()


# Define some useful functions for creating widgets
# that are repeated.
def separator(background: str):
    """
    Create a separator widget to put between other widgets.

    background (str): Hexadecimal code for the background color.
    """
    return widget.Sep(
        linewidth=0,
        padding=10,
        background=background,
    )


def left_arrow(foreground: str, background: str, padding: int=-4):
    """
    Create a left-facing powerline-style arrow (◀).
    
    foreground (str): Hexadecimal code for the foreground color.
    background (str): Hexadecimal code for the background color.
    """
    return widget.TextBox(
        font="Ubuntu Mono",
        text="\u25c0",
        foreground=foreground,
        background=background,
        padding=padding,
        fontsize=37,
    )


def right_arrow(foreground: str, background: str, padding: int=-4):
    """
    Create a right-facing powerline-style arrow (◀).
    
    foreground (str): Hexadecimal code for the foreground color.
    background (str): Hexadecimal code for the background color.
    """
    return widget.TextBox(
        font="Ubuntu Mono",
        text="\u25b6",
        foreground=foreground,
        background=background,
        padding=padding,
        fontsize=37,
    )


def icon(icon: str, foreground: str, background: str):
    """
    Create an icon to be displayed in the bar.

    icon       (str): The icon to show.
    foreground (str): Hexadecimal code for the foreground color.
    background (str): Hexadecimal code for the background color.
    """
    return widget.TextBox(
        font="Ubuntu Mono",
        text=icon,
        foreground=foreground,
        background=background,
        padding=3,
        fontsize=16,
    )


# Configure the bar/panel with widgets and decorations.
# Change the colors, etc, in the above sections.
screens = [
    Screen(
        top=bar.Bar(
            [
                # Right hand side of the bar.
                separator(theme[4]),
                icon("⌦", theme["text"], theme[4]),
                widget.QuickExit(
                    default_text="[Log Out]",
                    background=theme[4],
                    **widget_defaults,
                ),
                right_arrow(theme[4], theme[3]),
                separator(theme[3]),
                icon("\u2318", theme["text"], theme[3]),
                widget.TextBox(
                    text=" Workspaces",
                    background=theme[3],
                    **widget_defaults,
                ),
                right_arrow(theme[3], theme[2]),
                separator(theme[2]),
                widget.GroupBox(
                    font="Ubuntu Mono Bold",
                    highlight_method="line",
                    highlight_color=theme[3],
                    padding_y=3,
                    margin_x=8,
                    padding_x=6,
                    borderwidth=2,
                    active=theme[4],
                    inactive=theme["text"],
                    this_current_screen_border=theme[4],
                    background=theme[2],
                    fontsize=widget_defaults["fontsize"],
                ),
                right_arrow(theme[2], theme[1]),
                separator(theme[1]),
                icon("\u2387", theme["text"], theme[1]),
                widget.CurrentLayout(
                    background=theme[1],
                    **widget_defaults,
                ),
                separator(theme[1]),
                widget.Prompt(
                    background=theme[1],
                    cursor_color=theme["text"],
                    **widget_defaults,
                ),
                right_arrow(theme[1], theme[0]),
                right_arrow(theme[0], theme["bar"]),
                separator(theme["bar"]),
                widget.WindowName(
                    **widget_defaults,
                ),
                separator(theme["bar"]),

                # Right hand side of the bar.
                # Use arrows for a powerline-style effect.
                separator(theme["bar"]),
                left_arrow(theme[0], theme["bar"], padding=-5),
                left_arrow(theme[1], theme[0]),
                icon("\u26c1", theme["text"], theme[1]),
                widget.Net(
                    interface="wlan0",
                    format="{down}↓ {up}↑",
                    background=theme[1],
                    **widget_defaults,
                ),
                separator(theme[1]),
                left_arrow(theme[2], theme[1]),
                widget.CPU(
                    format="CPU {load_percent}%",
                    background=theme[2],
                    **widget_defaults,
                ),
                widget.Memory(
                    measure_mem="G",
                    format="Mem {MemUsed: .1f}/{MemTotal: .1f}GB",
                    background=theme[2],
                    **widget_defaults,
                ),
                widget.NvidiaSensors(
                    format="GPU {perf} {temp}°C",
                    background=theme[2],
                    **widget_defaults,
                ),
                separator(theme[2]),
                left_arrow(theme[3], theme[2]),
                icon("⌨", theme["text"], theme[3]),
                widget.TextBox(
                    text="System",
                    background=theme[3],
                    **widget_defaults,
                ),
                separator(theme[3]),
                left_arrow(theme[4], theme[3]),
                icon("\u231b", theme["text"], theme[4]),
                widget.Clock(
                    format="%m/%d %H:%M",
                    background=theme[4],
                    **widget_defaults,
                ),
                separator(theme[4]),
            ],
            24,
            background=theme["bar"],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
