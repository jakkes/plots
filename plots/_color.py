from enum import Enum
from typing import List, Sequence

import matplotlib


class Color(str, Enum):
    """Set of predefined colors."""

    MATPLOT_BLUE = "#1f77b4"
    """Classic blue color of matplotlib."""

    MATPLOT_ORANGE = "#ff7f0e"
    """Classic orange color of matplotlib."""

    MATPLOT_GREEN = "#2ca02c"
    """Classic green color of matplotlib."""

    MATPLOT_RED = "#d62728"
    """Classic red color of matplotlib."""

    MATPLOT_PURPLE = "#9467bd"
    """Classic red color of matplotlib."""

    MATPLOT_BROWN = "#8c564b"
    """Classic brown color of matplotlib."""

    MATPLOT_PINK = "#e377c2"
    """Classic pink color of matplotlib."""

    MATPLOT_GRAY = "#7f7f7f"
    """Classic gray color of matplotlib."""

    MATPLOT_OLIVE = "#bcbd22"
    """Classic olive color of matplotlib."""

    MATPLOT_CYAN = "#17becf"
    """Classic cyan color of matplotlib."""

    ALICE_BLUE = "#f0f8ff"
    ANTIQUEWHITE = "#faebd7"
    AQUA = "#00ffff"
    AQUAMARINE = "#7fffd4"
    AZURE = "#f0ffff"
    BEIGE = "#f5f5dc"
    BISQUE = "#ffe4c4"
    BLACK = "#000000"
    BLANCHED_ALMOND = "#ffebcd"
    BLUE = "#0000ff"
    BLUE_VIOLET = "#8a2be2"
    BROWN = "#a52a2a"
    BURLYWOOD = "#deb887"
    CADET_BLUE = "#5f9ea0"
    CHARTREUSE = "#7fff00"
    CHOCOLATE = "#d2691e"
    CORAL = "#ff7f50"
    CORNFLOWER_BLUE = "#6495ed"
    CORNSILK = "#fff8dc"
    CRIMSON = "#dc143c"
    CYAN = "#00ffff"
    DARK_BLUE = "#00008b"
    DARK_CYAN = "#008b8b"
    DARK_GOLDEN_ROD = "#b8860b"
    DARK_GRAY = "#a9a9a9"
    DARK_GREY = "#a9a9a9"
    DARK_GREEN = "#006400"
    DARK_KHAKI = "#bdb76b"
    DARK_MAGENTA = "#8b008b"
    DARK_OLIVE_GREEN = "#556b2f"
    DARK_ORANGE = "#ff8c00"
    DARK_ORCHID = "#9932cc"
    DARK_RED = "#8b0000"
    DARK_SALMON = "#e9967a"
    DARK_SEA_GREEN = "#8fbc8f"
    DARK_SLATE_BLUE = "#483d8b"
    DARK_SLATE_GRAY = "#2f4f4f"
    DARK_SLATE_GREY = "#2f4f4f"
    DARK_TURQUOISE = "#00ced1"
    DARK_VIOLET = "#9400d3"
    DEEP_PINK = "#ff1493"
    DEEP_SKY_BLUE = "#00bfff"
    DIM_GRAY = "#696969"
    DIM_GREY = "#696969"
    DODGER_BLUE = "#1e90ff"
    FIRE_BRICK = "#b22222"
    FLORALWHITE = "#fffaf0"
    FOREST_GREEN = "#228b22"
    FUCHSIA = "#ff00ff"
    GAINSBORO = "#dcdcdc"
    GHOSTWHITE = "#f8f8ff"
    GOLD = "#ffd700"
    GOLDEN_ROD = "#daa520"
    GRAY = "#808080"
    GREY = "#808080"
    GREEN = "#008000"
    GREEN_YELLOW = "#adff2f"
    HONEY_DEW = "#f0fff0"
    HOT_PINK = "#ff69b4"
    INDIAN_RED = "#cd5c5c"
    INDIGO = "#4b0082"
    IVORY = "#fffff0"
    KHAKI = "#f0e68c"
    LAVENDER = "#e6e6fa"
    LAVENDER_BLUSH = "#fff0f5"
    LAWN_GREEN = "#7cfc00"
    LEMON_CHIFFON = "#fffacd"
    LIGHT_BLUE = "#add8e6"
    LIGHT_CORAL = "#f08080"
    LIGHT_CYAN = "#e0ffff"
    LIGHT_GOLDEN_ROD_YELLOW = "#fafad2"
    LIGHT_GRAY = "#d3d3d3"
    LIGHT_GREY = "#d3d3d3"
    LIGHT_GREEN = "#90ee90"
    LIGHT_PINK = "#ffb6c1"
    LIGHT_SALMON = "#ffa07a"
    LIGHT_SEA_GREEN = "#20b2aa"
    LIGHT_SKY_BLUE = "#87cefa"
    LIGHT_SLATE_GRAY = "#778899"
    LIGHT_SLATE_GREY = "#778899"
    LIGHT_STEEL_BLUE = "#b0c4de"
    LIGHT_YELLOW = "#ffffe0"
    LIME = "#00ff00"
    LIME_GREEN = "#32cd32"
    LINEN = "#faf0e6"
    MAGENTA = "#ff00ff"
    MAROON = "#800000"
    MEDIUM_AQUA_MARINE = "#66cdaa"
    MEDIUM_BLUE = "#0000cd"
    MEDIUM_ORCHID = "#ba55d3"
    MEDIUM_PURPLE = "#9370db"
    MEDIUM_SEA_GREEN = "#3cb371"
    MEDIUM_SLATE_BLUE = "#7b68ee"
    MEDIUM_SPRING_GREEN = "#00fa9a"
    MEDIUM_TURQUOISE = "#48d1cc"
    MEDIUM_VIOLET_RED = "#c71585"
    MIDNIGHT_BLUE = "#191970"
    MINT_CREAM = "#f5fffa"
    MISTY_ROSE = "#ffe4e1"
    MOCCASIN = "#ffe4b5"
    NAVAJOWHITE = "#ffdead"
    NAVY = "#000080"
    OLD_LACE = "#fdf5e6"
    OLIVE = "#808000"
    OLIVE_DRAB = "#6b8e23"
    ORANGE = "#ffa500"
    ORANGE_RED = "#ff4500"
    ORCHID = "#da70d6"
    PALE_GOLDEN_ROD = "#eee8aa"
    PALE_GREEN = "#98fb98"
    PALE_TURQUOISE = "#afeeee"
    PALE_VIOLET_RED = "#db7093"
    PAPAYAWHIP = "#ffefd5"
    PEACH_PUFF = "#ffdab9"
    PERU = "#cd853f"
    PINK = "#ffc0cb"
    PLUM = "#dda0dd"
    POWDER_BLUE = "#b0e0e6"
    PURPLE = "#800080"
    REBECCA_PURPLE = "#663399"
    RED = "#ff0000"
    ROSY_BROWN = "#bc8f8f"
    ROYAL_BLUE = "#4169e1"
    SADDLE_BROWN = "#8b4513"
    SALMON = "#fa8072"
    SANDY_BROWN = "#f4a460"
    SEA_GREEN = "#2e8b57"
    SEA_SHELL = "#fff5ee"
    SIENNA = "#a0522d"
    SILVER = "#c0c0c0"
    SKY_BLUE = "#87ceeb"
    SLATE_BLUE = "#6a5acd"
    SLATE_GRAY = "#708090"
    SLATE_GREY = "#708090"
    SNOW = "#fffafa"
    SPRING_GREEN = "#00ff7f"
    STEEL_BLUE = "#4682b4"
    TAN = "#d2b48c"
    TEAL = "#008080"
    THISTLE = "#d8bfd8"
    TOMATO = "#ff6347"
    TURQUOISE = "#40e0d0"
    VIOLET = "#ee82ee"
    WHEAT = "#f5deb3"
    WHITE = "#ffffff"
    WHITE_SMOKE = "#f5f5f5"
    YELLOW = "#ffff00"
    YELLOW_GREEN = "#9acd32"

    @staticmethod
    def get_default_color_cycle() -> List[str]:
        """Returns the default color cycle used in plots.

        Returns:
            List[str]: List of hex color codes.
        """
        return [x["color"] for x in matplotlib.rcParams["axes.prop_cycle"]]

    @staticmethod
    def set_default_color_cycle(colors: Sequence[str]):
        """Sets the default color cycle used in plots.

        Args:
            colors (Sequence[str]): Sequence of hex color codes.
        """
        matplotlib.rcParams["axes.prop_cycle"] = list(colors)
