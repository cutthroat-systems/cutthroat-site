from nicegui import ui

import theme

services = {
    # Column 1 -----------------------------------------------
    "Software Engineering": [
        {
            "title": "Data Visualization and Analytics",
            "description": "Build interactive dashboards and analytics pipelines that transform raw data into actionable insights, empowering stakeholders with real-time metrics and trend analysis. We integrate data sources, implement drill-down reporting, and optimize performance for both desktop and mobile viewing, backed by robust data governance practices.",
        },
        {
            "title": "Integrated Software & Low-level Programming",
            "description": "Develop firmware, device drivers, and embedded software to ensure seamless hardware integration, deterministic performance, and reliable operation in mission-critical systems. We follow strict coding standards, implement safety checks, and automate testing and deployment through CI/CD pipelines to maintain code quality.",
        },
        {
            "title": "Custom Software Development",
            "description": "Craft custom full-stack software solutions—from architecture design through deployment—using agile processes, automated testing, and modular code to meet your business goals. We provide clear documentation, user-training sessions, and ongoing support contracts to ensure smooth adoption and continuous improvement.",
        },
    ],
    # Column 2 -----------------------------------------------
    "Hardware Design": [
        {
            "title": "Production Design",
            "description": "We design robust, scalable mechanical systems, creating detailed CAD models and tolerance analyses to ensure optimal manufacturability and reliability in high-volume production. Our iterative approach includes rapid prototyping feedback loops, DFMEA reviews, and close collaboration to minimize cycle time and reduce costs.",
        },
        {
            "title": "Rapid Prototyping & Manufacturing Consultation",
            "description": "We provide rapid-prototyping and manufacturability consulting—choosing materials and processes to speed development, coordinating vendors, and planning seamless transitions to full-scale production.",
        },
        {
            "title": "Thermal & Laboratory Analyses Consultation",
            "description": "We conduct CFD and thermal analyses to optimize cooling and ensure component reliability under extreme conditions, validating models with testing and integrating real-time monitoring for robust performance.",
        },
    ],
    # Column 3 -----------------------------------------------
    "System Integration": [
        {
            "title": "Precision and Scientific Control Systems",
            "description": "Design and integrate high-precision control systems with advanced sensor feedback and closed-loop algorithms, delivering sub-micron accuracy for scientific and industrial applications. Our solutions comply with regulatory standards, include full traceability features, and support remote monitoring and diagnostics.",
        },
        {
            "title": "Calibration Systems and Equipment Automations",
            "description": "Automate calibration workflows with custom rigs, automated measurement routines, and real-time data logging to enhance accuracy, reduce manual steps, and speed up results. We implement audit-ready reporting, remote calibration capabilities, and alerting mechanisms to maintain compliance and uptime.",
        },
        {
            "title": "Deployment and Training",
            "description": "Deliver turnkey deployment and hands-on training—from installation to best practices—to ensure your team can effectively operate, maintain, and scale the system. We provide tailored training materials, follow-up coaching, and performance assessments to guarantee long-term success.",
        },
    ],
}


imglist = [
    "static/img/services/Software Engineering.jpg",
    "static/img/services/Hardware Design.jpg",
    "static/img/services/System Integration.jpg",
]


def render() -> None:
    with ui.column().classes('w-full mx-auto pt-24 pb-0 gap-4 items-center').props(
        'id=about'
    ).style("padding-top: 0;"):
        ui.image('static/img/services/TroutCard.png').style(
            "width: 275px; object-fit: fill; margin: 0; padding: 0; display:"
        )
        ui.label('Services Provided').classes(
            'text-5xl italic font-bold text-center pb-4'
        ).style(f"color: {theme.Color.SOFT_ORANGE};")

        ui.label(
            "At Cutthroat Systems, our team of exceptional engineers brings together expertise in software, mechanical, and aerospace engineering to tackle even the most complex challenges. "
            "We specialize in consulting, CAD design and prototyping, precision mechanical engineering, aerospace solutions, custom software development, and systems design for calibration and automation. "
            "We are committed to delivering innovative solutions tailored to the unique needs of each client, ensuring every project is approached with creativity and precision. "
            "Our mission is to provide cutting-edge services that empower your business to thrive. "
            "Client satisfaction is at the heart of everything we do, and we take pride in transforming challenges into opportunities. "
        ).classes('text-lg text-center font-medium').style(
            f"color: {theme.Color.PARCHMENT}; max-width: 120ch;"
        )

        for i, (category, items) in enumerate(services.items()):
            img = imglist[i]
            with ui.card().classes(
                'parallax-card rounded-2xl shadow-lg w-4/5 px-6 py-4 '
                'flex flex-col items-center text-center '
                'hover:shadow-2xl transition-shadow duration-300'
            ).style(f'background-color: {theme.Color.PARCHMENT};'):

                # Parallax header container
                with ui.element('div').classes('parallax-header').style(
                    f"background-image: url('{img}');"
                ):
                    ui.label(category).classes('category-title')

                # Content below the header
                for service in items:
                    ui.label(service['title']).classes(
                        'text-2xl text-left font-bold'
                    ).style(f'color: {theme.Color.BURNT_ORANGE};')
                    ui.label(service['description']).classes(
                        'text-lg text-left font-medium'
                    ).style(f'color: {theme.Color.DARK_BROWN};')
                    ui.separator()

        # # Create cards for each service category
        # for i, (category, items) in enumerate(services.items()):
        #     with ui.card().classes(
        #         'rounded-2xl shadow-lg w-4/5 px-6 py-4 flex flex-col items-center text-center hover:shadow-2xl transition-shadow duration-300'
        #     ).style(f'background-color: {theme.Color.PARCHMENT};'):

        #         # Add a header card with a parallax image and category title
        #         with ui.element("q-parallax").props(
        #             f"src='{imglist[i]}' height='150' auto-width speed=30"
        #         ).style('background-position: bottom;'):
        #             with ui.card().classes(
        #                 'rounded-2xl shadow-md w-full px-4 py-2 flex items-center justify-center'
        #             ).style(
        #                 f'background-color: {theme.Color.SOFT_ORANGE}; width: fit-content;'
        #             ):
        #                 ui.label(category).classes('text-4xl italic font-bold').style(
        #                     f"color: {theme.Color.DARK_BROWN};"
        #                 )

        #         # List all services under the category
        #         for service in items:
        #             ui.label(service["title"]).classes(
        #                 'text-2xl text-left font-bold'
        #             ).style(f"color: {theme.Color.BURNT_ORANGE};")
        #             ui.label(service["description"]).classes(
        #                 'text-lg text-left font-medium'
        #             ).style(f"color: {theme.Color.DARK_BROWN};")
        #             ui.separator()
