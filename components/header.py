from nicegui import context, ui

import theme


def render():
    with ui.header().classes("w-full h-[15vh] min-h-[4rem]").style(
        f"background-color: {theme.Color.PARCHMENT}; border-bottom: 5px solid {theme.Color.BURNT_ORANGE};"
    ):
        with ui.row().classes(
            "h-full w-full justify-between items-center flex-nowrap overflow-hidden"
        ):

            with ui.row().classes("h-full items-center justify-start"):
                with ui.link(target="/").classes("cursor-pointer").style(
                    "height: 11vh; display: flex; align-items: center;"
                ):
                    ui.html(
                        f"""
                        <img src="{theme.Logo.LOGO_NAME}" alt="Cutthroat Logo" title="Cutthroat Systems"
                            style="height: 100%; width: auto; max-height: 11vh; object-fit: contain; display: block;" />
                    """
                    )

            with ui.row().classes(
                "flex-auto h-full gap-16 items-end justify-end pe-16 pb-2 flex-wrap overflow-hidden"
            ):
                nav_link("Home", "/")
                nav_link("Services", "/services")
                nav_link("About", "/about")
                nav_link("Contact", "/contact")


def nav_link(name: str, target: str):
    is_underlined = (
        "underline" if context.client.page.path == target else "no-underline"
    )

    link = (
        ui.link(name, target)
        .classes(
            f"font-bold cursor-pointer {is_underlined} transition duration-200 ease-in-out"
        )
        .style(
            f"color: {theme.Color.DEEP_BROWN}; font-size: 4.75vh; text-decoration-thickness: 3px;"
        )
    )

    link.on(
        "mouseover",
        lambda: link.style(
            f"color: {theme.Color.SOFT_ORANGE}; transform: scale(1.05); text-decoration-thickness: 3px;"
        ),
    )
    link.on(
        "mouseout",
        lambda: link.style(
            f"color: {theme.Color.DEEP_BROWN}; transform: scale(1); text-decoration-thickness: 3px;"
        ),
    )
