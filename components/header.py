from nicegui import context, ui

import theme


def render():
    ui.add_head_html('<meta name="viewport" content="width=device-width, initial-scale=1">')

    with ui.header().classes(
        "w-full bg-[var(--q-parchment)] border-b-[7.5px] border-[var(--q-burnt-orange)] "
        "flex gap-6 flex-col items-center py-4 px-6 "
        "sm:flex-row sm:justify-between sm:items-center sm: gap-0"
    ):
        ui.element("img").props(f'src="{theme.Logo.LOGO_FULL}" alt="Logo"').classes(
            "cursor-pointer "
            "transform transition-transform duration-200 hover:scale-105 "
            "w-full max-w-[90vw] h-auto object-contain min-h-[6vh] "  # mobile
            "sm:w-auto sm:max-h-[12vh] flex-shrink-0"  # desktop
        ).style("display:block;").on("click", lambda: ui.navigate.to("/"))

        with ui.row().classes(
            "mt-auto flex flex-wrap justify-center flex-1 items-center gap-y-8 flex-nowrap "
            "gap-2 text-sm "  # mobile defaults
            "sm:justify-end sm:gap-16 sm:text-lg sm:px-4 sm:pb-2"  # desktop overrides
        ):
            # Each nav link shrinks to fit
            for label, path in [
                ("Home", "/"),
                ("Services", "/services"),
                ("About", "/about"),
                ("Contact", "/contact"),
            ]:
                nav_link(label, path)


def nav_link(name: str, target: str):
    _underline_thickness = 4
    is_underlined = "underline" if context.client.page.path == target else "no-underline"

    link = (
        ui.link(name, target)
        .classes(
            f"roboto-slab-title text-2xl sm:text-5xl cursor-pointer {is_underlined} transition duration-200 ease-in-out flex-shrink-0"
        )
        .style(
            f"color: {theme.Color.DEEP_BROWN}; text-decoration-thickness: {_underline_thickness}px; font-weight: 800 !important;"
        )
    )

    link.on(
        "mouseover",
        lambda: link.style(
            f"color: {theme.Color.BURNT_ORANGE}; transform: scale(1.05); text-decoration-thickness: {_underline_thickness}px;"
        ),
    )
    link.on(
        "mouseout",
        lambda: link.style(
            f"color: {theme.Color.DEEP_BROWN}; transform: scale(1); text-decoration-thickness: {_underline_thickness}px;"
        ),
    )
