from typing import List, Tuple

import reflex as rx

from link_bio_web.components.technology import technologies_image
from link_bio_web.states.technologies import SourceForeachState

#
icons: List[Tuple[str, str]] = [
    ("/icons/icons8-html-5-100.png", "Icono HTML"),
    ("/icons/icons8-css3-100.png", "Icono CSS"),
    ("/icons/icons/icons8-javascript-128.ico", "Icono JAVASCRIPT"),
    ("/icons/icons8-python-100.png", "Icono PYTHON"),
    ("/reflex_banner.png", "Icono REFLEX"),
    ("/icons/icons8-react-100.png", "Icono REACT"),
    ("/icons/icons8-tailwind-css-100.png", "Icono TAILWIND CSS"),
    ("/icons/icons8-tableau-software-96.png", "Icono TABLEAU"),
    ("/icons/icons8-css3-100.png", "Icono CSS"),
    ("/icons/icons8-microsoft-excel-100.png", "Icono EXCEL"),
    ("/icons/icons8-tableau-software-96.png", "Icono TABLEAU"),
    ("/icons/svg/docker-icon.svg", "Icono DOCKER"),
]

def technologies() -> rx.Component:
    return rx.flex(
        *[
            technologies_image(src, alt)
            for src, alt in icons #for ratio in [16 / 9, 3 / 2, 2 / 3, 1]
        ],
        align="center",
        justify="between",
        width="100%",
        wrap="wrap",
    )