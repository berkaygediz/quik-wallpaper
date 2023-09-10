import ctypes


def set_wallpaper(path):
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)


if __name__ == "__main__":
    print("quik-wallpaper v1.0.0")
    wallpaper_path = "C:\\Users\\user\\Pictures\\wallpaper.jpg"

    if set_wallpaper(wallpaper_path) == None:
        print("Wallpaper set successfully!")
    else:
        print("Wallpaper setting failed!")
