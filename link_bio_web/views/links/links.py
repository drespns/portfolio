import reflex as rx

from link_bio_web.components.link_button import link_button

def links() -> rx.Component:
    """text:str, url:str, color_scheme:str
    
    Literal['tomato', 'red', 'ruby', 'crimson', 'pink', 'plum', 'purple', 'violet', 'iris', 'indigo', 'blue', 'cyan', 'teal', 'jade', 'green', 'grass', 'brown', 'orange', 'sky', 'mint', 'lime', 'yellow', 'amber', 'gold', 'bronze', 'gray']
    """
    return rx.vstack(
        link_button("Whatsapp", "Hola", "https://web.whatsapp.com/", "grass"),
        link_button("Youtube", "Adios", "https://www.youtube.com/", "ruby"),
        link_button("Instagram", "Hola", "https://www.instagram.com/", "purple"),
        link_button("Github", "Adios", "https://github.com/drespns", "jade"),
        align="center",
        justify="center",
        width="100%",
    )