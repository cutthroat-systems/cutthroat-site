from nicegui import ui

import theme
from components import name_animation


def render():

    # --- Home Animation ---
    name_animation.render()

    # --- About Section ---
    with ui.column().classes("w-full mx-auto pt-8 pb-0 gap-4 items-center").props(
        "id=about"
    ):
        ui.label(
            "Engineering efficiency through custom software and hardware integration."
        ).classes("text-4xl italic font-bold text-center").style(
            f"color: {theme.Color.SOFT_ORANGE};"
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
    with ui.column().classes("w-full mx-auto pt-14 pb-0 gap-8 items-center").props(
        "id=services"
    ):
        ui.label("What We Do").classes(
            "text-6xl italic font-bold text-center pb-2"
        ).style(f"color: {theme.Color.SOFT_ORANGE};")

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
                    f"background-color: {theme.Color.PARCHMENT}; width: 21vw; min-width: 250px;"
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
        ui.label("How We Work").classes(
            "text-6xl italic font-bold text-center pb-2"
        ).style(f"color: {theme.Color.SOFT_ORANGE};")

        steps = [
            {
                "icon": "groups",
                "title": "Initial Consultation",
                "desc": "During this phase, we collaborate closely with your leadership and stakeholders to deeply understand your strategic objectives, current workflows, and pain points. We conduct structured interviews, facilitate workshops, and document detailed requirements to ensure alignment on project goals and success metrics.",
            },
            {
                "icon": "description",
                "title": "Proposal & Agreement",
                "desc": "In this stage, we craft a comprehensive proposal tailored to your needs, outlining scope, deliverables, timelines, and cost estimates in detail. Once reviewed, we refine terms, secure approvals, and formalize the partnership—incorporating risk assessments and milestone planning to set clear expectations—enabling a smooth transition into project execution.",
            },
            {
                "icon": "search",
                "title": "Research & Discovery",
                "desc": "Our team performs in-depth analysis of your existing systems, gathering quantitative and qualitative data through surveys, logs, and stakeholder interviews. We map current architectures, identify technical constraints, assess integration points, and deliver a comprehensive discovery report with actionable insights to guide informed design decisions.",
            },
            {
                "icon": "engineering",
                "title": "Design & Prototyping",
                "desc": "Leveraging the insights gained, we create prototypes, wireframes, and proof-of-concept models to validate key features and user flows. Through iterative feedback loops, technical feasibility reviews, and usability testing, we refine designs to meet functional requirements, address performance considerations, and provide an intuitive experience before full implementation.",
            },
            {
                "icon": "check_circle",
                "title": "Advisory & Delivery",
                "desc": "During development, we build and integrate robust, scalable solutions aligned with your architecture and quality standards. We provide ongoing technical guidance, conduct thorough code reviews, perform deployment planning, and facilitate knowledge transfer sessions, ensuring smooth delivery and empowering your team to maintain and extend the system effectively.",
            },
            {
                "icon": "handshake",
                "title": "Ongoing Support",
                "desc": "After launch, we continue to support your solution through proactive monitoring, performance optimization, and maintenance under agreed SLAs. Our team offers training, periodic updates, rapid issue resolution, and enhancement services, ensuring the system evolves with your business needs and that you maximize long-term ROI.",
            },
        ]

        with ui.stepper().props('horizontal alternative-labels').classes(
            'rounded-2xl w-[52vw]'
        ).style(f"background-color: {theme.Color.PARCHMENT};") as stepper:
            for step in steps:
                with ui.step(step["title"], step["title"], icon=step["icon"]).props(
                    "active-color=burnt-orange done-color=soft-orange"
                ):
                    ui.label(step["desc"]).classes("text-xl")
                    with ui.stepper_navigation():
                        ui.button("Next", color="burnt-orange", on_click=stepper.next)
                        if not step == steps[0]:
                            ui.button(
                                'Back', color="burnt-orange", on_click=stepper.previous
                            ).props("flat")

    # --- Contact Section ---
    with ui.column().classes("w-full gap-4 items-center pb-0 mt-8").props("id=contact"):
        ui.label("Contact Us").classes(
            "text-6xl italic font-bold text-center pb-2"
        ).style(f"color: {theme.Color.SOFT_ORANGE};")

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
