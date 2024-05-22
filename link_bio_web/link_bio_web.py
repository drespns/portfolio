"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

# Views
from link_bio_web.views.header import header
from link_bio_web.views.links import links
from link_bio_web.views.technologies import technologies
from link_bio_web.views.navbar import navbar
from link_bio_web.views.footer import footer

# States
from link_bio_web.states.states import State
# Styles
from link_bio_web.styles import styles #import MAX_WIDTH
#


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.script("document.documentElement.lang='es'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                technologies(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value,
            ),
        ),
        footer(),
    )
#

# -------------------------------------------------------------------------------------------------------

TAG = ""
app = rx.App(
    # stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",],
    style=styles.BASE_STYLE,
#     head_components=[
#         rx.script(src=f"htpps://googletagmanager.com/gtag/js?id={TAG}"),
#         rx.script(
#             f"""
# window.dataLayer = window.dataLayer || [];
# function gtag(){dataLayer.push(arguments);}
# gtag('js', new Date());
# gtag('config', '{TAG}');
# """
#         )
#     ]
)

# ------

title = "👨🏽 Portfolio"
description = "Bienvenid@ a mi portfolio. Me llamo Daniel Rodriguez Espinosa; soy programador y matematico. En camino a ser full-stack."
avatar = "hasbulla.jpg"
preview = "https://cdn.milenio.com/uploads/media/2022/10/13/hasbulla-instagram.jpg"
app.add_page(
    index,
    title=title,
    description=description,
    image=avatar,
    meta=[ # añadimos las meta-tags; información que se nos comparte cuando nosotros ponemos el link de nuestra
        # web en redes sociales.
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:decription", "content": description},
        {"name": "og:image", "content": preview},
        # {"name": "twitter:card", "content": "summary_large_image"},
        # {"name": "twitter:site", "content": "@drespns"},
    ]
)
"""
(method) def add_page(
    component: Component | ComponentCallable,
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    image: str = constants.DefaultPage.IMAGE,
    on_load: EventHandler | EventSpec | list[EventHandler | EventSpec] | None = None,
    meta: list[dict[str, str]] = constants.DefaultPage.META_LIST
) -> None
"""