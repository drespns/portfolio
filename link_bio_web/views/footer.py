from datetime import datetime
import reflex as rx

from link_bio_web.styles import styles

current_year = datetime.today().year

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/reflex.png", width="250px", height="auto",
        ),
        rx.link(
            rx.icon("copyright", size=5, stroke_width=15, color="black"),
            f"DANIEL RODRIGUEZ ESPINOSA - {current_year}",
            href="https://github.com/drespns",
            is_external=True,
            font_size=styles.Size.BIG.value
        ),
        rx.text("MATEMATICO - PROGRAMADOR - :)", margin_bottom=styles.Size.MEDIUM.value),
        align="center",
        background_color=styles.Color.CONTENT.value,
    )