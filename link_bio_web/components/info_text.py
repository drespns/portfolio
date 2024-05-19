import reflex as rx

from link_bio_web.styles import styles

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title, weight="bold", color=styles.Color.SHADOW, as_="span"),
        body,
    )