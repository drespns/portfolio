import reflex as rx

from link_bio_web.styles import styles

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "drespns",
            #height="40px",
            color_scheme="crimson",
            high_contrast=True,
            as_="span",
            size="2"
        ),
        position="sticky",
        inset="0",
        background_color=styles.Color.CONTENT.value,
        padding_x=styles.Size.BIG.value,
        padding_y=styles.Size.BIG.value,
        box_sizing="border-box",
        width="100%",
        z_indez="999"
    )