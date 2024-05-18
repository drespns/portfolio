"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from link_bio_web.views.header.header import header
from link_bio_web.views.links.links import links
from link_bio_web.components.navbar import navbar
from link_bio_web.components.footer import footer


class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        navbar(),
        header(),
        links(),
        footer(),
    )


app = rx.App()
app.add_page(index)
