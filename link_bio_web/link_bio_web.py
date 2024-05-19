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

# -------------------------------------------------------------------------------------------------------

app = rx.App(
    stylesheets=[
        "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
    ],
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="👨🏽 Portfolio - Daniel Rguez Espinosa",
    description="Mi portfolio.",
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