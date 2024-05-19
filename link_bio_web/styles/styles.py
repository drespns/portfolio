from enum import Enum

import reflex as rx

from .colors import Color, TextColor


# Sizes:
class Size(Enum):
    ZERO = "0 !important"
    SMALL = "0.5em" # 1em <- tamaño fuente de la app.
    MEDIUM = "0.75em"
    DEFAULT = "1em"
    BIG = "1.5em"
    VERY_BIG = "2em"
    ULTRA_BIG = "2.5em"
    HUMONGOUS = "3em"
    GARGANTUAN = "3em"


# Constants:
MAX_WIDTH="600px"

# Global styles:
BASE_STYLE = { # NOTE: solo se toman de aquí las propiedades CSS.
    "background_color": Color.BACKGROUND.value,
    rx.avatar: {
        #"size": "8",
        #fallback='DR',
        # high_contrast=True,
        # variant='solid',
        #"radius":"full",
        "border":"5px solid",
        "border_color": Color.SECONDARY.value,
        "box_shadow": f"{Color.SHADOW.value} 0 5px 5px"
    },
    rx.button: {
        "background_color": Color.CONTENT.value,
        "color": TextColor.HEADER.value,
        "width": "100%",
        "height": "100%",
        "cursor": "pointer",

        "_hover": {
            "background_color": Color.SECONDARY.value,
        }
    },
    rx.link: {
        "_hover": {
            "border_color": Color.SHADOW.value,
        }
    },
    rx.box: {
        "color": TextColor.BODY.value,
        "font_size": Size.MEDIUM.value
    },
    rx.text: {
        "color": TextColor.BODY.value
    }
}

# Other styles:

title_style = dict(
    size="lg",
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value
)

button_subtitle_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
)
