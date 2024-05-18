import reflex as rx

from link_bio_web.styles import styles

def link_button(title:str, subtitle:str, url:str, color_scheme:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon("heart"),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(subtitle, style=styles.button_title_style),
                ),
                color_scheme=color_scheme,
                high_contrast=True,
                variant="outline",
                #cursor="pointer",
                width="100%",
                radius="large",
            ),
            height="50px",
        ),
        href=url,
        is_external=True,
        width="100%",
    )