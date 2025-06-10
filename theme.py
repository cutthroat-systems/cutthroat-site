from pathlib import Path

from nicegui import app, ui

from components import footer, header


class Color:
    DEEP_BROWN = "#2C1E1A"
    DARK_BROWN = "#201814"
    BURNT_ORANGE = "#e85e1c"
    LIGHT_SALMON = "#F9B78A"
    TAN_YELLOW = "#F7D396"
    SOFT_ORANGE = "#E99356"
    PARCHMENT = "#F4E8DC"


class Logo:
    LOGO = "static/img/logo/cutthroat.svg"
    LOGO_FULL = "static/img/logo/cutthroat_logo.svg"
    LOGO_LONG = "static/img/logo/cutthroat_logo_long.svg"


class Icon:
    HARDWARE = "static/img/icon/hardware.svg"
    INTEGRATION = "static/img/icon/integration.svg"
    SOFTWARE = "static/img/icon/software.svg"


class Github:
    URL = "https://github.com/cutthroat-systems"


# ---------------------
# Global Page Styling
# ---------------------
static_path = Path(__file__).parent.resolve() / "static"


def apply():
    app.add_static_files("/static", static_path)
    for path in static_path.glob("css/*.css"):
        ui.add_css(path)

    ui.dark_mode()

    # Adds above class colors to NiceGUI as Quasar colors (ex. BURNT_ORANGE -> burnt-orange)
    ui.colors(
        **{name.lower(): getattr(Color, name) for name in dir(Color) if name.isupper()}
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
