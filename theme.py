import os

from nicegui import app, ui

from components import footer, header


class Color:

    DEEP_BROWN = "#2C1E1A"
    DARK_BROWN = "#201814"
    BURNT_ORANGE = "#e85e1c"
    LIGHT_SALMON = "#F9B78A"
    TAN_YELLOW = "#F4B951"
    SOFT_ORANGE = "#E99356"
    PARCHMENT = "#F4E8DC"


class Logo:
    LOGO = "static/img/logos/cutthroat.svg"
    LOGO_NAME = "static/img/logos/cutthroat_name&logo.svg"
    LOGO_NAME_long = "static/img/logos/cutthroat_name&logo_long.svg"


class Icon:
    HARDWARE = "static/img/icon/hardware.svg"
    INTEGRATION = "static/img/icon/integration.svg"
    SOFTWARE = "static/img/icon/software.svg"


# ---------------------
# Global Page Styling
# ---------------------
def apply():

    app.add_static_files("/static", os.path.join(os.path.dirname(__file__), "static"))
    ui.add_head_html(
        """
        <link href="static/handwrite.css" type="text/css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css2?family=Titillium+Web:ital,wght@0,200;0,300;0,400;0,600;0,700;1,200;1,300;1,400;1,600;1,700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Titillium Web', sans-serif;
            }
            .font-titillium {
                font-family: 'Titillium Web', sans-serif;
            }
        </style>
    """
    )

    ui.query("body").style(
        f"""
        background-color: {Color.DEEP_BROWN};
        margin: 0 auto;
        max-width: 80vw;
        padding: 0;
    """
    )

    header.render()
    footer.render()
