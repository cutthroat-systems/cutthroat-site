from nicegui import ui

import theme

topBlurb = "\n".join([
    "At Cutthroat Systems, our team of exceptional engineers brings together expertise in software, mechanical, and aerospace engineering to tackle even the most complex challenges. ",
    "We specialize in consulting, CAD design and prototyping, precision mechanical engineering, aerospace solutions, custom software development, and systems design for calibration and automation. ",
    "We are committed to delivering innovative solutions tailored to the unique needs of each client, ensuring every project is approached with creativity and precision. ",
    "Our mission is to provide cutting-edge services that empower your business to thrive. ",
    "Client satisfaction is at the heart of everything we do, and we take pride in transforming challenges into opportunities. "
])

Pat_text = """Patrick is a seasoned business project manager, analytics expert, and software developer with a unique blend of financial acumen and technical creativity.


He began his career at some of the nation’s largest lending institutions, managing a portfolio valued at nearly $500 million. Working with industry giants like Blackstone, Wells Fargo, and Bank of America, Patrick played a pivotal role in financing major high-rise developments across New York City. Leveraging his sharp analytical skills and strong foundation in mathematics, he built predictive models that could forecast loan performance and detect early signs of failure—bringing clarity to some of the most complex financing operations.


His path eventually led to a private lending firm focused on small and medium-sized businesses. It was there that Patrick developed a deep respect for entrepreneurship and the calculated risks business owners take every day. Through data-driven analysis, he uncovered how even small operational improvements—like reducing time waste or tightening workflows—could dramatically impact a company’s success.


It was during this time that Patrick made a discovery that would change the course of his career. Recognizing the motivational power of gamification, he designed an in-office funding leaderboard for the sales and underwriting teams. The results? Higher morale, better productivity, and a newfound passion for software. What began as a hobby quickly became a calling. With executive backing, Patrick officially transitioned into software development—and he hasn’t looked back.


Today, Patrick leads financial strategy and business operations at Cutthroat Systems, a forward-thinking software and engineering design firm. While managing the business side, he’s also hands-on with software architecture and development. Currently pursuing a Master’s in Software Engineering, Patrick brings a rare perspective—bridging the worlds of business, data, and code—to help your company thrive."""



people = [
        {
            "name":"Jarred Druzynski",
            "title": "Production Design",
            "description": "Our engineers have combined decades of experience designing mechanical mechanisms within the industry.",
            "icon":"static\img\headshots\JDHeadshot.jpg"
        },
        {
            "name":"Patrick Miller",
            "description":Pat_text,
            "icon":"static\img\headshots\PatHeadshot.jpg"
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
    ):
        ui.label('About Our People').classes(
            'text-5xl italic font-bold text-center pb-4'
        ).style(f"color: {theme.Color.PARCHMENT};")
        ui.label(topBlurb).classes('text-lg text-center font-medium').style(
            f"color: {theme.Color.PARCHMENT}; max-width: 120ch;"
        )

        for person in people:
             makePerson(person)
