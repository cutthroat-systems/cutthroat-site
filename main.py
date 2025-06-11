from nicegui import ui

import theme
from pages import about, contact, home, services

ui.add_head_html(
    f'''
    <link rel="icon" href="/static/img/favicon/favicon.ico" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="https://cutthroatsystems.com/" />
    <meta property="og:title" content="Cutthroat Systems - Custom Engineering Solutions" />
    <meta property="og:description" content="We help businesses automate workflows and integrate hardware & software." />
    <link rel="icon" type="image/png" sizes="32x32" href="/static/img/favicon/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/static/img/favicon/favicon-16x16.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/static/img/favicon/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="192x192" href="/static/img/favicon/android-chrome-192x192.png" />
    <link rel="icon" type="image/png" sizes="512x512" href="/static/img/favicon/android-chrome-512x512.png" />
    <link rel="manifest" href="/site.webmanifest">
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="msapplication-TileColor" content="{theme.Color.DEEP_BROWN}" />
    <meta name="msapplication-TileImage" content="/static/mstile-150x150.png" />
'''
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

    # port = int(os.environ.get('PORT', 80))
    # host = "0.0.0.0"

    # ui.run(
    #     reload=False,
    #     title="Cutthroat Systems",
    #     host=host,
    #     port=port,
    #     favicon=theme.Logo.LOGO,
    # )

    ui.run(
        reload=True,
        title="Cutthroat Systems",
        host="127.0.0.1",
        port=8081,
        favicon=theme.Logo.LOGO,
    )
