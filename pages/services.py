from nicegui import ui

import theme

services = {
    # Column 1 -----------------------------------------------
    "Software Engineering": [
        {
            "title": "Data Visualization and Analytics",
            "description": "We build interactive analytics dashboards that transform raw data into valuable insights, empowering businesses with real-time metrics and trend analysis. We integrate data sources, implement reporting, and optimize performance, backed by robust data governance practices.",
        },
        {
            "title": "Integrated Software & Low-level Programming",
            "description": "We develop firmware, device drivers, and embedded software to ensure hardware integration, performance, and operation in critical systems. We follow strict coding standards, implement safety checks, and automate testing and deployment through CI/CD pipelines to maintain quality and ensure compatibility.",
        },
        {
            "title": "Custom Software Development",
            "description": "We craft custom full-stack software solutions—from design through deployment—using custom processes, automated testing, and modular code to meet your business goals. We provide clear documentation, user-training sessions, and ongoing support contracts to ensure smooth adoption and continuous improvement.",
        },
    ],
    # Column 2 -----------------------------------------------
    "Hardware Design": [
        {
            "title": "Production Design",
            "description": "We craft robust, scalable mechanical solutions by developing detailed CAD models, performing tolerance analysis, and conducting DFMEA-driven design reviews. Through iterative prototyping and close collaboration with businesses, we ensure optimal performance, reliability, and design integrity.",
        },
        {
            "title": "Rapid Prototyping & Manufacturing Consultation",
            "description": "We provide rapid-prototyping and manufacturability consulting—choosing materials and processes to speed development, coordinating vendors, and planning seamless transitions to full-scale production. We then develop production workflows and quality checkpoints to ensure a seamless transition into manufacturing.",
        },
        {
            "title": "Thermal & Laboratory Analyses Consultation",
            "description": "We conduct CFD and thermal analyses to optimize cooling and ensure component reliability under extreme conditions, validating models with testing and integrating real-time monitoring for robust performance. We integrate sensor feedback and data-logging systems for performance monitoring and reliability assurance in the field.",
        },
    ],
    # Column 3 -----------------------------------------------
    "System Integration": [
        {
            "title": "Precision and Scientific Control Systems",
            "description": "We design and integrate high-precision control systems with sensor feedback and closed-loop algorithms, delivering accuracy for scientific and industrial applications. Our solutions comply with regulatory standards, include traceability features, and support remote monitoring and diagnostics.",
        },
        {
            "title": "Calibration Systems and Equipment Automations",
            "description": "We automate calibration workflows with custom rigs, automated measurement routines, and real-time data logging to enhance accuracy, reduce manual steps, and speed up results. We implement audit-ready reporting, remote calibration capabilities, and alerting mechanisms to maintain compliance and uptime.",
        },
        {
            "title": "Deployment and Training",
            "description": "We deliver turnkey deployment and hands-on training to ensure your team can effectively operate, maintain, and scale the system. We provide tailored training materials, follow-up coaching, performance assessments, and dedicated account management to guarantee long-term success.",
        },
    ],
}


imglist = [
    "static/img/services/Software Engineering.jpg",
    "static/img/services/Hardware Design.jpg",
    "static/img/services/System Integration.jpg",
]


def render() -> None:
    with ui.column().classes("w-full mx-auto pt-4 pb-0 gap-4 items-center"):
        # Services Provided
        ui.label("Services Provided").classes("text-7xl italic font-bold text-center pb-4").style(
            f"color: {theme.Color.SOFT_ORANGE};"
        )

        # Trout Services Img
        ui.element("img").props("src='static/img/services/TroutCard.png'").classes(
            "h-[10rem] w-auto object-contain pb-2"
        )

        ui.label(
            "We operate out of San Diego providing services to customers around the world.\n"
            "We're ready to bring our expertise to you."
        ).classes("text-xl italic text-center font-medium pb-4").style(
            f"color: {theme.Color.PARCHMENT}; max-width: 100ch;"
        )

        # Services Cards
        for i, (category, items) in enumerate(services.items()):
            img = imglist[i]
            with (
                ui.card()
                .classes(
                    "parallax-card rounded-2xl shadow-lg w-[90vw] sm:w-[75vw] px-6 pt-6 pb-6 mb-5 "
                    "flex flex-col items-center text-center "
                )
                .style(f"background-color: {theme.Color.PARCHMENT};")
            ):
                # Parallax header container
                with (
                    ui.element("div")
                    .classes("parallax-header rounded-t-4xl rounded-b-none text-lg sm:text-5xl")
                    .style(f"background-image: url('{img}');")
                ):
                    ui.label(category).classes("category-title")

                # Content below the header
                for service in items:
                    ui.label(service["title"]).classes("w-full text-2xl text-center font-bold").style(
                        f"color: {theme.Color.BURNT_ORANGE};"
                    )
                    ui.label(service["description"]).classes("w-full text-base text-left font-medium").style(
                        f"color: {theme.Color.DARK_BROWN};"
                    )
                    ui.separator()
