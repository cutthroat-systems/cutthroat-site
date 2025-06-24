import os

from dotenv import load_dotenv
from nicegui import ui

import theme
from pages import about, contact, home, services

# Add "DEV_MODE=True" to ./.env to enable development mode
load_dotenv()
DEV = os.getenv("DEV_MODE", False)

# ^ This works to add most content, but fails to produce twitter cards, ios banners, etc. Needs work.
ui.add_head_html(
    f"""
    <title>Cutthroat Systems</title>
    <link rel="canonical" href="https://cutthroatsystems.com/" />
    <meta name="description" content="We help businesses automate workflows and integrate hardware & software.">
    <meta name="theme-color" content="{theme.Color.DEEP_BROWN}">

    <meta property="og:locale"      content="en_US" />
    <meta property="og:type"        content="website" />
    <meta property="og:site_name"   content="Cutthroat Systems" />
    <meta property="og:url"         content="https://cutthroatsystems.com/" />
    <meta property="og:title"       content="Cutthroat Systems - Custom Engineering Solutions" />
    <meta property="og:description" content="We help businesses automate workflows and integrate hardware & software." />
    <meta property="og:image"       content="https://cutthroatsystems.com/static/img/logo/preview-1200x630.png"/>

    <link rel="icon"                                    href="/static/img/favicon/favicon.ico" />
    <link rel="icon" type="image/png"   sizes="32x32"   href="/static/img/favicon/favicon-32x32.png">
    <link rel="icon" type="image/png"   sizes="16x16"   href="/static/img/favicon/favicon-16x16.png">
    <link rel="apple-touch-icon"        sizes="180x180" href="/static/img/favicon/apple-touch-icon.png">
    <link rel="icon" type="image/png"   sizes="192x192" href="/static/img/favicon/android-chrome-192x192.png" />
    <link rel="icon" type="image/png"   sizes="512x512" href="/static/img/favicon/android-chrome-512x512.png" />
    <link rel="manifest"                                href="/static/img/favicon/site.webmanifest">

    <meta name="twitter:card"           content="summary_large_image" />
    <meta name="twitter:title"          content="Cutthroat Systems - Custom Engineering Solutions" />
    <meta name="twitter:description"    content="We help businesses automate workflows and integrate hardware & software." />
    <meta name="twitter:image"          content="https://cutthroatsystems.com/static/img/logo/preview-1200x630.png" />
"""
)


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


if __name__ in {"__main__", "__mp_main__"}:
    if DEV:
        ui.run(
            reload=True,
            title="Cutthroat Systems",
            host="127.0.0.1",
            port=8081,
            favicon=theme.Logo.LOGO,
            uvicorn_reload_includes="*.py, *.html, *.css, *.js, *.vue",
            uvicorn_reload_excludes="**/.git/**, **/.venv/**, **/__pycache__/**",
        )
    else:
        port = int(os.environ.get("PORT", 80))
        host = "0.0.0.0"

        ui.run(
            reload=False,
            title="Cutthroat Systems",
            host=host,
            port=port,
            favicon=theme.Logo.LOGO,
        )
