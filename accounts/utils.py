import hashlib
from datetime import datetime
from datetime import timedelta
from django.utils.crypto import get_random_string
from .models import Profile
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings

def generate_activation_key(username):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    secret_key = get_random_string(20, chars)
    return hashlib.sha256((secret_key + username).encode('utf-8')).hexdigest()

# Email context is hard coded below
def send_activation_email(user):
    profile = Profile.objects.get(user=user)
    profile.activation_key = generate_activation_key(user.username)
    profile.key_expires = datetime.strftime(datetime.now() + timedelta(days=2),
                                            '%Y-%m-%d %H:%M:%S')
    profile.save()
    text_temp = get_template('accounts/activate_email.txt')
    html_temp = get_template('accounts/activate_email.html')
    subject = 'Activate your account - Project'
    from_email = settings.DEFAULT_FROM_EMAIL
    to = user.email
    email_context = {'username': user.username,
                     'activation_key': profile.activation_key,
                     'protocol': 'http',
                     'domain': 'localhost:8000',
                     'site_name': 'Project',}
    text_content = text_temp.render(context=email_context)
    html_content = html_temp.render(context=email_context)
    message = EmailMultiAlternatives(subject, text_content, from_email, [to])
    message.attach_alternative(html_content, "text/html")
    message.send()
