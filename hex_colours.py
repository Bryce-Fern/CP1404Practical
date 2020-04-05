colour_format = {"AliceBlue": "#f0f8ff", "aquamarine1": "#7fffd4", "purple": "#a020f0", "red1": "#ff0000", "DeepPink1": "#ff1493", "turquoise1": "#00f5ff", "SpringGreen1": "#00ff7f", "magenta": "ff00ff", "cyan1": "#00ffff", "DarkGoldenrod1": "#ffb90f", "burlywood": "#deb887", "orchid1": "#ff83fa"}

colour_hex = input("Enter colour: ")
while colour_hex != "":
    if colour_hex in colour_format:
        print(colour_hex, "hex code is", colour_format[colour_hex])
    else:
        print("Invalid Hex Colour")
    colour_hex = input("Enter colour: ")
