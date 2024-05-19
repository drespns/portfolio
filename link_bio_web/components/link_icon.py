import reflex as rx

from link_bio_web.styles import styles

def link_icon(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            text,
            width=styles.Size.BIG,
            height=styles.Size.BIG,
        ),
        href=url,
        is_external=True
    )