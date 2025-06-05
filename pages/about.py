from nicegui import ui

import theme

topBlurb = "\n".join([
    "At Cutthroat Systems, our team of exceptional engineers brings together expertise in software, mechanical, and aerospace engineering to tackle even the most complex challenges. ",
    "We specialize in consulting, CAD design and prototyping, precision mechanical engineering, aerospace solutions, custom software development, and systems design for calibration and automation. ",
    "We are committed to delivering innovative solutions tailored to the unique needs of each client, ensuring every project is approached with creativity and precision. ",
    "Our mission is to provide cutting-edge services that empower your business to thrive. ",
    "Client satisfaction is at the heart of everything we do, and we take pride in transforming challenges into opportunities. "
])

Pat_text = """Patrick is a seasoned project manager, analytics expert, and software developer with a unique blend of financial and technical expertise. He began his career managing a $500 million portfolio while working with leading lending institutions, including Blackstone, Wells Fargo, and Bank of America, where he developed predictive models to forecast loan performance and detect risks in complex financing operations.

\n\nHis transition into software development began with a breakthrough in gamification—designing a funding leaderboard that boosted productivity and morale. This sparked a passion for creating data-driven solutions to optimize workflows and enhance business performance.

Now leading financial strategy and software architecture at Cutthroat Systems, Patrick combines his deep analytical skills, business acumen, and software development expertise to deliver innovative engineering and software solutions. Currently pursuing a Master’s in Software Engineering, he bridges the gap between business, data, and technology to drive company success."""



people = [
        {
            "name":"Jarred Druzynski",
            "title": "Production Design",
            "description": "Our engineers have combined decades of experience designing mechanical mechanisms within the industry.",
            "icon":"static/img/headshots/JDHeadshot.jpg"
        },
        {
            "name":"Patrick Miller",
            "title": "Business Analytics and Software Design",
            "description": Pat_text,
            "icon":"static/img/headshots/PatHeadshot.png"
        },
                {
            "name":"Chase Hallahan",
            "title": "",
            "description": "",
            "icon":"static/img/headshots/ChaseHeadshot.png"
        },
]

addVSep = lambda : ui.separator()\
    .props("vertical")\
    .style('border-left: 4px solid var(--theme-color-soft-orange); height: 100%;')


def makePerson(person:dict):
    with ui.card().classes('rounded-2xl shadow-sm w-full px-4 py-8').style(
            f'background-color: {theme.Color.PARCHMENT};'
        ):
            with ui.row().classes('w-full justify-center gap-8'):
                with ui.column().classes('w-1/3 h-full items-center text-center'):
                    with ui.avatar().classes("flex items-center justify-center w-full h-auto"):
                        ui.image(person.get("icon","https://nicegui.io/logo_square.png"))

                addVSep()

                with ui.column().classes('w-1/2 items-center text-center'):
                    ui.label(person.get("name","Name")).classes('text-4xl text-left italic font-bold').style(
                            f"color: {theme.Color.BURNT_ORANGE};"
                        )
                    ui.label(person.get("title","Title")).classes('text-3xl text-left font-bold')
                    ui.separator()
                    ui.label(person.get("description","Description")).classes('text-lg text-left font-medium')




def render() -> None:
    with ui.column().classes('w-full mx-auto pt-24 pb-0 gap-4 items-center').props(
        'id=about'
    ).style("padding: 5px;"):
        ui.label('About Our People').classes(
            'text-5xl italic font-bold text-center pb-4'
        ).style(f"color: {theme.Color.PARCHMENT};")
        ui.label(topBlurb).classes('text-lg text-center font-medium').style(
            f"color: {theme.Color.PARCHMENT}; max-width: 120ch;"
        )
        for person in people:
            makePerson(person)
