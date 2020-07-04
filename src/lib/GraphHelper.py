from random import randint

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
colors = (
    "#5b9bd5",
    "#ed7d31",
    "#a4a4a4",
    "#fdc131",
    "#4472c4",
    "#70ad46",
    "#255e91",
    "#9e4919",
    "#636363",
    "#99731a",
    "#264478",
    "#43682b",
    "#7cafdd",
    "#f1965a",
    "#b7b7b7",
    "#ffcd33",
    "#698ed0",
    "#8cc168",
    "#327dc2",
    "#d26025",
    "#848484",
    "#cc9a26",
    "#335aa1",
    "#598a39",
    "#9dc3e6",
    "#9dc3e6",
    "#c9c9c9",
    "#ffd966",
    "#8eaadc",
    "#a9d18e",
    "#1f4e79",
    "#843c13",
    "#525252",
    "#7f6013",
    "#203864",
    "#385723",
    "#8cb9e2",
    "#f2a46e",
    "#bfc0bf",
    "#ffd34d",
    "#bfc0bf",
    "#ffd34d",
    "#7c9cd6",
    "#9ac97a",
    "#2b6da9",
)
markers = (".", "v", "^", "<", ">", "8", "s", "P", "*", "+", "D", "d")


def rand_marker():
    n = randint(0, len(markers) - 1)
    return markers[n]


def rand_pattern():
    n = randint(0, len(patterns) - 1)
    return patterns[n]


def rand_color():
    n = randint(0, len(colors) - 1)
    return colors[n]


def normalize(value, min_value, max_value, range_values):
    return (range_values[1] - range_values[0]) * (
        (value - min_value)
        / (1 if max_value - min_value == 0 else max_value - min_value)
    ) + range_values[0]
