import html
import os
from typing import Any, Dict

import phonenumbers
import pycountry
import requests
from email_validator import EmailNotValidError, validate_email
from nicegui import ui
from nicegui.events import ValueChangeEventArguments
from phonenumbers import NumberParseException

import theme

API_KEY = os.getenv("ZEPTO_API_KEY")
RECAPTCHA_SITE_KEY = os.getenv("RECAPTCHA_SITE_KEY")
RECAPTCHA_SECRET_KEY = os.getenv("RECAPTCHA_SECRET_KEY")

ui.add_head_html("""
  <script src="https://www.google.com/recaptcha/api.js" async defer></script>
""")

OPTIONS: dict[str, str] = {}
ISO_TO_DIAL: dict[str, str] = {}
ISO_TO_FLAG: dict[str, str] = {}

for c in sorted(pycountry.countries, key=lambda c: c.name):  # type: ignore
    iso = str(c.alpha_2)  # type: ignore
    code = phonenumbers.country_code_for_region(iso)

    if code == 0:
        continue

    flag = "".join(chr(0x1F1E6 + ord(ch) - 65) for ch in iso)
    dial = f"+{code}"

    label = f"{flag}  {c.name} ({dial})"  # type: ignore
    OPTIONS[iso] = label
    ISO_TO_DIAL[iso] = dial
    ISO_TO_FLAG[iso] = flag


def _send_email(name: str, email: str, phone: str, message: str) -> None:
    url = "https://api.zeptomail.com/v1.1/email"

    payload: Dict[str, Any] = {
        "from": {"address": "noreply@cutthroatsystems.com"},
        "to": [
            {
                "email_address": {
                    "address": "chase@cutthroatsystems.com",  #############################################
                    "name": "Cutthroat Team",
                }
            }
        ],
        "subject": f"{name}: Contact Form Submission",
        "htmlbody": (
            f"<div>"
            f"You've recieved a submission from https://cutthroat.systems/contact<br>"
            f"<b>Name:</b> {html.escape(name)}<br>"
            f"<b>Email:</b> {html.escape(email)}<br>"
            f"<b>Phone:</b> {phone or '—'}<br>"
            f"<b>Message:</b><br> {html.escape(message)}"
            f"</div>"
        ),
    }

    headers: Dict[str, Any] = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Zoho-enczapikey {API_KEY}",
    }

    try:
        r = requests.post(url, json=payload, headers=headers, timeout=10)
        ui.notify("Message sent!" if r.ok else f"Send failed: {r.text}", type="positive" if r.ok else "negative")
    except requests.RequestException as err:
        ui.notify(f"Network error: {err}", type="negative")


# Validation function on click
def _validate_input(
    name: ui.input,
    email: ui.input,
    cc: ui.select,
    phone: ui.input,
    message: ui.textarea,
) -> None:
    for field in (name, email, phone, message):
        field.props("error=false error-message=''")
    send_email = True

    # name and message validation
    if not name.value.strip():
        name.props('error error-message="Name is required."')
        send_email = False
    if not message.value.strip():
        message.props("error error-message='A message is required.'")
        send_email = False

    # email validation
    if email.value.strip():
        try:
            validate_email(email.value.strip())
        except EmailNotValidError as e:
            email.props(f"error error-message='{e}'")
            send_email = False

    else:
        email.props("error error-message='Email is required.'")
        send_email = False

    # phone validation
    formatted_phone = ""
    if phone.value.strip():
        try:
            parsed = phonenumbers.parse(phone.value.strip(), cc.value)
            if not (phonenumbers.is_possible_number(parsed) and phonenumbers.is_valid_number(parsed)):
                raise ValueError("fails plausibility check")

            formatted_phone = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)

        except (NumberParseException, ValueError):
            phone.props("error error-message='Phone number is invalid.'")
            send_email = False

    # pass to email function
    if not send_email:
        ui.notify(
            "No message was sent. Please fix the highlighted fields and try again.",
            type="negative",
        )
        return
    else:
        _send_email(
            name.value,
            email.value,
            formatted_phone,
            message.value,
        )


# Function to render the form
def render() -> None:
    # UI rendering
    with (
        ui.column()
        .classes("w-full mx-auto pt-24 pb-16 gap-8 items-center")
        .props("id=contact-us")
        .style("padding: 5px")
    ):
        ui.label("Contact Us").classes("text-7xl italic font-bold text-center").style(
            f"color: {theme.Color.SOFT_ORANGE};"
        )
        ui.label(
            "We'd love to hear from you! Whether you have questions, feedback, or inquiries about our services, "
            "our team is here to help. Fill out the form below, and we'll get back to you as soon as possible."
        ).classes("text-lg text-center font-medium").style(f"color: {theme.Color.PARCHMENT}; max-width: 80ch;")

        with (
            ui.card()
            .classes("rounded-2xl shadow-lg w-[90vw] px-8 py-6 flex flex-col items-start gap-4 sm:w-[50vw]")
            .style(f"background-color: {theme.Color.PARCHMENT};")
        ):
            input_style = f"background-color: white; border-radius: 4px; --q-field-border-color: {theme.Color.DARK_BROWN}; --q-field-hover-border-color: {theme.Color.BURNT_ORANGE};"

            # *Name
            ui.label("Name").classes("font-bold text-xl").style(f"color: {theme.Color.DARK_BROWN};")
            name = (
                ui.input()
                .props('placeholder="Enter your full name" required')
                .classes("w-full px-4 py-2 border rounded")
                .style(input_style)
            )

            # *Email
            ui.label("Email").classes("font-bold text-xl pt-1.5").style(f"color: {theme.Color.DARK_BROWN};")
            email = (
                ui.input()
                .props("placeholder='Enter your email address' type='email' required")
                .classes("w-full px-4 py-2 border rounded")
                .style(input_style)
            )

            # *Phone number
            ui.label("Phone Number").classes("font-bold text-xl pt-1.5").style(f"color: {theme.Color.DARK_BROWN};")

            # country code select element on_change
            def _compact_view(e: ValueChangeEventArguments) -> None:
                iso = e.value
                flag = ISO_TO_FLAG.get(iso, "")
                cc_select.props(f'display-value="{ISO_TO_DIAL.get(iso, "")}" prefix="{flag}"')
                if iso == "US":
                    phone.props('mask="(###) ###-####"')
                else:
                    phone.props('mask="#################"')

            with ui.row().classes("justify-start items-end gap-2 w-full"):
                cc_select = (
                    ui.select(
                        options=OPTIONS,
                        value="US",
                        on_change=_compact_view,
                    )
                    .props(
                        "outlined virtual-scroll "
                        f'display-value="+1" prefix="{ISO_TO_FLAG["US"]}" '
                        'popup-content-style="height: 40vh; width: 30ch"'
                    )
                    .classes("mb-1")
                    .style(input_style)
                )

                phone = (
                    ui.input()
                    .props('placeholder="Enter your phone number (optional)" type="tel" mask="(###) ###-####"')
                    .classes("w-[40ch] px-4 py-2 border rounded")
                    .style(input_style)
                )

            # *Message
            ui.label("Message").classes("font-bold text-xl").style(f"color: {theme.Color.DARK_BROWN};")
            message = (
                ui.textarea()
                .props('placeholder="Type your message here..." rows=5 required')
                .classes("w-full px-4 py-2 border rounded")
                .style(input_style)
            )

            # *Submit
            with ui.row():
                ui.button(
                    "Send Message",
                    on_click=lambda: _validate_input(name, email, cc_select, phone, message),
                ).classes("px-6 py-2 mt-4 mb-2 rounded-lg text-white")
