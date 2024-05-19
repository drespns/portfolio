import reflex as rx

'''def technologies_image(src: str) -> rx.Component:
    return rx.image(
        src=src,
        width="100px",
        height="100px",
        border_radius="50%",
        border="5px solid #555",
    )'''
def technologies_image(src: str, alt: str) -> rx.Component:
    return rx.box(
        rx.aspect_ratio(
            rx.image(
                src=src,
                alt=alt,
                width="100%",
                height="100%",
                border_radius="50%",
                border="3px solid #555",
                box_shadow="#fe0 0 5px 5px",
            ),
            ratio=1,
        ),
        width="15%",
    )