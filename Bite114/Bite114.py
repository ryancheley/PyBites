import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, 'color_values.py')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/color_values.py',
    color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color.upper()
        try:
            self.rgb = COLOR_NAMES[self.color]
        except KeyError:
            self.rgb = None

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        hex = hex.lstrip('#')
        hlen = 6

        try:
            result = tuple(int(hex[i:i + int(hlen / 3)], 16) for i in range(0, hlen, int(hlen / 3)))
        except ValueError:
            raise ValueError
            pass
        return result

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        if int(rgb[0]) > 255 or int(rgb[1]) > 255 or int(rgb[2]) > 255:
            raise ValueError
        if int(rgb[0]) < 0 or int(rgb[1]) < 0 or int(rgb[2]) < 0:
            raise ValueError
        return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

    def __repr__(self):
        """Returns the repl of the object"""
        return f"{str(self.__class__.__name__)}('{self.color.lower()}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb is None:
            message = 'Unknown'
        else:
            message = str(self.rgb)
        return message