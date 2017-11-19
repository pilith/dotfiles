from i3pystatus import Status, get_module
from i3pystatus.updates import aptget

status = Status()

# Displays clock like this:
status.register("clock",
    format=[("%X"), ("%a %-d %b")],
    color="#c95a10",
    on_leftclick = ['scroll_format', 1],)

# Shows your CPU temperature, if you have a Intel CPU
#status.register("temp",
#    hints = {"markup": "pango"},
#    format="<span color=\"#8c16da\">{temp:.0f}</span>",
#    alert_temp = 70,
#    alert_color = "#FF0000",)


status.register("network",
    interface="enp10s0",
    format_up="  {kbs}KB/s",
    )

# Disks 
status.register("disk",
    hints = {"markup": "pango"},
    path="/",
    format="  <span color=\"#6cb87a\">{avail}G</span>",)

status.register("disk",
    hints = {"markup": "pango"},
    path="/mnt/Games/",
    format=" <span color=\"#ff850d\">{avail}G</span>",)
# Shows pulseaudio default sink volume
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    color_unmuted = "#645b9c",
    color_muted = "#FF0000",
    multi_colors = True,
    step = 3,
    format="♪{volume}",)

# Apt-Get update count
#status.register("updates", 
#    format = "Updates:{count}",
#    format_no_updates = "Up to Date",
#    backends = [aptget.AptGet()])


status.run()
