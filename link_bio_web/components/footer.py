from datetime import datetime
import reflex as rx

current_year = datetime.today().year

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/reflex.png", width="250px", height="auto",
        ),
        rx.link(
            f"♾️ DANIEL RODRIGUEZ ESPINOSA - {current_year}",
            href="https://github.com/drespns",
        ),
        rx.text("MATEMATICO - PROGRAMADOR - :)"),
        align="center",
    )