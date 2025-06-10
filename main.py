from nicegui import ui

import theme
from pages import about, contact, home, services


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


ui.run(
    reload=True,
    uvicorn_reload_includes="*.py, *.html, *.js, *.css",
    title="Cutthroat Systems",
    port=8081,
    favicon=theme.Logo.LOGO,
)
