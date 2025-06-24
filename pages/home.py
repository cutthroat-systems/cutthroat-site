from nicegui import ui

import theme
from components import name_animation


def render():
    # --- Home Animation ---
    name_animation.render()

    # --- About Section ---
    with ui.column().classes("w-full mx-auto pt-8 pb-0 gap-4 items-center").props("id=about"):
        ui.label("Engineering efficiency through custom software and hardware integration.").classes(
            "text-4xl italic font-bold text-center"
        ).style(f"color: {theme.Color.SOFT_ORANGE};")

        ui.label(
            (
                "We're a consulting firm of engineers based out of San Diego, California specializing in tailored software and embedded hardware solutions that solve real-world operational challenges. From automating manual workflows to designing full-stack systems that interface with physical devices, we help businesses improve efficiency, reduce complexity, and scale with confidence."
            )
        ).classes("text-xl text-center").style(f"color: {theme.Color.PARCHMENT}; max-width: 95ch;")

    # --- Services Section ---
    with ui.column().classes("w-full mx-auto pt-14 pb-0 gap-8 items-center").props("id=services"):
        ui.label("What We Do").classes("text-6xl italic font-bold text-center pb-2").style(
            f"color: {theme.Color.SOFT_ORANGE};"
        )

        with ui.row().classes("flex-wrap justify-center gap-8 items-stretch"):
            service_data = [
                {
                    "title": "Software Engineering",
                    "desc": "Custom software and embedded solutions that bring your product or system to life.",
                    "icon": theme.Icon.SOFTWARE,
                },
                {
                    "title": "Hardware Design",
                    "desc": "Mechanical and electrical systems designed for real-world performance and reliability.",
                    "icon": theme.Icon.HARDWARE,
                },
                {
                    "title": "System Integration",
                    "desc": "We connect the pieces — hardware, software, and data — into seamless operations.",
                    "icon": theme.Icon.INTEGRATION,
                },
            ]

            for service in service_data:
                with (
                    ui.card()
                    .classes(
                        "rounded-2xl shadow-lg px-0 py-2 flex flex-col h-full"
                        "transform transition-transform duration-300 ease-in-out hover:scale-105 cursor-pointer"
                    )
                    .style(f"background-color: {theme.Color.PARCHMENT}; width: 18vw; min-width: 250px;")
                    .on("click", lambda: ui.navigate.to("/services"))
                ):
                    with ui.column().classes("items-center p-6 gap-4").style(f"color: {theme.Color.DARK_BROWN};"):
                        ui.image(service["icon"]).props("fit=contain").classes("w-16 h-16 service-icon").style(
                            "overflow: visible; object-fit: contain;"
                        )
                        ui.label(service["title"]).classes("text-2xl font-bold text-center").style(
                            f"color: {theme.Color.BURNT_ORANGE};"
                        )
                        ui.label(service["desc"]).classes("text-lg text-center font-medium")

    # --- How We Work Section ---
    with ui.column().classes("w-[80vw] mx-auto pt-12 my-8 gap-8 items-center").props("id=workflow"):
        ui.label("How We Work").classes("text-6xl italic font-bold text-center pb-2").style(
            f"color: {theme.Color.SOFT_ORANGE};"
        )

        steps = [
            {
                "icon": "groups",
                "title": "Initial Consultation",
                "desc": "During this phase, we collaborate closely with your leadership and stakeholders to deeply understand your strategic objectives, current workflows, and pain points. We conduct structured interviews, facilitate workshops, map business processes, and document detailed requirements, as well as evaluate stakeholder feedback and identify hidden inefficiencies to ensure comprehensive alignment before moving into planning.",
            },
            {
                "icon": "description",
                "title": "Proposal & Agreement",
                "desc": "In this stage, we craft a comprehensive proposal tailored to your needs, outlining scope, deliverables, timelines, resource allocations, and cost estimates in granular detail. We refine terms, secure stakeholder approvals, formalize the statement of work with clear milestones, and incorporate regulatory requirements and risk assessments to ensure robust governance and predictable outcomes.",
            },
            {
                "icon": "search",
                "title": "Research & Discovery",
                "desc": "Our team conducts an exhaustive technical assessment, analyzing your existing systems and infrastructure, collecting both quantitative and qualitative data through logs, performance metrics, security audits, and stakeholder interviews. We map current architectures, identify integrations, compliance constraints, and deliver a detailed discovery report with prioritized recommendations and risk mitigation strategies.",
            },
            {
                "icon": "engineering",
                "title": "Design & Prototyping",
                "desc": "Leveraging insights from our discovery phase, we develop design artifacts including interactive prototypes, high-fidelity wireframes, and proof-of-concept models to validate core functionalities and user workflows. Through iterative feedback cycles, feasibility reviews, and usability testing sessions, we refine each design to balance performance, accessibility, and maintainability prior to full-scale development.",
            },
            {
                "icon": "check_circle",
                "title": "Advisory & Delivery",
                "desc": "During delivery, we implement and integrate robust, scalable solutions that adhere to your architectural principles and quality standards. We provide ongoing technical guidance, conduct rigorous code reviews and automated testing, perform deployment and rollback planning, and facilitate comprehensive knowledge transfer sessions to empower your team with best practices and operational readiness.",
            },
            {
                "icon": "handshake",
                "title": "Ongoing Support",
                "desc": "After launch, we offer continuous support and maintenance to ensure optimal performance, reliability, and security under agreed service-level agreements. Our team conducts proactive monitoring, performance tuning, security updates, and rapid incident resolution. We also provide strategic recommendations, roadmap planning, and user adoption assistance to keep your solution evolving smoothly with your business objectives.",
            },
        ]

        with (
            ui.stepper()
            .props("horizontal alternative-labels")
            .classes("rounded-2xl w-[80vw]")
            .style(f"background-color: {theme.Color.PARCHMENT};") as stepper
        ):
            for step in steps:
                with ui.step(step["title"], step["title"], icon=step["icon"]).props(
                    "active-color=burnt-orange done-color=soft-orange header-nav=true"
                ):
                    ui.label(step["desc"]).classes("text-lg")
                    with ui.stepper_navigation():
                        if not step == steps[-1]:
                            ui.button("Next", on_click=stepper.next)
                        if not step == steps[0]:
                            ui.button("Back", on_click=stepper.previous).props("flat")

    # --- Contact Section ---
    with ui.column().classes("w-full gap-4 items-center pb-0 mt-8").props("id=contact"):
        ui.label("Contact Us").classes("text-6xl italic font-bold text-center pb-2").style(
            f"color: {theme.Color.SOFT_ORANGE};"
        )

        ui.label("Let's talk about your next project. We're here to help engineer it right.").classes(
            "italic text-xl text-center"
        ).style(f"color: {theme.Color.PARCHMENT};")

        ui.html(
            f"""
            For project inquiries, reach out through our website
            <a href="/contact" class="text-[{theme.Color.SOFT_ORANGE}] italic underline hover:text-[{theme.Color.LIGHT_SALMON}]">here</a>
            or email us at
            <a href="mailto:info@cutthroatsystems.com" class="text-[{theme.Color.SOFT_ORANGE}] italic underline hover:text-[{theme.Color.LIGHT_SALMON}]">info@cutthroatsystems.com</a>

        """
        ).classes("text-xl text-center text-base").style(f"color: {theme.Color.PARCHMENT}")
