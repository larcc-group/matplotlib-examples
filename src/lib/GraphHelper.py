patterns = (
    "\\\\\\\\",
    "x",
    "////",
    "+",
    "||",
    ".",
    "//",
    "\\\\",
    "-",
    "||||",
    "|",
    "/",
    "\\",
)
markers = (".", "v", "^", "<", ">", "8", "s", "P", "*", "+", "D", "d")


def get_marker(index):
    index = index % len(markers)
    return markers[index]


def get_pattern(index):
    index = index % len(patterns)
    return patterns[index]
