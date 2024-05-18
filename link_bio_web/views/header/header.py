import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback='DR', high_contrast=True, variant='solid', size="8", radius="full"), #name="Daniel Rodriguez" -> DR (fallback).
        rx.text("@8gofio"),
        rx.text("➡️ MI NOMBRE ES DANIEL 😊"),
        rx.text(
            """
            JSLDKJFBAJKSDFBJKSADFBJASBFDLKASBFDJKASBDFASBFJKASDFBSFJ
            """
        ),
        align="center",
        min_height="35vh"
    )