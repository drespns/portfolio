import reflex as rx

from link_bio_web.styles import styles

def link_button(title: str, subtitle: str, url: str, color_scheme: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    "github",
                    width=styles.Size.BIG,
                    height=styles.Size.BIG,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(subtitle, style=styles.button_title_style),
                    padding="0",
                    spacing="0",
                ),
                width="100%",
                align="center",
                justify="start",
                spacing="2",
            ),
            color_scheme=color_scheme,
            radius="full",
            high_contrast=True,
            variant="classic",
        ),
        href=url,
        is_external=True,
        width="100%",
    )