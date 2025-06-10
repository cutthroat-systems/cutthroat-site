from nicegui import ui

import theme

people = [
    {
        "name": "Patrick Miller",
        "title": "Business Analytics and Software Design",
        "description": "Patrick is a seasoned project manager, analytics expert, and software developer with a unique blend of financial and technical expertise. He began his career managing a $500 million portfolio while working with leading lending institutions, including Blackstone, Wells Fargo, and Bank of America, where he developed predictive models to forecast loan performance and detect risks in complex financing operations. His transition into software development began with a breakthrough in gamification—designing a funding leaderboard that boosted productivity and morale. This sparked a passion for creating data-driven solutions to optimize workflows and enhance business performance. Now leading financial strategy and software architecture at Cutthroat Systems, Patrick combines his deep analytical skills, business acumen, and software development expertise to deliver innovative engineering and software solutions. Currently pursuing a Master's in Software Engineering, he bridges the gap between business, data, and technology to drive company success.",
        "icon": "static/img/headshots/PatHeadshot.png",
    },
    {
        "name": "Jarred Druzynski",
        "title": "Software and Integration Engineer",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque euismod, nibh non consequat aliquet, nisi urna tincidunt lectus, ac sollicitudin enim ipsum id lorem. Fusce quis vulputate felis. Sed at vestibulum est. Morbi pretium, orci nec vehicula facilisis, purus lacus ultricies sapien, id egestas ipsum lacus eu orci. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus sit amet velit et sem dapibus efficitur. Integer vitae ex eu dolor fringilla efficitur. Vivamus finibus, eros sed aliquet consequat, dolor augue luctus lacus, sed sodales justo purus at neque. Donec a turpis vitae massa elementum tempus. Etiam sit amet lectus vitae urna vehicula imperdiet. Nullam ut justo sit amet urna dignissim malesuada non nec mi. Suspendisse potenti. Ut tristique vestibulum lectus vel blandit.",
        "icon": "static/img/headshots/JDHeadshot.jpg",
    },
    {
        "name": "Chase Hallahan",
        "title": "Mechanical and Integration Engineer",
        "description": "Chase holds a Bachelor's in Mechanical Engineering with a minor in Mathematics from San Diego State University, where he built a strong foundation in applied differential equations for modeling dynamic systems, product design, and manufacturing processes. He began his career as an engineer at a regional brewery plant, overseeing equipment performance and process optimization. For over five years, he has specialized in hands-on automotive design, leading product development, testing protocols, and validation workflows for high-performance components. A collaborative problem-solver, Chase taught himself VBA to automate engineering workflows for himself and his colleagues and has since expanded his skill set to languages like Python and C# to develop custom integration software, calibration automation, and hobby projects—from enterprise-level CAD software integrations to automated fishkeeping systems. As Mechanical and Integration Engineer at Cutthroat Systems, he bridges the gap between hardware and software to deliver end-to-end automation solutions that streamline operations and ensure compliance with industry standards.",
        "icon": "static/img/headshots/ChaseHeadshot.png",
    },
]


def render() -> None:
    with ui.column().classes('w-full mx-auto pt-24 pb-0 gap-4').props('id=about').style(
        "padding: 5px;"
    ):
        ui.label('Meet Our Team').classes(
            'text-7xl italic font-bold self-center pb-4'
        ).style(f"color: {theme.Color.SOFT_ORANGE};")

        for i, person in enumerate(people):
            align = "self-start" if i % 2 == 0 else "self-end"
            direction = "flex-row" if i % 2 == 0 else "flex-row-reverse"

            with ui.card().classes(
                f'rounded-2xl shadow-sm w-[65vw] h-auto px-8 py-8 mx-[5vw] {align} '
                f'flex {direction} gap-8 items-stretch'
            ).style(f'background-color: {theme.Color.PARCHMENT};'):
                # Headshot image wrapped in avatar
                with ui.column().classes('w-1/4 justify-center items-center'):
                    with ui.avatar(color="burnt-orange").classes("w-full h-auto"):
                        ui.image(person["icon"])
                # Right side text
                with ui.column().classes('flex-1 items-center px-4'):
                    # Name and title
                    ui.label(person.get("name", "Name")).classes(
                        'text-4xl font-bold'
                    ).style(f"color: {theme.Color.DARK_BROWN}")
                    ui.label(person.get("title", "Title")).classes(
                        'text-3xl italic font-bold'
                    ).style(f"color: {theme.Color.BURNT_ORANGE};")
                    # Horizontal separator
                    ui.separator()
                    # Bio
                    ui.label(person.get("description", "Description")).classes(
                        'text-lg text-justify indent-12 font-medium'
                    )
