from nicegui import ui

import theme
from components import name_animation


def render():

    # --- Home Animation ---
    name_animation.render()

    # --- About Section ---
    with ui.column().classes("w-full mx-auto pt-12 pb-0 gap-4 items-center").props(
        "id=about"
    ):
        ui.label(
            "Engineering efficiency through custom software and hardware integration."
        ).classes("text-5xl italic font-bold text-center pb-4").style(
            f"color: {theme.Color.PARCHMENT};"
        )

        ui.label(
            (
                """
            We're a consulting firm of engineers specializing in tailored software and embedded hardware
            solutions that solve real-world operational challenges. From automating manual workflows to designing
            full-stack systems that interface with physical devices, we help businesses improve efficiency,
            reduce complexity, and scale with confidence.
        """
            )
        ).classes("text-xl text-center").style(
            f"color: {theme.Color.PARCHMENT}; max-width: 90ch;"
        )

    # --- Services Section ---
    with ui.column().classes("w-full mx-auto my-8 pt-12 pb-0 gap-8 items-center").props(
        "id=services"
    ):
        ui.label("What We Do").classes("text-6xl font-bold text-center pb-2").style(
            f"color: {theme.Color.SOFT_ORANGE};"
        )

        with ui.row().classes("flex-wrap justify-center gap-8"):
            service_data = [
                {
                    "title": "Hardware Design",
                    "desc": "Mechanical and electrical systems designed for real-world performance and reliability.",
                    "icon": theme.Icon.HARDWARE,
                },
                {
                    "title": "Software Engineering",
                    "desc": "Custom software and embedded solutions that bring your product, process, or system to life.",
                    "icon": theme.Icon.SOFTWARE,
                },
                {
                    "title": "System Integration",
                    "desc": "We connect the pieces — hardware, software, and data — into seamless operations.",
                    "icon": theme.Icon.INTEGRATION,
                },
            ]

            for service in service_data:
                with ui.card().classes("rounded-2xl shadow-lg").style(
                    f"background-color: {theme.Color.PARCHMENT}; width: 23vw; min-width: 250px;"
                ):
                    with ui.column().classes("items-center p-6 gap-4").style(
                        f"color: {theme.Color.DARK_BROWN};"
                    ):
                        ui.image(service["icon"]).props("fit=contain").classes(
                            "w-16 h-16 service-icon"
                        ).style("overflow: visible; object-fit: contain;")
                        ui.label(service["title"]).classes(
                            "text-2xl font-bold text-center"
                        ).style(f"color: {theme.Color.BURNT_ORANGE};")
                        ui.label(service["desc"]).classes(
                            "text-lg text-center font-medium"
                        )

    # --- How We Work Section ---
    with ui.column().classes("w-[80vw] mx-auto pt-12 my-8 gap-8 items-center").props(
        "id=workflow"
    ):
        ui.label("How We Work").classes("text-6xl font-bold text-center pb-2").style(
            f"color: {theme.Color.SOFT_ORANGE};"
        )

        step_card_width = 18

        steps = [
            {
                "icon": "groups",
                "title": "Initial Consultation",
                "desc": "We meet with your team to align on goals, review your current systems, and identify project requirements together.",
            },
            {
                "icon": "description",
                "title": "Proposal & Agreement",
                "desc": "We deliver a detailed proposal outlining scope, timeline, and pricing — then finalize terms and start the engagement.",
            },
            {
                "icon": "search",
                "title": "Research & Discovery",
                "desc": "We analyze your environment, gather data, and document the technical context to guide effective design decisions.",
            },
            {
                "icon": "engineering",
                "title": "Design & Prototyping",
                "desc": "We develop wireframes, mockups, or proof-of-concepts to validate core ideas before full-scale implementation begins.",
            },
            {
                "icon": "check_circle",
                "title": "Advisory & Delivery",
                "desc": "We build and deploy robust, scalable solutions while advising your team on usage, integration, and system handoff.",
            },
            {
                "icon": "handshake",
                "title": "Ongoing Support",
                "desc": "We offer continued support through service contracts, updates, and improvements tailored to your evolving needs.",
            },
        ]

        _step_card_width = f"[{step_card_width}vw]"

        # [0] --> [1]  --> [2]
        with ui.row().classes("flex-wrap justify-center gap-6 items-center"):
            for i in range(3):
                with ui.column().classes("items-center gap-2"):
                    with ui.card().classes(
                        f"w-{_step_card_width} rounded-xl shadow-md"
                    ).style(f"background-color: {theme.Color.PARCHMENT};"):
                        with ui.column().classes("items-center p-4 gap-3").style(
                            f"color: {theme.Color.DARK_BROWN};"
                        ):
                            ui.icon(steps[i]["icon"]).classes("text-4xl")
                            ui.label(steps[i]["title"]).classes(
                                "text-lg font-bold text-center"
                            ).style(f"color: {theme.Color.BURNT_ORANGE};")
                            ui.label(steps[i]["desc"]).classes(
                                "text-sm text-center font-medium"
                            )

                if i < 2:
                    ui.icon("arrow_forward_ios").classes(
                        "text-2xl mx-2 self-center"
                    ).style(f"color: {theme.Color.PARCHMENT};")

        # [ ]    [ ]     v
        with ui.row().classes("justify-center pt-2 gap-6"):

            ui.element().classes(f"w-{_step_card_width}")
            ui.element().classes(f"w-{_step_card_width}")
            ui.element().style("width: 10rem;")

            with ui.column().classes(f"w-{_step_card_width} items-center"):
                ui.icon("arrow_downward_ios").classes("text-2xl").style(
                    f"color: {theme.Color.PARCHMENT};"
                )

        # [5]  <-- [4]  <-- [3]
        with ui.row().classes("flex-wrap justify-center gap-6 items-center"):
            for i in range(5, 2, -1):
                with ui.column().classes("items-center gap-2"):
                    with ui.card().classes(
                        f"w-{_step_card_width} rounded-xl shadow-md"
                    ).style(f"background-color: {theme.Color.PARCHMENT};"):
                        with ui.column().classes("items-center p-4 gap-3").style(
                            f"color: {theme.Color.DARK_BROWN};"
                        ):
                            ui.icon(steps[i]["icon"]).classes("text-4xl")
                            ui.label(steps[i]["title"]).classes(
                                "text-lg font-bold text-center"
                            ).style(f"color: {theme.Color.BURNT_ORANGE};")
                            ui.label(steps[i]["desc"]).classes(
                                "text-sm text-center font-medium"
                            )

                if i > 3:
                    ui.icon("arrow_back_ios").classes(
                        "text-2xl mx-2 self-center"
                    ).style(f"color: {theme.Color.PARCHMENT};")

    # --- Contact Section ---
    with ui.column().classes("w-full gap-4 items-center pb-0 mt-8").props("id=contact"):
        ui.label("Contact Us").classes("text-6xl font-bold text-center pb-2").style(
            f"color: {theme.Color.SOFT_ORANGE};"
        )

        ui.label(
            "Let's talk about your next project. We're here to help engineer it right."
        ).classes("italic text-xl text-center").style(
            f"color: {theme.Color.PARCHMENT};"
        )

        ui.html(
            f"""
            For project inquiries, reach out through our website
            <a href="/contact" class="text-[{theme.Color.SOFT_ORANGE}] italic underline hover:text-[{theme.Color.LIGHT_SALMON}]">here</a>
            or email us at
            <a href="mailto:info@cutthroatsystems.com" class="text-[{theme.Color.SOFT_ORANGE}] italic underline hover:text-[{theme.Color.LIGHT_SALMON}]">info@cutthroatsystems.com</a>

        """
        ).classes("text-xl text-center text-base").style(
            f"color: {theme.Color.PARCHMENT}"
        )
