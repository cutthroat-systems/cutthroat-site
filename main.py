from nicegui import ui

import theme
from pages import home, services, about

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

#    about.render()

@ui.page("/contact")
def show_contact():
    theme.apply()

#    contact.render()

ui.run(reload=True, port = 8081)
