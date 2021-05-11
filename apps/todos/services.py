from django.core import mail


class Services:
    @staticmethod
    def send_mail(subject, body, to, **kwargs):
        message = mail.EmailMessage(subject, body, to=to, **kwargs)
        message.send()
