import reflex as rx

def description() -> rx.Component:
    return rx.text(
        "Soy matemático y programador en el lenguaje ",
        rx.badge("PYTHON", variant="solid", high_contrast=True, color_scheme="grass"),
        " con apenas medio año de experiencia. También tengo conocimientos en ",
        rx.badge("HTML", variant="solid", high_contrast=True, color_scheme="red"), " y ",
        rx.badge("CSS", variant="solid", high_contrast=True, color_scheme="sky"),
        ". Actualmente estoy trabajando en ",
        rx.link(
            rx.badge("SAO", variant="solid", high_contrast=True, color_scheme="crimson"),
            href="https://saosl.com",
            is_external=True,
            cursor="pointer",
        ),
        " s.l., como becario por un periodo de ~10 meses. Estoy cursando el Máster de Big Data y Ciencia de datos en la ",
        rx.badge("VIU", variant="solid", high_contrast=True, color_scheme="orange"),
        "(", rx.text.em("Valencian International University"), ") donde trabajo con tecnologías punteras como ",
        rx.badge("MongoDB", variant="solid", high_contrast=True, color_scheme="lime"),
        "...",
        width="100%",
    )