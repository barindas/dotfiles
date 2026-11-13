import os
import random

WALL_DIR = '/home/barindas/.config/hypr/wallpapers/'
CONFIG_DIR = '/home/barindas/.config/hypr/hyprpaper.conf'

walls = [
    os.path.join(WALL_DIR, f)
    for f in os.listdir(WALL_DIR)
    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))
]

if __name__ == '__main__':
    if not walls:
        raise SystemExit(f"No wallpapers found in {WALL_DIR}")

    curr_wall = random.choice(walls)

    with open(CONFIG_DIR, 'w', encoding='UTF-8') as config:
        config.write(
            "wallpaper {\n"
            "    monitor = DP-1\n"
            f"    path = {curr_wall}\n"
            "    fit_mode = contain\n"
            "}\n"
        )

    os.system('kill hyprpaper & hyprpaper')
