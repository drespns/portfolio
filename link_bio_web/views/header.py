import reflex as rx

from link_bio_web.components.description import description
from link_bio_web.components.info_text import info_text
from link_bio_web.components.link_icon import link_icon

from link_bio_web.styles import styles

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src="/hasbulla.jpg",
                name="Daniel Rodriguez", # -> DR (fallback)
                size="9",
            ),
            rx.vstack(
                rx.vstack(
                    rx.heading("Daniel Rodriguez Espinosa".upper(), size="5"),
                    rx.text("@8gofio", margin_top=styles.Size.ZERO.value),
                    spacing="0"
                ),
                rx.hstack(
                    link_icon("github", "https://github.com"),
                    link_icon("linkedin", "https://github.com"),
                    link_icon("youtube", "https://youtube.com"),
                    spacing="1",
                ),
                align="start",
                justify="between",
                width="100%",
                #spacing=""
            ),
            spacing="2",
            align="center",
            justify="start"
        ),
        rx.flex(
            info_text("+13", "años de experiencia"),
            #rx.spacer(),
            info_text("+13", "Experiencia"),
            #rx.spacer(),
            info_text("+13", "Experiencia"),
            #rx.spacer(),
            justify="between",
            width="100%"
        ),
        description(),
        align="center",
        justify="center",
        min_height="35vh",
        width="100%",
    )