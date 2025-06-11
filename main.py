import os

from nicegui import ui

import theme
from pages import about, contact, home, services

theme.apply()


@ui.page("/")
def show_home():
    theme.apply()
    home.render()


@ui.page("/services")
def show_services():
    theme.apply()
    services.render()


@ui.page("/about")
def show_about():
    theme.apply()
    about.render()


@ui.page("/contact")
def show_contact():
    theme.apply()
    contact.render()


if __name__ == "__main__":

    port = int(os.environ.get('PORT', 8080))
    host = "0.0.0.0"

    ui.run(
        reload=False,
        title="Cutthroat Systems",
        host=host,
        port=port,
        favicon=theme.Logo.LOGO,
    )
