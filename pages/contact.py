import re

from nicegui import ui

import theme


# Function to send email
def send_email(name: str, email: str, phone: str, message: str) -> None:
    """url = "https://api.zeptomail.com/v1.1/email"

    payload = {
        "from": {"address": "noreply@cutthroatsystems.com"},
        "to": [
            {
                "email_address": {
                    "address": "team@cutthroatsystems.com",
                    "name": "Cutthroat Team"
                }
            }
        ],
        "subject": f"{name}: Contact Form Submission",
        "htmlbody": (
            f"<div>"
            f"<b>Name:</b> {name}<br>"
            f"<b>Email:</b> {email}<br>"
            f"<b>Phone:</b> {phone}<br>"
            f"<b>Message:</b> {message}"
            f"</div>"
        )
    }

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'authorization': "Zoho-enczapikey wSsVR60l+hajD/17mzetc71rn19SDlmnQEosjlDw6yP1HarE/Mdvn0zKUQahGvcYFmZgHTIaoOp9nRsE2jZdjN4ty10GASiF9mqRe1U4J3x17qnvhDzOW2ldkBSLLooJzwlinWVjEMsm+g==",
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    if response.ok:
        ui.notify('Message Sent!', type="positive")
    else:
        ui.notify(f'Failed to send message: {response.text}', type='negative')
    """
    ui.notify('Message Sent!', type="positive")


# Function to render the form
def render() -> None:

    # Validation function
    def validate_and_send():
        phone_pattern = re.compile(
            r'^(\+?1[\s-]?)?(\(?\d{3}\)?[\s-]?)\d{3}[\s-]?\d{4}$'
        )
        if not name.value:
            ui.notify("Name is required", type="negative")
            return
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email.value):
            ui.notify("Invalid email format", type="negative")
            return
        if not phone_pattern.match(phone.value):
            ui.notify("Invalid phone number format", type="negative")
            return
        if not message.value:
            ui.notify("Message cannot be empty", type="negative")
            return
        send_email(name.value, email.value, phone.value, message.value)

    # UI rendering
    with ui.column().classes('w-full mx-auto pt-24 pb-16 gap-8 items-center').props(
        'id=contact-us'
    ).style("padding: 5px"):
        ui.label('Contact Us').classes('text-7xl italic font-bold text-center').style(
            f"color: {theme.Color.SOFT_ORANGE};"
        )
        ui.label(
            "We'd love to hear from you! Whether you have questions, feedback, or inquiries about our services, "
            "our team is here to help. Fill out the form below, and we’ll get back to you as soon as possible."
        ).classes('text-lg text-center font-medium').style(
            f"color: {theme.Color.PARCHMENT}; max-width: 80ch;"
        )

        with ui.card().classes(
            'rounded-2xl shadow-lg w-[90vw] px-8 py-6 flex flex-col items-start gap-4 sm:w-[50vw]'
        ).style(f"background-color: {theme.Color.PARCHMENT};"):
            ui.label('Name').classes('font-bold text-xl').style(
                f"color: {theme.Color.DARK_BROWN};"
            )
            name = (
                ui.input()
                .props('placeholder="Enter your full name"')
                .classes('w-full px-4 py-2 border rounded')
                .style('background-color: white;')
            )

            ui.label('Email').classes('font-bold text-xl').style(
                f"color: {theme.Color.DARK_BROWN};"
            )
            email = (
                ui.input()
                .props('placeholder="Enter your email address"')
                .classes('w-full px-4 py-2 border rounded')
                .style('background-color: white;')
            )

            ui.label('Phone Number').classes('font-bold text-xl').style(
                f"color: {theme.Color.DARK_BROWN};"
            )
            phone = (
                ui.input()
                .props('placeholder="Enter your phone number"')
                .classes('w-full px-4 py-2 border rounded')
                .style('background-color: white;')
            )

            ui.label('Message').classes('font-bold text-xl').style(
                f"color: {theme.Color.DARK_BROWN};"
            )
            message = (
                ui.textarea()
                .props('placeholder="Type your message here..." rows=5')
                .classes('w-full px-4 py-2 border rounded')
                .style('background-color: white;')
            )

            ui.button('Send Message', on_click=validate_and_send).classes(
                'px-6 py-2 rounded-lg text-white'
            ).props('color=burnt-orange')
