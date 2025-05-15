from nicegui import ui

import theme

services = {
    # Column 1 -----------------------------------------------
    "Hardware Design": [
        {
            "title": "Production Design",
            "description": "Our engineers leverage decades of experience to design mechanical mechanisms tailored to meet industry standards. We focus on creating robust, scalable, and efficient solutions for production.",
            "icon": "ree",
        },
        {
            "title": "Thermal Engineering Consultation",
            "description": "Optimize your systems with expert thermal analysis and engineering. From heat dissipation to thermal management, we ensure peak performance under demanding conditions.",
            "icon": "ree",
        },
        {
            "title": "Rapid Protyping & Manufacturing Consultation",
            "description": "Accelerate your product development with our rapid prototyping services. We provide guidance on material selection, manufacturing techniques, and optimization for production.",
            "icon": "ree",
        },
    ],
    # Column 2 -----------------------------------------------
    "Software Engineering": [
        {
            "title": "Data Visualization and Analytics",
            "description": "Transform raw data into actionable insights with our advanced visualization tools. We specialize in creating intuitive dashboards and analytics systems to empower decision-making.",
            "icon": "ree",
        },
        {
            "title": "Integrated Software & Low-level Programming",
            "description": "Our expertise includes firmware development, system integration, and low-level programming to ensure seamless operation and compatibility with hardware.",
            "icon": "ree",
        },
        {
            "title": "Custom Software Developement", 
            "description": "From concept to deployment, we develop tailored software solutions designed to address unique business challenges and enhance operational efficiency.", 
            "icon": "ree"},
    ],
    # Column 3 -----------------------------------------------
    "System Integration": [
        {
            "title": "Precision and Scientific Control Systems",
            "description": "Specializing in high-accuracy control systems, we design and integrate solutions for scientific and industrial applications that require uncompromising precision.",
            "icon": "ree",
        },
        {"title": "Calibration Systems and Equipment Automations", "description": "Streamline your system processes with our advanced automation solutions. We specialize in developing systems that seamlessly integrate with your equipment, enabling automated data collection, precision adjustments, and comprehensive reporting. Our solutions reduce manual intervention, enhance accuracy, and save valuable time.", "icon": "ree"},
        {"title": "Deployment and Training", "description": "Ensure smooth transitions and effective system use with our comprehensive deployment and training services. We provide the tools and knowledge your team needs to succeed.", "icon": "ree"},
    ],
}

imglist = ["static/img/services/Hardware Design.jpg","static/img/services/Software Engineering.jpg","static/img/services/System Integration.jpg"]


def render() -> None:
    with ui.column().classes('w-full mx-auto pt-24 pb-0 gap-4 items-center').props('id=about'):
                
        ui.image('static/img/services/TroutCard.png').style(
            "width: 600px; height: 200px; object-fit: fill; margin: 0; padding: 0; display:"
            )
        
        ui.label('Services Provided').classes('text-5xl italic font-bold text-center pb-4').style(f"color: {theme.Color.PARCHMENT};")
        """
        with ui.card().classes('rounded-2xl shadow-lg w-auto px-20 py-2 flex flex-col items-center text-center').style(f'background-color: {theme.Color.SOFT_ORANGE};'):
            with ui.row().classes('w-full justify-center gap-3 flex-wrap'):
                ui.image(theme.Icon.HARDWARE).props("fit=contain").classes(
                                "w-16 h-16 service-icon"
                            ).style("overflow: visible; object-fit: contain;")
                ui.image(theme.Icon.SOFTWARE).props("fit=contain").classes(
                                "w-16 h-16 service-icon"
                            ).style("overflow: visible; object-fit: contain;")
                ui.image(theme.Icon.INTEGRATION).props("fit=contain").classes(
                                "w-16 h-16 service-icon"
                            ).style("overflow: visible; object-fit: contain;")
                """
                           
        ui.label(
            "At Cutthroat Systems, our team of exceptional engineers brings together expertise in software, mechanical, and aerospace engineering to tackle even the most complex challenges. "
            "We specialize in consulting, CAD design and prototyping, precision mechanical engineering, aerospace solutions, custom software development, and systems design for calibration and automation. "
            "We are committed to delivering innovative solutions tailored to the unique needs of each client, ensuring every project is approached with creativity and precision. "
            "Our mission is to provide cutting-edge services that empower your business to thrive. "
            "Client satisfaction is at the heart of everything we do, and we take pride in transforming challenges into opportunities. "
        ).classes('text-lg text-center font-medium').style(
            f"color: {theme.Color.PARCHMENT}; max-width: 120ch;"
        )

        with ui.row().classes('w-full justify-center gap-3 flex-wrap'):
            keys_list = list(services.keys())  # Get the keys for the columns
            with ui.card().classes('rounded-2xl shadow-lg w-25% min-w-[150px] px-4 py-4 flex flex-col items-center text-center hover:shadow-2xl transition-shadow duration-300').style(f"background-color: {theme.Color.PARCHMENT};"):
                for i, key in enumerate(keys_list):
                    with ui.column().classes('w-full items-center text-left gap-2'):
                        # Parallax Image
                        with ui.element("q-parallax").props(f"src='{imglist[i]}' height='150' auto-width speed=30").style('background-position: bottom;'):
                            with ui.card().classes('rounded-2xl shadow-lg w-auto px-2 py-2 flex flex-col items-center text-center').style(f'background-color: {theme.Color.SOFT_ORANGE};'):
                                ui.label(key).classes('text-4xl italic font-bold').style(
                                    f"color: {theme.Color.DARK_BROWN};"
                                )
                        ui.separator()
                        with ui.column().classes('w-full text-left gap-2'):
                            add_info(key)

       

def add_info(key: str) -> None:
    for i, service in enumerate(services[key]):
        ui.label(service["title"]).classes('text-2xl text-left font-bold').style(f"color: {theme.Color.BURNT_ORANGE};")
        ui.label(service["description"]).classes('text-lg text-left font-medium').style(f"color: {theme.Color.DARK_BROWN};")
        if (i != len(services) - 1):
            ui.separator()

    """def clicked(key : str ) -> None: #Function to populate screen w/ button info
        right_column.clear()

        for service in services[key]:
            with right_column:
                with ui.card(align_items="baseline").classes(f'rounded-2xl shadow-lg').style(f'background-color: {theme.Color.PARCHMENT}; width: 30vw; min-width: 200px;'):
                    with ui.().classes('w-full items-center'):
                        ui.labelcolumn(service["title"]).classes('text-3xl text-center font-bold')
                    with ui.column(align_items="start").classes('w-full mx-auto pt-0 pb-0 gap-1 items-left'):
                        ui.label(service["description"]).classes('text-lg text-left font-medium')"""
