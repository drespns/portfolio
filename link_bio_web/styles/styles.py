from enum import Enum

import reflex as rx

# Constants:
MAX_WIDTH="600px"

# Sizes:
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.75em"
    DEFAULT = "1em"
    BIG = "2em"

# Global styles:
"""styles = {
    rx.chakra.Button
}"""

title_style = dict(
    size="lg",
    width="100%",
    padding_top=Size.DEFAULT.value,
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
)

button_subtitle_style = dict(
    font_size=Size.MEDIUM.value,
)
