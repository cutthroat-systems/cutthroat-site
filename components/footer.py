import datetime

from nicegui import ui

import theme


def render():
    with ui.footer().classes("w-full relative").style(
        f"""
            background-color: {theme.Color.PARCHMENT};
            border-top: 5px solid {theme.Color.BURNT_ORANGE};
            padding-top: 0.5rem;
            padding-bottom: 0.5rem;
        """
    ):

        with ui.column().classes(
            "w-full h-full items-center justify-center text-center"
        ).style("gap: 0.25rem; padding: 0;"):

            today = datetime.date.today()
            ui.label(f"© {today.year} Cutthroat Systems — All Rights Reserved").classes(
                "text-sm leading-tight"
            ).style(
                f"color: {theme.Color.DARK_BROWN}; margin: 0; padding-top: 0.125rem;"
            )

            ui.html(
                f"""
                <p style="
                    margin: 0;
                    font-size: 0.85rem;
                    color: {theme.Color.DARK_BROWN};
                    text-align: center;
                    padding-bottom: 0.125rem;
                ">
                    We made this site! Check out this and some of our other projects
                    <a href="{theme.Github.URL}" target="_blank"
                    style="color: {theme.Color.BURNT_ORANGE}; text-decoration: underline;">
                        here
                    </a>.
                </p>
            """
            )
