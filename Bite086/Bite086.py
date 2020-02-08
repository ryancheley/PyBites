def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    if r > 255 or g > 255 or b > 255:
        raise ValueError
    r_hex = hex(r).replace('0x', '').ljust(2, '0').upper()
    g_hex = hex(g).replace('0x', '').ljust(2, '0').upper()
    b_hex = hex(b).replace('0x', '').ljust(2, '0').upper()
    result = '#'+r_hex+g_hex+b_hex

    return result

r = rgb_to_hex((192, 192, 192))
print(r)