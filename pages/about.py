from nicegui import ui

import theme

topBlurb = (
    "Cutthroat Systems started with a small team of engineers united by a passion for solving automation challenges. "
    "We create custom solutions—from CAD design and prototyping to full hardware-software integration—that streamline calibration, testing, and manufacturing. "
    "Our hands-on approach and software-driven workflows help businesses simplify complexity and boost efficiency."
)

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
        "description": "Our engineers have combined decades of experience designing mechanical mechanisms within the industry.",
        "icon": "static/img/headshots/JDHeadshot.jpg",
    },
    {
        "name": "Chase Hallahan",
        "title": "Mechanical and Integration Engineer",
        "description": "Chase holds a Bachelor's in Mechanical Engineering with a minor in Mathematics from San Diego State University, where he built a strong foundation in applied differential equations for modeling dynamic systems, product design, and manufacturing processes. He began his career as an engineer at a regional brewery plant, overseeing equipment performance and process optimization. For over five years, he has specialized in hands-on automotive design, leading product development, testing protocols, and validation workflows for high-performance components. A collaborative problem-solver, Chase taught himself VBA to automate engineering workflows for himself and his colleagues and has since expanded his skill set to languages like Python and C# to develop custom integration software, calibration automation, and hobby projects—from enterprise-level CAD software integrations to automated fishkeeping systems. As Mechanical and Integration Engineer at Cutthroat Systems, he bridges the gap between hardware and software to deliver end-to-end automation solutions that streamline operations and ensure compliance with industry standards.",
        "icon": "static/img/headshots/ChaseHeadshot.png",
    },
]

addVSep = (
    lambda: ui.separator()
    .props("vertical")
    .style('border-left: 4px solid var(--theme-color-soft-orange); height: 100%;')
)


def makePerson(person: dict):
    with ui.card().classes('rounded-2xl shadow-sm w-full px-4 py-8 h-auto').style(
        f'background-color: {theme.Color.PARCHMENT};'
    ):
        with ui.row().classes('w-full justify-center gap-8 items-stretch'):
            with ui.column().classes('w-1/3 items-center'):
                with ui.avatar(color="burnt-orange", size="28rem"):
                    ui.image(person["icon"])

            addVSep()

            with ui.column().classes('w-1/2 items-center text-center'):
                ui.label(person.get("name", "Name")).classes(
                    'text-4xl text-left font-bold'
                ).style(f"color: {theme.Color.DARK_BROWN}")
                ui.label(person.get("title", "Title")).classes(
                    'text-3xl text-left italic font-bold'
                ).style(f"color: {theme.Color.BURNT_ORANGE};")
                ui.separator()
                ui.label(person.get("description", "Description")).classes(
                    'text-lg text-left font-medium'
                )


def render() -> None:
    with ui.column().classes('w-full mx-auto pt-24 pb-0 gap-4 items-center').props(
        'id=about'
    ).style("padding: 5px;"):
        ui.label('Meet Our Team').classes(
            'text-5xl italic font-bold text-center pb-4'
        ).style(f"color: {theme.Color.SOFT_ORANGE};")
        # ui.label(topBlurb).classes('text-lg text-center font-medium').style(
        #     f"color: {theme.Color.PARCHMENT}; max-width: 120ch;"
        # )
        for person in people:
            makePerson(person)
