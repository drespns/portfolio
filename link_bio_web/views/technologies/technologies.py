from typing import List

import reflex as rx


class SourceForeachState(rx.State):
    src: List[str] = [
        "/icons/icons8-css3-100.png",
        "/icons/icons8-css3-100.png",
        "/icons/icons8-css3-100.png",
        "/icons/icons8-css3-100.png",
        "/icons/icons8-css3-100.png",
        "/icons/icons8-css3-100.png",
        "/icons/icons8-css3-100.png",
        "/icons/icons8-css3-100.png",
        "/icons/icons8-css3-100.png",
    ]
#

def tech_image(src: str) -> rx.Component:
    return rx.image(
        src=src,
        width="100px",
        height="100px",
        border_radius="50%",
        border="5px solid #555",
    )
#
def technologies() -> rx.Component:
    return rx.grid(
        rx.foreach(
            SourceForeachState.src,
            tech_image,
        ),
        rows="3",
        spacing="4",
        align="center",
        justify="center"
    )