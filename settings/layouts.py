from libqtile import layout
from settings.theme import colors
from libqtile.config import Match


layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 4
}

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    layout.MonadTall(**layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.Bsp(**layout_conf),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.RatioTile(**layout_conf),
]

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
    ], border_focus=colors["color4"][0]
)
