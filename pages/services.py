from nicegui import ui

import theme

services = {
    # Column 1 -----------------------------------------------
    "Hardware Design": [
        {
            "title": "Production Design",
            "description": "Our engineers have combined decades of experience designing mechanical mechanisms within the industry.",
            "icon": "ree",
        },
        {
            "title": "Thermal Engineering Consultation",
            "description": "Jarred REEEE",
            "icon": "ree",
        },
        {
            "title": "Rapid Protyping & Manufacturing Consultation",
            "description": "ree",
            "icon": "ree",
        },
    ],
    # Column 2 -----------------------------------------------
    "Software Engineering": [
        {
            "title": "Data Visualization and Analytics",
            "description": "ree",
            "icon": "ree",
        },
        {
            "title": "Integrated Software & Low-level Programming",
            "description": "ree",
            "icon": "ree",
        },
        {"title": "Custom Software Developement", "description": "ree", "icon": "ree"},
    ],
    # Column 3 -----------------------------------------------
    "System Integration": [
        {
            "title": "Precision and Scientific Control Systems",
            "description": "ree",
            "icon": "ree",
        },
        {"title": "Private Militia", "description": "ree", "icon": "ree"},
        {"title": "Deployment and Training", "description": "ree", "icon": "ree"},
    ],
}


def render() -> None:
    with ui.column().classes('w-full mx-auto pt-24 pb-0 gap-4 items-center').props(
        'id=about'
    ):
        ui.label('Services Provided').classes(
            'text-5xl italic font-bold text-center pb-4'
        ).style(f"color: {theme.Color.PARCHMENT};")
        ui.label(
            "At Cutthroat Systems, our team of exceptional engineers brings together expertise in software, mechanical, and aerospace engineering to tackle even the most complex challenges. "
            "We specialize in consulting, CAD design and prototyping, precision mechanical engineering, aerospace solutions, custom software development, and systems design for calibration and automation. "
            "We are committed to delivering innovative solutions tailored to the unique needs of each client, ensuring every project is approached with creativity and precision. "
            "Our mission is to provide cutting-edge services that empower your business to thrive. "
            "Client satisfaction is at the heart of everything we do, and we take pride in transforming challenges into opportunities. "
        ).classes('text-lg text-center font-medium').style(
            f"color: {theme.Color.PARCHMENT}; max-width: 120ch;"
        )

        # ui.image('assets\TempBanner.png')
        with ui.row().classes('w-full justify-center gap-8'):
            ui.video(
                'static/vid/Manufacturing.mp4',
                controls=False,
                autoplay=True,
                muted=True,
                loop=True,
            ).style('height: 440px;')
            ui.video(
                'static/vid/Programming.mp4',
                controls=False,
                autoplay=True,
                muted=True,
                loop=True,
            ).style('height: 440px;')
            ui.video(
                'static/vid/serverRoom.mp4',
                controls=False,
                autoplay=True,
                muted=True,
                loop=True,
            ).style('height: 440px;')

        with ui.card().classes('rounded-2xl shadow-lg w-full px-4 py-8').style(
            f'background-color: {theme.Color.PARCHMENT};'
        ):
            # Row for horizontal alignment
            with ui.row().classes('w-full justify-center gap-8'):
                keys_list = list(services.keys())  # Get the keys for the columns
                for i, key in enumerate(keys_list):
                    # Render each column
                    with ui.column().classes('w-1/4 items-center text-center gap-2'):
                        ui.label(key).classes('text-4xl italic font-bold').style(
                            f"color: {theme.Color.BURNT_ORANGE};"
                        )
                        ui.separator()
                        add_info(key)

                    # Add a vertical separator except after the last column
                    if i < len(keys_list) - 1:
                        ui.separator().props("vertical").style(
                            'border-left: 4px solid var(--theme-color-soft-orange); height: 100%;'
                        )  # tbis aint working for shit rn


def add_info(key: str) -> None:
    for service in services[key]:
        ui.label(service["title"]).classes('text-3xl text-center font-bold')
        ui.label(service["description"]).classes('text-lg text-left font-medium')
        ui.separator()

    """def clicked(key : str ) -> None: #Function to populate screen w/ button info
        right_column.clear()

        for service in services[key]:
            with right_column:
                with ui.card(align_items="baseline").classes(f'rounded-2xl shadow-lg').style(f'background-color: {theme.Color.PARCHMENT}; width: 30vw; min-width: 200px;'):
                    with ui.column().classes('w-full items-center'):
                        ui.label(service["title"]).classes('text-3xl text-center font-bold')
                    with ui.column(align_items="start").classes('w-full mx-auto pt-0 pb-0 gap-1 items-left'):
                        ui.label(service["description"]).classes('text-lg text-left font-medium')"""
