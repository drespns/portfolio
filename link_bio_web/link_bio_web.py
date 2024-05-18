"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

# Views
from link_bio_web.views.header.header import header
from link_bio_web.views.links.links import links
from link_bio_web.views.technologies.technologies import technologies
# Components
from link_bio_web.components.navbar import navbar
from link_bio_web.components.footer import footer
# States
#...
# Styles
from link_bio_web.styles import styles #import MAX_WIDTH
#


class State(rx.State):
    """The app state."""

    pass
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
                # align='center',
                # justify='center',
                margin_y=styles.Size.DEFAULT.value,
            ),
        ),
        footer(),
    )

"""
stylesheets=[
        "/css/styles.css",  # This path is relative to assets/
    ],
"""
app = rx.App()
app.add_page(index)
