import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text("drespns", height="40px", color_scheme="crimson", high_contrast=True, as_="mark"),
        position="sticky",
        bg="gray",
        padding_x="16px",
        padding_y="16px",
        box_sizing="border-box",
        width="100%",
        z_indez="999"
    )