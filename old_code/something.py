monitor_size = 200
crosshair_x = 2250
crosshair_y = 1519


monitor = {
    "top": crosshair_y - monitor_size // 2,
    "left": crosshair_x - monitor_size // 2,
    "width": monitor_size,
    "height":monitor_size
}
center_point = (monitor['width'] // 2, monitor['height'] // 2)
cx, cy = center_point

print(cx)
print(cy)