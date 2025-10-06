from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_welcome_email(username, email):
    subject = '🎉 Welcome to MyBlog!'
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [email]

    # Render HTML template with user data
    html_content = render_to_string('users/welcome_email.html', {'username': username})
    text_content = f'Hi {username}, welcome to MyBlog!' 

    # Create the email object
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
