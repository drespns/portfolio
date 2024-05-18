import reflex as rx

def link_button(text:str, url:str, color_scheme:str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon("heart"),
            f"{text}",
            color_scheme=color_scheme,
            high_contrast=True,
            variant="outline",
            #cursor="pointer",
        ),
        href=url,
        is_external=True,
    )