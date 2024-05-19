import reflex as rx

from link_bio_web.components.link_button import link_button
from link_bio_web.components.title import title

def links() -> rx.Component:
    """text:str, url:str, color_scheme:str
    
    Literal['tomato', 'red', 'ruby', 'crimson', 'pink', 'plum', 'purple', 'violet', 'iris', 'indigo', 'blue', 'cyan', 'teal', 'jade', 'green', 'grass', 'brown', 'orange', 'sky', 'mint', 'lime', 'yellow', 'amber', 'gold', 'bronze', 'gray']
    """
    return rx.vstack(
        title("Proyectos"),
        link_button("Proyecto", "Portfolio hecho con Reflex", "https://github.com/drespns", "grass"),
        link_button("Proyecto", "Pandas", "https://github.com/drespns", "ruby"),
        link_button("Proyecto", "HTML - CSS - JavaScript", "https://github.com/drespns", "purple"),
        link_button("Proyecto", "MongoDB", "https://github.com/drespns", "gray"),
        align="center",
        justify="center",
        width="100%",
    )