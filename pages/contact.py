from nicegui import ui
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import theme

def send_email(name: str, email: str, phone: str, message: str) -> None:
    try:
        # Email configuration
        sender_email = "your_email@example.com"  # Replace with your email
        sender_password = "your_password"        # Replace with your email password
        receiver_email = "receiver_email@example.com"  # Replace with the recipient's email
        
        # Email content
        subject = "New Contact Us Submission"
        body = f"""
        Name: {name}
        Email: {email}
        Phone: {phone}
        Message: {message}
        """

        # Setting up the email message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Sending the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        
        ui.notify("Your message has been sent successfully!")
    except Exception as e:
        ui.notify(f"Failed to send message: {e}", color="negative")


def render() -> None:
    with ui.column().classes('w-full mx-auto pt-24 pb-16 gap-8 items-center ').props('id=contact-us').style("padding: 5px"):
        # Header
        ui.label('Contact Us').classes('text-5xl italic font-bold text-center').style(f"color: {theme.Color.PARCHMENT};")
        
        # Introduction
        ui.label(
            "We'd love to hear from you! Whether you have questions, feedback, or inquiries about our services, "
            "our team is here to help. Fill out the form below, and we’ll get back to you as soon as possible."
        ).classes('text-lg text-center font-medium').style(f"color: {theme.Color.PARCHMENT}; max-width: 80ch;")

        # Contact Form Card
        with ui.card().classes('rounded-2xl shadow-lg w-2/3 px-8 py-6 flex flex-col items-center gap-4').style(f"background-color: {theme.Color.PARCHMENT};"):
            # Name Field
            with ui.column().classes('w-full gap-2'):
                ui.label('Your Name').classes('text-left font-bold').style(f"color: {theme.Color.DARK_BROWN};")
                ui.input().props('placeholder="Enter your full name"').classes('w-full px-4 py-2 border rounded').style('background-color: white;')

            # Email Field
            with ui.column().classes('w-full gap-2'):
                ui.label('Your Email').classes('text-left font-bold').style(f"color: {theme.Color.DARK_BROWN};")
                ui.input().props('placeholder="Enter your email address"').classes('w-full px-4 py-2 border rounded').style('background-color: white;')

            # Phone Number Field
            with ui.column().classes('w-full gap-2'):
                ui.label('Your Phone Number').classes('text-left font-bold').style(f"color: {theme.Color.DARK_BROWN};")
                ui.input().props('placeholder="Enter your phone number"').classes('w-full px-4 py-2 border rounded').style('background-color: white;')

            # Message Field
            with ui.column().classes('w-full gap-2'):
                ui.label('Your Message').classes('text-left font-bold').style(f"color: {theme.Color.DARK_BROWN};")
                ui.textarea().props('placeholder="Type your message here..." rows=5').classes('w-full px-4 py-2 border rounded').style('background-color: white;')

            # Submit Button
            ui.button('Send Message', on_click=lambda: ui.notify('Message Sent!')).classes('px-6 py-2 rounded-lg text-white').props(f'color=orange-8')
